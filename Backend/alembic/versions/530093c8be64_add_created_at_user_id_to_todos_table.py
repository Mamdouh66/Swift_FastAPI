"""Add created_at, user_id to todos table

Revision ID: 530093c8be64
Revises: b76c76f71577
Create Date: 2023-10-15 00:08:17.721411

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "530093c8be64"
down_revision: Union[str, None] = "b76c76f71577"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "todos",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )


def downgrade() -> None:
    op.drop_column("todos", "created_at")
