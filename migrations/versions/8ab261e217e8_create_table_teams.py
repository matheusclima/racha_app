"""Create table teams

Revision ID: 8ab261e217e8
Revises: 265544c44426
Create Date: 2020-11-20 02:12:00.109579

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8ab261e217e8'
down_revision = '265544c44426'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teams',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('players', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('letter', sa.String(length=255), nullable=True),
    sa.Column('day', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teams')
    # ### end Alembic commands ###
