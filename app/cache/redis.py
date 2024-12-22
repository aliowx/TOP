"""redis.py"""
import os
from typing import Tuple

import redis.asyncio as redis
from redis.asyncio import client
from redis import asyncio
from cache.enums import RedisStatus
from app.core.config import settings

async def redis_connect(host_url: str) -> Tuple[RedisStatus, client.Redis]:
    """Attempt to connect to `host_url` and return a Redis client instance if successful."""
    return (
        await _connect(host_url)
        if os.environ.get("CACHE_ENV") != "TEST"
        else _connect_fake()
    )
    
    
# for we
async def redis_connect_async(timeout: int = None)-> asyncio.Redis:
    client = asyncio.from_url(
        str(settings.REDIS_URI),
        timeout=timeout,
        decode_responses=True
    )
    return client 




async def _connect(
    host_url: str,
) -> tuple[RedisStatus, client.Redis]:  # pragma: no cover
    try:
        redis_client = await redis.from_url(host_url)
        if await redis_client.ping():
            return (RedisStatus.CONNECTED, redis_client)
        return (RedisStatus.CONN_ERROR, None)
    except redis.AuthenticationError:
        return (RedisStatus.AUTH_ERROR, None)
    except redis.ConnectionError:
        return (RedisStatus.CONN_ERROR, None)

def redis_connect_sync() -> client.Redis:
    client = redis.from_url(
        str(settings.REDIS_URI)
    )
    return client

redis_client = redis_connect_sync()


def _connect_fake() -> Tuple[RedisStatus, client.Redis]:
    from fakeredis import FakeRedis

    return (RedisStatus.CONNECTED, FakeRedis())
