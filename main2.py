from fastapi import FastAPI


app=FastAPI()
# Base.metadata.create_all(engine)

@app.get("/")
def hello():
    return {"msg":"helo"}

#app.include_router(roles.router)
#app.include_router(users.router)
# app.include_router(posts.router)
# app.include_router(comments.router)
# app.include_router(likes.router)