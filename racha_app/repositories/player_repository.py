from racha_app.repositories.repository import Repository
from racha_app.db import db

class PlayerRepository(Repository):

    def select(self, name):
        return db.session.query(self).filter_by(name = name).first()
        
