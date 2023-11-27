from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from httpx import AsyncClient

from app import crud
from app.core.config import settings
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from tests.utils.utils import random_email, random_lower_string


async def user_authentication_headers(
    client: AsyncClient, email: str, password: str
) -> Dict[str, str]:
    payload = {"username": email, "password": password}

    response = await client.post(f"{settings.API_V1_STR}/users/login/access-token", data=payload)
    tokens = response.json()
    auth_token = tokens.get("access_token", None)
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


async def create_random_user(db: AsyncSession) -> User:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(username=email, email=email, password=password)
    user = await crud.user.create(db=db, obj_in=user_in)
    return user


async def authentication_token_from_email(
    client: AsyncClient, email: str, db: AsyncSession
) -> dict[str, str]:
    """
    Return a valid token for the user with given email.
    If the user doesn't exist it is created first.
    """
    password = random_lower_string()
    user = await crud.user.get_by_email(db, email=email)
    if not user:
        user_in_create = UserCreate(username=email, email=email, password=password)
        await crud.user.create(db, obj_in=user_in_create)
    else:
        user_in_update = UserUpdate(password=password)
        await crud.user.update(db, db_obj=user, obj_in=user_in_update)

    return await user_authentication_headers(
        client=client, email=email, password=password
    )
