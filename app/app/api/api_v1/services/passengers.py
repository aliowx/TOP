from sqlalchemy.ext.asyncio import AsyncSession
from app import crud
from app import exceptions as exc
from app import models, schemas


async def read_passengers(
        db: AsyncSession,
        user_in: int
        
)-> schemas.passenger:
    passenger = await crud.pasenger.get_passenger(db=db, user_id=user_in)


    if not passenger:
        raise exc.NotFoundException(
            detail="no historical passenger here!"
        )
    
    return passenger


async def create_passenger(
        db: AsyncSession,
        user_id: int,
        name: str,
        age: int,
        nationa_id: int
        
)-> schemas.passenger:
    new_passenger = await crud.pasenger.insert_passenger(
        user_id=user_id,
        name=name,
        age=age,
        nationa_id=nationa_id
    )

    if user_id and nationa_id == None:
        raise exc.ValidationException(
            detail = "there is validation erro try agin"
        )
    # if user_id :
    #     raise exc.AlreadyExistException(
    #         detail='this passenger is already exist'
    #     )

