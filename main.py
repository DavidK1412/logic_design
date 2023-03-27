from fastapi import FastAPI
from models.request_body import BaseBody, OperationBody
from utils.number_set import get_number_base
from utils.operations import addition, subtraction, multiplication, division
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/base/")
async def get_base(num: BaseBody):
    base_num1 = get_number_base(num.num)
    base_num2 = get_number_base(num.num2)
    return {"base": base_num1 if base_num1 >= base_num2 else base_num2}


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