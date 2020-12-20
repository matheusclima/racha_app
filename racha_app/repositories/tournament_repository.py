from racha_app.repositories.repository import Repository
from racha_app.db import db

class TournamentRepository(Repository):

    def get_date(self, id):
        return db.session.query(self).filter_by(id = id).first().date   

