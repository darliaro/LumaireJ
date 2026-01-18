"""Add updated_at to journal_entries

Revision ID: 62a1b2c3d4e5
Revises: 419a7670b421
Create Date: 2026-01-19

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "62a1b2c3d4e5"
down_revision: str | Sequence[str] | None = "419a7670b421"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Add updated_at column to journal_entries."""
    op.add_column(
        "journal_entries",
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    """Remove updated_at column from journal_entries."""
    op.drop_column("journal_entries", "updated_at")
