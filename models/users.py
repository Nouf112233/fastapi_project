
import database
from sqlalchemy import Column,Integer,String,Date,Table,ForeignKey
from sqlalchemy.orm import relationship



class Users(database.Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,index=True)
    password=Column(String,index=True)
    username=Column(String,index=True)
    # role_id = Column(Integer, ForeignKey("roles.id"))
    # role=relationship("Roles", back_populates="users")
    like=relationship("Likes", back_populates="users")
    post=relationship("Posts", back_populates="users")
    comment=relationship("Comments", back_populates="users")
    
    