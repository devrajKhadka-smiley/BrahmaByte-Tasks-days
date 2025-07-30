"""drop users table

Revision ID: f71448a03319
Revises: 6fb048c3897f
Create Date: 2025-07-30 14:22:27.781538

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f71448a03319"
down_revision: Union[str, Sequence[str], None] = "6fb048c3897f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("users")


def downgrade() -> None:
    op.create_table(
        "users",
        op.Column("id", sa.Integer, primary_key=True),
        op.Column("name", sa.String, unique=True),
        op.Column("email", sa.String, unique=True),
        op.Column("hashed_password", sa.String, nullable=False),
    )
