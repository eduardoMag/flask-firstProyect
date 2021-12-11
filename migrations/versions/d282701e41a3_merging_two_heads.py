"""merging two heads

Revision ID: d282701e41a3
Revises: 9ae85934f02a, 9ce26cf9a717
Create Date: 2021-12-06 14:26:26.202520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd282701e41a3'
down_revision = ('9ae85934f02a', '9ce26cf9a717')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
