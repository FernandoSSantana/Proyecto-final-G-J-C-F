"""empty message

Revision ID: 586579ec6bf0
Revises: bcc89321ee1d
Create Date: 2025-01-23 11:12:53.198146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '586579ec6bf0'
down_revision = 'bcc89321ee1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=500),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    # ### end Alembic commands ###
