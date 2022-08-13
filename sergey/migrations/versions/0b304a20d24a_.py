"""empty message

Revision ID: 0b304a20d24a
Revises: 
Create Date: 2022-07-30 11:57:43.445084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b304a20d24a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_submit_email', table_name='user_submit')
    op.create_index(op.f('ix_user_submit_email'), 'user_submit', ['email'], unique=False)
    op.drop_index('ix_user_submit_name', table_name='user_submit')
    op.create_index(op.f('ix_user_submit_name'), 'user_submit', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_submit_name'), table_name='user_submit')
    op.create_index('ix_user_submit_name', 'user_submit', ['name'], unique=False)
    op.drop_index(op.f('ix_user_submit_email'), table_name='user_submit')
    op.create_index('ix_user_submit_email', 'user_submit', ['email'], unique=False)
    # ### end Alembic commands ###