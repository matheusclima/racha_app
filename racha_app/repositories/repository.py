# from flask import session
from racha_app.db import db

class Repository:
    
    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def select_all(self):
        return db.session.query(self).order_by(self.name).all()

