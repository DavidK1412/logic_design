from fastapi import FastAPI
from models.request_body import BaseBody, OperationBody
from utils.number_set import get_number_base
from utils.operations import addition, subtraction, multiplication, division


app = FastAPI()


@app.get("/base/")
async def get_base(num):
    return {"base": get_number_base(num.num)}


@app.post("/addition/")
async def get_addition(num: OperationBody):
    return {"result": addition(num.num1, num.num2, num.base)}

@app.post("/subtraction/")
async def get_subtraction(num: OperationBody):
    return {"result": subtraction(num.num1, num.num2, num.base)}

@app.post("/multiplication/")
async def get_multiplication(num: OperationBody):
    return {"result": multiplication(num.num1, num.num2, num.base)}

@app.post("/division/")
async def get_division(num: OperationBody):
    return {"result": division(num.num1, num.num2, num.base)}