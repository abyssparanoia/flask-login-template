from flask import render_template, Blueprint, current_app
from flask_login import login_user, login_required, current_user

app = Blueprint('write', __name__)


@app.route('/write', methods=['GET', 'POST'])
@login_required
def write():
    company = current_app.config['USERS_COLLECTION'].find_one({
        '_id':
        current_user.username
    }).get('company')
    return render_template('write.html', company=company)
