import database 
from sqlalchemy import Column,Integer,String,Date,Table,ForeignKey,Boolean
from sqlalchemy.orm import relationship
# from .users import Users
# from .posts import Posts


class Likes(database.Base):
    __tablename__="likes"
    id=Column(Integer,primary_key=True,index=True)
    like=Column(Boolean,default=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    user=relationship("Users", back_populates="likes")
    post=relationship("Posts", back_populates="likes")