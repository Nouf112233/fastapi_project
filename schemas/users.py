from typing import Optional,List
from pydantic import BaseModel
from schemas.posts import Posts

class Users(BaseModel):
    id:Optional[int]=None
    email:str
    password:str
    username:str
    class Config:  # serialize our sql obj to json
        orm_mode = True

class ShowUser(BaseModel):
    email: str
    password:str
    username:str
    posts: List[Posts] = []
    class Config:  # serialize our sql obj to json
        orm_mode = True
   