"""Change columns of matches table

Revision ID: 302637e861de
Revises: 2ab8c4e6e489
Create Date: 2020-12-24 02:24:00.817287

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '302637e861de'
down_revision = '2ab8c4e6e489'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matches', sa.Column('away_goals', sa.Integer(), nullable=False))
    op.add_column('matches', sa.Column('away_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.add_column('matches', sa.Column('home_goals', sa.Integer(), nullable=False))
    op.add_column('matches', sa.Column('home_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.add_column('matches', sa.Column('tournament_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(None, 'matches', 'teams', ['home_id'], ['id'])
    op.create_foreign_key(None, 'matches', 'teams', ['away_id'], ['id'])
    op.create_foreign_key(None, 'matches', 'tournaments', ['tournament_id'], ['id'])
    op.drop_column('matches', 'goal_1')
    op.drop_column('matches', 'goal_2')
    op.drop_column('matches', 'team_2')
    op.drop_column('matches', 'day')
    op.drop_column('matches', 'team_1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matches', sa.Column('team_1', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.add_column('matches', sa.Column('day', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('matches', sa.Column('team_2', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.add_column('matches', sa.Column('goal_2', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('matches', sa.Column('goal_1', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'matches', type_='foreignkey')
    op.drop_constraint(None, 'matches', type_='foreignkey')
    op.drop_constraint(None, 'matches', type_='foreignkey')
    op.drop_column('matches', 'tournament_id')
    op.drop_column('matches', 'home_id')
    op.drop_column('matches', 'home_goals')
    op.drop_column('matches', 'away_id')
    op.drop_column('matches', 'away_goals')
    # ### end Alembic commands ###
