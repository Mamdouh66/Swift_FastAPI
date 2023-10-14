"""Add phonenumber to users table

Revision ID: 2992ddf0f2a9
Revises: 12ab8443f573
Create Date: 2023-10-15 00:20:39.961790

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2992ddf0f2a9"
down_revision: Union[str, None] = "12ab8443f573"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users", sa.Column("phone_number", sa.String(), nullable=False, unique=True)
    )


def downgrade() -> None:
    op.drop_column("users", "phone_number")
