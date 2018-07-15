from flask import render_template
from flask_login import login_user, login_required, current_user
from app import app


@app.route('/write', methods=['GET', 'POST'])
@login_required
def write():
    company = app.config['USERS_COLLECTION'].find_one(
        {'_id': current_user.username}).get('company')
    return render_template('write.html', company=company)
