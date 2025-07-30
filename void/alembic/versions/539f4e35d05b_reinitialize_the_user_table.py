"""reinitialize the user table

Revision ID: 539f4e35d05b
Revises: f71448a03319
Create Date: 2025-07-30 14:24:49.208931

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '539f4e35d05b'
down_revision: Union[str, Sequence[str], None] = 'f71448a03319'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, unique=True),
        sa.Column('email', sa.String, unique=True),
        sa.Column('hashed_password', sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users')