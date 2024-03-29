"""add location_column_to_packages_table

Revision ID: 1a78fdd41d93
Revises: 0ff0db171a89
Create Date: 2024-02-08 12:44:09.643188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a78fdd41d93'
down_revision = '0ff0db171a89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(length=20), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.drop_column('location')

    # ### end Alembic commands ###
