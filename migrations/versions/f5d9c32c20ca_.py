"""empty message

Revision ID: f5d9c32c20ca
Revises: 5418dabfc62e
Create Date: 2021-01-11 21:29:10.964861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5d9c32c20ca'
down_revision = '5418dabfc62e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inverter_price',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=10), nullable=False),
    sa.Column('brand', sa.String(length=100), nullable=False),
    sa.Column('power', sa.Integer(), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inverter_price')
    # ### end Alembic commands ###
