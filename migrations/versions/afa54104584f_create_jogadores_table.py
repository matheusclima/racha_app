"""create jogadores table

Revision ID: afa54104584f
Revises: 
Create Date: 2020-11-01 20:33:21.491266

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'afa54104584f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jogadores',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jogadores')
    # ### end Alembic commands ###
