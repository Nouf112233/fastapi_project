
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

postgresql_url = "postgresql://postgres:Almasah1&2@localhost:5000/social_media"
engine = create_engine(postgresql_url,echo=True)
localsession =sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base= declarative_base()

def get_db():
    db=localsession()
    try:
        yield db
    finally:
        db.close()


