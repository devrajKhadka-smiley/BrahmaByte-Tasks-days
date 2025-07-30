"""Create users table again

Revision ID: 6fb048c3897f
Revises: c6c8a0ee90b1
Create Date: 2025-07-30 14:16:15.797800

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fb048c3897f'
down_revision: Union[str, Sequence[str], None] = 'c6c8a0ee90b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, unique=True),
        sa.Column('email', sa.String, unique=True),
        sa.Column('hashed_password', sa.String, nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')