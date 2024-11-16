from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.crud.base import CRUDBase
from app.models.ticket import Ticket # type: ignore
from app.schemas.ticket import TicketCreate, TicketUpdate


class CRUDTicket(CRUDBase[TicketCreate, TicketUpdate]):

    async def get_by_id(db: AsyncSession, ticket_id: int) -> Ticket:
        result = await db.execute(select(Ticket).where(Ticket.id == ticket_id))
        return result.scalars().first()


    async def create_ticket(db: AsyncSession, ticket_data: TicketCreate) -> Ticket:
        ticket = Ticket(**ticket_data.model_dump()) 
        db.add(ticket)
        await db.commit()
        return ticket



ticket = CRUDTicket(Ticket)