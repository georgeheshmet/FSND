"""empty message

Revision ID: 9fd376e043f3
Revises: 094894932bae
Create Date: 2020-08-17 00:35:51.120485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fd376e043f3'
down_revision = '094894932bae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shows')
    # ### end Alembic commands ###
