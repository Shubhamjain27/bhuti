from fastapi import FastAPI, File
from pydantic import BaseModel
app = FastAPI()
import pickle
from starlette.middleware.cors import CORSMiddleware
import numpy as np

from new_eval import *
import base64
from starlette.requests import Request
import io
class Item(BaseModel):
    name :str
    price: float
    # img_file : bytes=File(...)
    # is_offer: bool = None

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
def read_root():
    return{"Hello":"World"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = None):
    return{"item_id" : item_id, "q" :q}

@app.put('/items/{item_id}')
def update_item(item_id:int, item: Item):
    return{"item_name": item.name, "item_id": item_id}


@app.post('/api/')
def predict():
    print('received')
    
    # image = base64.b64encode(image).decode("utf-8")
    # print(data)
    # model = pickle.load(open('model.pkl','rb'))
    predict = main()
    print("predict", predict)
    return(predict)