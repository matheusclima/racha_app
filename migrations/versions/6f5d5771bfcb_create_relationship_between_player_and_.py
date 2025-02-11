"""Create relationship between player and goal

Revision ID: 6f5d5771bfcb
Revises: 01c8ce3d373c
Create Date: 2020-11-25 14:02:11.855117

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6f5d5771bfcb'
down_revision = '01c8ce3d373c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goals', sa.Column('scorer_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(None, 'goals', 'players', ['scorer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'goals', type_='foreignkey')
    op.drop_column('goals', 'scorer_id')
    # ### end Alembic commands ###
