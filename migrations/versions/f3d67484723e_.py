"""empty message

Revision ID: f3d67484723e
Revises: 107f90c00078
Create Date: 2023-03-04 00:45:11.123129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3d67484723e'
down_revision = '107f90c00078'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.alter_column('planets_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.alter_column('planets_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
