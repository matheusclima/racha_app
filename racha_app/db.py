import uuid

from sqlalchemy.dialects.postgresql import UUID
from racha_app.models.player import Player
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Float, Integer, String, ARRAY
from sqlalchemy.orm import relationship
from racha_app.models.user import User
from racha_app.models.goal import Goal
from racha_app.models.team import Team
from racha_app.models.match import Match
from racha_app.models.tournament import Tournament

db = SQLAlchemy()

users_mapping = db.Table(
    'users',
    db.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    db.Column('username', db.String(255)),
    db.Column('password', db.String(255)),
)

tournament_mapping = db.Table(
    'tournaments',
    db.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    db.Column('date', db.Date)
)

teams_mapping = db.Table(
    'teams',
    db.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    db.Column('points', db.Integer),
    db.Column('letter', db.String(255)),
    db.Column('tournament_id', UUID(as_uuid=True), db.ForeignKey('tournaments.id'))
)

players_mapping = db.Table(
    'players',
    db.Column('id', UUID(as_uuid = True), primary_key=True, default=uuid.uuid4, nullable=False),
    db.Column('name', db.String(255)),
)

team_player_relationship = db.Table(
    'team_player',
    db.Column('team_id', UUID(as_uuid=True), db.ForeignKey('teams.id')),
    db.Column('player_id', UUID(as_uuid=True), db.ForeignKey('players.id'))
)

match_mapping = db.Table(
    'matches',
    db.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    db.Column('home_id', UUID(as_uuid=True), db.ForeignKey('teams.id')),
    db.Column('away_id', UUID(as_uuid=True), db.ForeignKey('teams.id')),
    db.Column('home_goals', db.Integer, nullable = False),
    db.Column('away_goals', db.Integer, nullable = False),
    db.Column('tournament_id', UUID(as_uuid=True), db.ForeignKey('tournaments.id'))
)

goals_mapping = db.Table(
    'goals',
    db.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    db.Column('day', db.Date),
    db.Column('player_id', UUID(as_uuid=True), db.ForeignKey('players.id')),
)

db.mapper(Player, players_mapping)

db.mapper(User, users_mapping)

db.mapper(Goal, goals_mapping, properties={
    'player' : relationship(Player, backref = 'scorer')
})

db.mapper(Team, teams_mapping, properties={
    'players' : relationship(Player, secondary = team_player_relationship)
})

db.mapper(Match, match_mapping, properties={
    'home': relationship(Team, foreign_keys = match_mapping.c.home_id),
    'away': relationship(Team, foreign_keys = match_mapping.c.away_id)  
})
db.mapper(Tournament, tournament_mapping, properties={
    'teams': relationship(Team, backref = 'teams')
})

# users_mapping = db.Table(
#     'users',
#     db.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
#     db.Column('name', db.String(50)),
#     db.Column('username', db.String(50)),
#     db.Column('password', db.String(128))
# )

# db.mapper(User, users_mapping)