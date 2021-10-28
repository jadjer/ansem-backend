"""Update user model

Revision ID: 74b0946aaf25
Revises: c14c7f247b0d
Create Date: 2021-10-28 21:45:49.384008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74b0946aaf25'
down_revision = 'c14c7f247b0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('second_name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('country', sa.String(), nullable=True))
    op.add_column('users', sa.Column('city', sa.String(), nullable=True))
    op.add_column('users', sa.Column('address', sa.String(), nullable=True))
    op.add_column('users', sa.Column('mobile_no', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'mobile_no')
    op.drop_column('users', 'address')
    op.drop_column('users', 'city')
    op.drop_column('users', 'country')
    op.drop_column('users', 'second_name')
    # ### end Alembic commands ###
