"""Make key fields as unique

Revision ID: 041be2d1a8fb
Revises: c62b363236c7
Create Date: 2021-10-27 14:16:39.523507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '041be2d1a8fb'
down_revision = 'c62b363236c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'keys', ['description'])
    op.create_unique_constraint(None, 'keys', ['key'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'keys', type_='unique')
    op.drop_constraint(None, 'keys', type_='unique')
    # ### end Alembic commands ###
