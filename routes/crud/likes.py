from sqlalchemy.orm import session
from models import likes as m_likes
from schemas import likes as s_likes
from models import posts as m_posts
from schemas import posts as s_posts
from schemas import users as s_users

def create_like(post_id:int,current_user:s_users.Users,db:session):
    new_like = m_likes.Likes(
       like=True,
       user_id=1,
       post_id=post_id
    )
    db.add(new_like)
    db.commit()
    return current_user