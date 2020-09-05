"""empty message

Revision ID: faef9a1fd6e5
Revises: ea7253eab716
Create Date: 2020-08-31 21:07:57.319079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'faef9a1fd6e5'
down_revision = 'ea7253eab716'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('category', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questions', 'category')
    # ### end Alembic commands ###