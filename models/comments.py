import database
from sqlalchemy import Column,Integer,String,Date,Table,ForeignKey
from sqlalchemy.orm import relationship
# from .users import Users
# from .posts import Posts


class Comments(database.Base):
    __tablename__="comments"
    id=Column(Integer,primary_key=True,index=True)
    disc=Column(String,index=True)
    time=Column(Date,index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    users=relationship("Users", back_populates="comments")
    posts=relationship("Posts", back_populates="comments")