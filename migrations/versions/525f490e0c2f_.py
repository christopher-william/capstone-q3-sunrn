"""merge heads of migrations

Revision ID: 525f490e0c2f
Revises: e3354e0b85da, 1af8bccf51a7, ef59e7628463, a988a4642147
Create Date: 2021-01-20 09:03:48.504989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '525f490e0c2f'
down_revision = ('e3354e0b85da', '1af8bccf51a7', 'ef59e7628463', 'a988a4642147')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
