"""Create users table

Revision ID: c6c8a0ee90b1
Revises: 
Create Date: 2025-07-30 11:36:19.312493

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6c8a0ee90b1'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, unique=True),
        sa.Column('email', sa.String, unique=True),
        sa.Column('full_name', sa.String, nullable=True),
        sa.Column('hashed_password', sa.String, nullable=False)
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
