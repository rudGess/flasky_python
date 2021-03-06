"""empty message

Revision ID: 75d124ba9ab0
Revises: 190163627111
Create Date: 2021-12-14 15:30:58.048497

"""

# revision identifiers, used by Alembic.
revision = '75d124ba9ab0'
down_revision = '190163627111'

from alembic import op
import sqlalchemy as sa
from datetime import datetime



def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(),  default = False, index = True))
    op.add_column('roles', sa.Column('permissions', sa.DateTime(), default=datetime.utcnow))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'default')
    op.drop_column('roles', 'permission')
    ### end Alembic commands ###
