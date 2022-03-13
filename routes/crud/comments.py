
from sqlalchemy.orm import session
from models import comments as m_comments
from schemas import comments as s_comments
from models import likes as m_likes
from schemas import likes as s_likes
from models import posts as m_posts
from schemas import posts as s_posts
from schemas import users as s_users

def create_comment(post_id:int,comment:s_comments.Comments, current_user:s_users.Users,db:session):
    new_comment = m_comments.Comments(
       disc=comment.disc,
       time=comment.time,
       user_id = 1,
       post_id=post_id
    )
    db.add(new_comment)
    db.commit()
    return current_user