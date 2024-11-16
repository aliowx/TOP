from sqlalchemy.ext.asyncio import AsyncSession
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate
from app.crud.base import CRUDBase


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):
    def get_by_code(self, db: AsyncSession, code: int) -> Order:
        return db.query(Order).filter(Order.code == code).first()

    def get_orders_by_price(self, db: AsyncSession, min_price: float, max_price: float):
        return db.query(Order).filter(Order.price >= min_price, Order.price <= max_price).all()


order = CRUDOrder(Order)
