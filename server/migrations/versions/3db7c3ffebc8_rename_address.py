"""rename address

Revision ID: 3db7c3ffebc8
Revises: 845510583a0a
Create Date: 2025-03-31 18:13:16.334829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3db7c3ffebc8'
down_revision = '845510583a0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###