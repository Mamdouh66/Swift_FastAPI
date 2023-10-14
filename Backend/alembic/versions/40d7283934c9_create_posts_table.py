"""create todos table

Revision ID: 40d7283934c9
Revises: 
Create Date: 2023-10-14 23:57:17.658528

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "40d7283934c9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "todos",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("title", sa.String(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("todos")
