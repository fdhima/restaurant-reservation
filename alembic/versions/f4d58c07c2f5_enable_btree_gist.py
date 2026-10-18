"""enable btree_gist

Revision ID: f4d58c07c2f5
Revises: 
Create Date: 2026-10-18 22:21:36.188967

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4d58c07c2f5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS btree_gist")


def downgrade() -> None:
    op.execute("DROP EXTENSION IF EXISTS btree_gist")