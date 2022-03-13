from typing import Optional,List
from pydantic import BaseModel

class Likes(BaseModel):
    id:Optional[int]=None
    like:bool
    class Config:  # serialize our sql obj to json
        orm_mode = True

class ShowLikes(BaseModel):
    like:bool
    class Config:  # serialize our sql obj to json
        orm_mode = True
