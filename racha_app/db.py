import uuid

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from racha_app.models.jogador import Jogador

db = SQLAlchemy()

jogadores_mapping = db.Table(
    'jogadores',
    db.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    db.Column('nome', db.String(255)),
    # db.Column(
    #     'user_id',
    #     UUID(as_uuid=True),
    #     db.ForeignKey('users.id'),
    #     nullable=False
    # ),
)

db.mapper(Jogador, jogadores_mapping)

# users_mapping = db.Table(
#     'users',
#     db.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
#     db.Column('name', db.String(50)),
#     db.Column('username', db.String(50)),
#     db.Column('password', db.String(128))
# )

# db.mapper(User, users_mapping)