from flask import render_template, Blueprint
from flask_login import login_user, logout_user, login_required, current_user

app = Blueprint('home', __name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')
