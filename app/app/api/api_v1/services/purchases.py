from sqlalchemy.ext.asyncio import AsyncSession
from app import exceptions as exc
from app.schemas.order import OrderCreate
from app.schemas.ticket import TicketCreate
from app.schemas.user import UserBase
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud


async def purchase_ticket(
    db: AsyncSession,
    user: UserBase, 
    ticket_id: TicketCreate, 
    order_data: OrderCreate
)-> None:
    
    ticket = await crud.ticket.get_by_id(db=db, ticket_id=ticket_id)
    
    # if not ticket:
    #     raise exc.NotFoundException(
    #         detail=" There isn't any ticket here!"
    #     )
        
    order = await crud.order.create_order(
        db=db,
        order_data=order_data,
        user_id=user.id,  
        ticket_id=ticket.id 
    )
    
    return order