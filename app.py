import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from controllers.animerank import lista, pesquisa
from controllers.auth import decode_jwt_token, create_jwt_token
from controllers.user import create_user, logar, get_user
from models.query import Query
from models.user import Login

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get('/user')
def read_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_jwt_token(token)
        user = get_user(int(payload["sub"]))
        return user
    except Exception as e:
        print("Error decoding token:", e)
        raise


@app.get('/')
def base() -> list[dict]:
    return lista()


@app.post('/query')
def query(inputs: Query) -> list[dict]:
    response = pesquisa(inputs.query)
    return response


@app.post('/create')
def create(inputs: Login) -> int:
    response = create_user(inputs.username, inputs.email, inputs.password)
    return response


@app.post('/login')
def login(inputs: Login) -> dict:
    result = logar(inputs.email, inputs.password)
    if int(result["user_id"]) > 0:
        token = create_jwt_token({"sub": f'{result["user_id"]}'})
        print("Generated Token:", token)
        return {"access_token": token, "token_type": "bearer", "user": f'{result["user_id"]}'}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
