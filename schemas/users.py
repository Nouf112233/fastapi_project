from typing import Optional,List
from pydantic import BaseModel
from schemas import posts

class Users(BaseModel):
    id:Optional[int]=None
    email:str
    password:str
    username:str
    class Config:  # serialize our sql obj to json
        orm_mode = True

# class ShowUser(BaseModel):
#     name: str
#     email: str
#     username:str
#     posts: List[posts.Posts] = []
#     class Config:  # serialize our sql obj to json
#         orm_mode = True
   