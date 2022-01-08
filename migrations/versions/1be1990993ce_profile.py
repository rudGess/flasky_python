"""Profile

Revision ID: 1be1990993ce
Revises: f3acab076e01
Create Date: 2021-12-27 22:52:47.854306

"""

# revision identifiers, used by Alembic.
revision = '1be1990993ce'
down_revision = 'f3acab076e01'

from alembic import op
import sqlalchemy as sa
from datetime import datetime


def upgrade():
   op.add_column('users', sa.Column('name', sa.String(64)))
   op.add_column('users', sa.Column('location', sa.String(64)))
   op.add_column('users', sa.Column('about_me', sa.Text()))
   op.add_column('users', sa.Column('member_since', sa.DateTime(),default=datetime.utcnow))
   op.add_column('users', sa.Column('last_seen', sa.Text()))


def downgrade():
   op.drop_column('users', 'name')
   op.drop_column('users', 'location')
   op.drop_column('users', 'about_me')
   op.drop_column('users', 'member_since')
   op.drop_column('users', 'last_seen')
    # ### end Alembic commands ###
