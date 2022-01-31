"""empty message

Revision ID: 1efa5ea4b611
Revises: 83a3094f9569
Create Date: 2022-01-28 22:56:43.552875

"""

# revision identifiers, used by Alembic.
revision = '1efa5ea4b611'
down_revision = '83a3094f9569'

from alembic import op
import sqlalchemy as sa


def upgrade():
     op.add_column('posts', sa.Column('body_html', sa.Text, nullable=True)),



def downgrade():
     op.drop_column('posts', 'body_html')