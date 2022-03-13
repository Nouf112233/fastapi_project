# from database import Base
# from sqlalchemy import Column,Integer,String,Date,Boolean,ForeignKey
# from sqlalchemy.orm import relationship


# class Roles(Base):
#     __tablename__="roles"
#     id=Column(Integer,primary_key=True,index=True)
#     role=Column(String,index=True)
#     users=relationship("Users", back_populates="roles")

# class Comments(Base):
#     __tablename__="comments"
#     id=Column(Integer,primary_key=True,index=True)
#     disc=Column(String,index=True)
#     time=Column(Date,index=True)
#     username=Column(String,index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     post_id = Column(Integer, ForeignKey("posts.id"))
#     user=relationship("Users", back_populates="comments")
#     post=relationship("Posts", back_populates="comments")

# class Likes(Base):
#     __tablename__="likes"
#     id=Column(Integer,primary_key=True,index=True)
#     like=Column(Boolean,default=False, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     post_id = Column(Integer, ForeignKey("posts.id"))
#     user=relationship("Users", back_populates="likes")
#     post=relationship("Posts", back_populates="likes")

# class Posts(Base):
#     __tablename__="posts"
#     id=Column(Integer,primary_key=True,index=True)
#     disc=Column(String,index=True)
#     image=Column(String)
#     time=Column(Date,index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     user=relationship("Users", back_populates="posts")
#     like=relationship("Likes", back_populates="posts")
#     comment=relationship("Comments", back_populates="posts")

# class Users(Base):
#     __tablename__="users"
#     id=Column(Integer,primary_key=True,index=True)
#     email=Column(String,index=True)
#     password=Column(String,index=True)
#     username=Column(String,index=True)
#     role_id = Column(Integer, ForeignKey("roles.id"))
#     role=relationship("Roles", back_populates="users")
#     like=relationship("Likes", back_populates="users")
#     post=relationship("Posts", back_populates="users")
#     comment=relationship("Comments", back_populates="users")


