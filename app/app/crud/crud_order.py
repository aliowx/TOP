from sqlalchemy.ext.asyncio import AsyncSession
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate
from app.crud.base import CRUDBase
from sqlalchemy.future import select


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):

    async def get_by_code(self, db: AsyncSession, code: str) -> Order:
        result = await db.execute(select(Order).where(Order.code == code))
        
        return result.scalars().first()
    
    async def create_order(
        self,
        db: AsyncSession,
        order_data: OrderCreate,
        user_id: int,
        ticket_id:int
    )-> Order:
        
        order = Order(**order_data.model_dump(), user_id=user_id, ticket_id=ticket_id)
        db.add(order)
        await db.commit()
        return order

order = CRUDOrder(Order)
