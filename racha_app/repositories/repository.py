# from flask import session
from racha_app.db import db

class Repository:
    
    @staticmethod
    def add(entity):
        db.session.add(entity)
        db.session.commit()

    @staticmethod
    def delete(entity):
        db.session.delete(entity)
        db.session.commit()

