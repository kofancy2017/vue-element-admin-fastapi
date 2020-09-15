"""

Revision ID: 2bff36d80223
Revises: 766f4180ceb7
Create Date: 2020-07-23 14:05:10.546110

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2bff36d80223'
down_revision = '766f4180ceb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'avatar',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('user', 'introduction',
               existing_type=mysql.VARCHAR(length=256),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'introduction',
               existing_type=mysql.VARCHAR(length=256),
               nullable=False)
    op.alter_column('user', 'avatar',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    # ### end Alembic commands ###
