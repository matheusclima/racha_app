from racha_app.db import db
from racha_app.models.user import User

class UserRepository:
    def find_by_username(self, username):
        return db.session.query(User).filter_by(username = username).first()