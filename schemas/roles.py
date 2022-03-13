from typing import Optional
from pydantic import BaseModel

class Roles(BaseModel):
    id: Optional[int]=None
    role:str
    class Config:  # serialize our sql obj to json
        orm_mode = True