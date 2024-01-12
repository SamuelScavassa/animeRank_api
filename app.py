import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from controllers.animerank import lista, pesquisa, create_user

app = FastAPI()

class Item(BaseModel):
    query: str

class Login(BaseModel):
    username: str
    password: str
    email: str

@app.get('/')
def base() -> list[dict]:
    return lista()

@app.post('/query')
def query(inputs: Item) -> list[dict]:
    response = pesquisa(inputs.query)
    return response

@app.post('/create')
def create(inputs: Login) -> int:
    id = create_user(inputs.username,inputs.email,inputs.password)
    return id

if __name__ == '__main__':
    uvicorn.run(app, port=8000)