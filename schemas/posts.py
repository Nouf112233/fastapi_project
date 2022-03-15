from typing import Optional,List
from pydantic import BaseModel
from datetime import date
from schemas.comments import Comments
from schemas.likes import Likes

class Posts(BaseModel):
    id:Optional[int]=None
    disc:str
    image:str
    time:date
    class Config:  # serialize our sql obj to json
        orm_mode = True

class ShowPost(BaseModel):
    disc:str
    image:str
    time:date
    comments: List[Comments] = []
    likes: List[Likes] = []
    class Config:  # serialize our sql obj to json
        orm_mode = True

class ShowPosts(BaseModel):
    disc:str
    image:str
    time:date
    likes: List[Likes] = []
    class Config:  # serialize our sql obj to json
        orm_mode = True
