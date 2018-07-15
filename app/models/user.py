from werkzeug.security import check_password_hash
import hashlib


class User():

    def __init__(self, username):
        self.username = username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        hashedPassword = hashlib.sha256(password).hexdigest()
        if hashedPassword == password_hash:
            return True
        return False
