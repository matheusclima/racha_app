from racha_app.repositories.repository import Repository
from racha_app.db import db
from racha_app.models.player import Player

class PlayerRepository(Repository):

    @staticmethod
    def select(name):
        return db.session.query(Player).filter_by(name = name).first()

    @staticmethod
    def select_all():
        return db.session.query(Player).order_by(Player.name).all()   
