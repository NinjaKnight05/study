import uvicorn
import numpy as np
import joblib
import pandas as pd
from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def index():
    return {'message':'Hello coder '}

@app.get('/name')
def names():
    return {'message':'Hello Anurag'}

@app.get('/{naam}')
def Pnaam(naam:str):
    return{'Name is':f"{naam}"}

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)

