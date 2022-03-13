from typing import Optional,List
from pydantic import BaseModel
from datetime import date
from schemas import comments,likes

class Posts(BaseModel):
    id:Optional[int]=None
    disc:str
    image:str
    time:date
    class Config:  # serialize our sql obj to json
        orm_mode = True

# class ShowPosts(BaseModel):
#     disc:str
#     image:str
#     time:date
#     comments: List[comments.Comments] = []
#     likes: List[likes.Likes] = []
#     class Config:  # serialize our sql obj to json
#         orm_mode = True
