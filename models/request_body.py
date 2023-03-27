from pydantic import BaseModel


class OperationBody(BaseModel):
    num1: str
    num2: str
    base: int


class BaseBody(BaseModel):
    num: str
