import asyncio
from typing import Generator, AsyncGenerator

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from httpx import AsyncClient
from app.api.deps import get_db_async
from app.main import app
from app.db import Base


ASYNC_SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(
    ASYNC_SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)

async_session_local = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def override_get_db_async() -> AsyncGenerator:
    async with async_session_local() as db:
        yield db
        await db.commit()

app.dependency_overrides[get_db_async] = override_get_db_async


@pytest.fixture(scope="session")
def event_loop(request) -> Generator:  # noqa: indirect usage
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def db() -> AsyncSession:
    async_engine = engine
    async_session = async_session_local

    async with async_session() as session:
        async with async_engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
        yield session

    # async with async_engine.begin() as connection:
    #     await connection.run_sync(Base.metadata.drop_all)
    #     pass

    await async_engine.dispose()


@pytest_asyncio.fixture(scope="module")
async def client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
