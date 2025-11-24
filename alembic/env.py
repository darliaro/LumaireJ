import os
from logging.config import fileConfig

from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool
from sqlmodel import SQLModel

import app.models  # noqa: F401
from alembic import context

target_metadata = SQLModel.metadata

load_dotenv()

# Access Alembic configuration
config = context.config

# Get database URL from environment (prefer `database_url`, fallback to legacy `DATABASE_URL`)
database_url = os.getenv("database_url") or os.getenv("DATABASE_URL")  # noqa: SIM112
if not database_url:
    raise RuntimeError(
        "Set the database_url (or DATABASE_URL) environment variable before running Alembic"
    )
# set the SQLAlchemy URL in Alembic config
config.set_main_option("sqlalchemy.url", database_url)

# Configure Python logging based on the ini file
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


def run_migrations_offline() -> None:
    """Run migrations without an active DB connection"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations against the database engine"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    # Connect and run migrations
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


# Choose offline or online based on execution context
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
