from . import home
from . import login
from . import logout
from . import write
from app import app, lm
from ..models.user import User


@lm.user_loader
def load_user(username):
    u = app.config['USERS_COLLECTION'].find_one({'_id': username})
    if not u:
        return None
    return User(u.get('_id'))
