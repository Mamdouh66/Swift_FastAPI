"""Add foreign-key to todos table

Revision ID: 12ab8443f573
Revises: ef7103875e7e
Create Date: 2023-10-15 00:18:10.381652

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "12ab8443f573"
down_revision: Union[str, None] = "ef7103875e7e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "todos",
        sa.Column("user_id", sa.Integer(), nullable=False),
    )
    op.create_foreign_key(
        constraint_name="fk_todos_user_id",
        source_table="todos",
        referent_table="users",
        local_cols=["user_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    op.drop_constraint("fk_todos_user_id", "todos")
    op.drop_column("todos", "user_id")
