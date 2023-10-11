"""Create phone_number column in users tabele

Revision ID: 55711d4f78cf
Revises: 
Create Date: 2023-10-12 00:17:01.092395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "55711d4f78cf"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users", sa.Column("phone_number", sa.String(), nullable=False, unique=True)
    )


def downgrade() -> None:
    op.drop_column("users", "phone_number")
