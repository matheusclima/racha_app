from racha_app.repositories.repository import Repository
from racha_app.db import db
from racha_app.models.team import Team

class TeamRepository(Repository):

    @staticmethod
    def select_all(tournament_id):
        return db.session.query(Team).filter_by(tournament_id = tournament_id).all()