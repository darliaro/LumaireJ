"""add_mood_length_constraint

Revision ID: cc53177b8919
Revises: 62a1b2c3d4e5
Create Date: 2026-02-07 17:21:34.127825

"""
from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc53177b8919'
down_revision: str | Sequence[str] | None = '62a1b2c3d4e5'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add length constraint to mood column (PostgreSQL only; SQLite doesn't enforce VARCHAR length)
    with op.batch_alter_table('journal_entries', schema=None) as batch_op:
        batch_op.alter_column(
            'mood',
            existing_type=sa.String(),
            type_=sa.String(length=50),
            existing_nullable=True
        )


def downgrade() -> None:
    """Downgrade schema."""
    # Remove length constraint from mood column
    with op.batch_alter_table('journal_entries', schema=None) as batch_op:
        batch_op.alter_column(
            'mood',
            existing_type=sa.String(length=50),
            type_=sa.String(),
            existing_nullable=True
        )
