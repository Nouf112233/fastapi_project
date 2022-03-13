from sqlalchemy.orm import session
from fastapi import FastAPI,Depends
from database import engine,Base,localsession
from routes.routers import users,posts,comments,likes



app=FastAPI()
#Base.metadata.create_all(engine)
Base.metadata.create_all(bind=engine)


@app.get("/")
def hello():
    return {"msg":"helo"}

# app.include_router(roles.router)
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(likes.router)