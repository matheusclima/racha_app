from racha_app.repositories.repository import Repository
from racha_app.db import db
from racha_app.models.tournament import Tournament

class TournamentRepository(Repository):

    @staticmethod
    def select(id):
        return db.session.query(Tournament).filter_by(id = id).first()   

