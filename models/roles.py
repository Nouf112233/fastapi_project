# # from ..database import Base
# import database
# from sqlalchemy import Column,Integer,String,Date
# from sqlalchemy.orm import relationship
# from models.users import Users

# class Roles(database.Base):
#     __tablename__="roles"
#     id=Column(Integer,primary_key=True,index=True)
#     role=Column(String,index=True)
#     users=relationship("Users", back_populates="roles")
