from flask import request, redirect, render_template, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import app, lm
from ..models.user import User
from ..models.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = app.config['USERS_COLLECTION'].find_one(
            {'_id': form.username.data})
        if user and User.validate_login(user.get('password'), form.password.data.encode('utf-8')):
            userObj = User(user.get('_id'))
            login_user(userObj)
            flash("Logged in successfully!", category='success')
            return redirect(request.args.get('next') or url_for('write'))
        flash("Wrong username or password!", category='error')

    return render_template('login.html', title='login', form=form)
