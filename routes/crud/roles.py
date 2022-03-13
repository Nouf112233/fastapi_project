from sqlalchemy.orm import session
from models import roles as modelRoles
from schemas import roles as schemaRoles
import models
# import schemas.roles
# import models.roles


def create_role(rolee: schemaRoles.Roles,db:session):
    new_role = modelRoles.Roles(
        role=rolee.role,
    )
    db.add(new_role)
    db.commit()
    return new_role
