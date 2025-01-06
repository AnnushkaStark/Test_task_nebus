from typing import AsyncGenerator

from sqlalchemy import Integer
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql.sqltypes import ARRAY, String

from config.configs import db_settings

SQLALCHEMY_DATABASE_URL = (
    "postgresql+asyncpg://"
    f"{db_settings.POSTGRES_USER}:"
    f"{db_settings.POSTGRES_PASSWORD}@"
    f"{db_settings.POSTGRES_HOST}:"
    f"{db_settings.POSTGRES_PORT}/"
    f"{db_settings.POSTGRES_DB}"
)


async_engine = create_async_engine(
    url=SQLALCHEMY_DATABASE_URL, pool_size=100, max_overflow=20, echo=True
)

async_session = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    type_annotation_map = {
        list: ARRAY,
        list[str]: ARRAY(String),
        list[int]: ARRAY(Integer),
    }


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
