from flask import render_template
from flask_login import login_user, logout_user, login_required, current_user
from app import app


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')
