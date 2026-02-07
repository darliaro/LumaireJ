from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from sqlalchemy.exc import OperationalError
from sqlmodel import SQLModel

import app.models  # noqa: F401
from alembic import context
from app.core.config import settings

target_metadata = SQLModel.metadata

# Access Alembic configuration
config = context.config

# Use centralized config instead of manual os.getenv
database_url = settings.database_url
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
        compare_type=True,
        compare_server_default=True,
        render_as_batch=True,
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
    try:
        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=target_metadata,
                compare_type=True,
                compare_server_default=True,
                render_as_batch=True,
            )
            with context.begin_transaction():
                context.run_migrations()
    except OperationalError as exc:
        raise RuntimeError(
            f"Cannot connect to database. Check DATABASE_URL: {type(exc).__name__}"
        ) from exc


# Choose offline or online based on execution context
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
