import database 
from sqlalchemy import Column,Integer,String,Date,Table,ForeignKey
from sqlalchemy.orm import relationship
# from users import Users
# from likes import Likes
# from comments import Comments

class Posts(database.Base):
    __tablename__="posts"
    id=Column(Integer,primary_key=True,index=True)
    disc=Column(String,index=True)
    image=Column(String)
    time=Column(Date,index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user=relationship("Users", back_populates="posts")
    like=relationship("Likes", back_populates="posts")
    comment=relationship("Comments", back_populates="posts")