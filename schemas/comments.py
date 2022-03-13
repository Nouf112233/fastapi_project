from typing import Optional,List
from pydantic import BaseModel
from datetime import date

class Comments(BaseModel):
    id:Optional[int]=None
    disc:str
    time:date
    username:str
    class Config:  # serialize our sql obj to json
        orm_mode = True

class ShowComments(BaseModel):
    disc:str
    time:date
    username:str
    class Config:  # serialize our sql obj to json
        orm_mode = True
