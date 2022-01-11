"""empty message

Revision ID: 940654ccccfd
Revises: 1be1990993ce
Create Date: 2022-01-11 21:44:55.646970

"""

# revision identifiers, used by Alembic.
revision = '940654ccccfd'
down_revision = '1be1990993ce'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))



def downgrade():
    op.drop_column('users', 'avatar_hash')
