from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context
from config.configs import db_settings
from databases.database import Base
from models import *  # noqa: F403 F401

config = context.config

fileConfig(config.config_file_name)

target_metadata = Base.metadata


def get_url() -> str:
    postgres_server = db_settings.POSTGRES_HOST
    postgres_user = db_settings.POSTGRES_USER
    postgres_password = db_settings.POSTGRES_PASSWORD
    postgres_db = db_settings.POSTGRES_DB
    postgres_port = db_settings.POSTGRES_PORT
    return f"postgresql://{postgres_user}:{postgres_password}@{postgres_server}:{postgres_port}/{postgres_db}"  # noqa: E501


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    # url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=get_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)

    configuration["sqlalchemy.url"] = get_url()

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
