"""Add description, and done status to todos table

Revision ID: b76c76f71577
Revises: 40d7283934c9
Create Date: 2023-10-15 00:06:00.612868

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b76c76f71577"
down_revision: Union[str, None] = "40d7283934c9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "todos",
        sa.Column("description", sa.String(), nullable=False, server_default=""),
    )
    op.add_column(
        "todos", sa.Column("done", sa.Boolean(), nullable=False, server_default="FALSE")
    )


def downgrade() -> None:
    op.drop_column("todos", "description")
    op.drop_column("todos", "done")
