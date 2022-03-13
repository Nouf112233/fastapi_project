
from sqlalchemy.orm import session
from models import posts as m_posts
from schemas import posts as s_posts
from schemas import users as s_users

def create_post(post: s_posts.Posts,current_user:s_users.Users,db:session):

    new_post = m_posts.Posts(
       disc=post.disc,
       image=post.image,
       time=post.time,
       user_id=1
    )
    db.add(new_post)
    db.commit()
    return new_post