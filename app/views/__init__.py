from flask import Flask
from flask_login import LoginManager
from flask_sslify import SSLify
from . import home, auth, write
from ..models.user import User

application = Flask(__name__, template_folder='../templates')
application.config.from_object('config')
SSLify(application)
lm = LoginManager()
lm.init_app(application)
lm.login_view = '/login'


@lm.user_loader
def load_user(username):
    u = application.config['USERS_COLLECTION'].find_one({'_id': username})
    if not u:
        return None
    return User(u.get('_id'))


modules_define = [home.app, auth.app, write.app]

for app in modules_define:
    application.register_blueprint(app)
