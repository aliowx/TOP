from celery import Celery, Task
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from celery.signals import worker_init
from app.core.config import settings

BROKER_URL = str(settings.REDIS_URI)


celery_app = Celery(
    "worker", backend="rpc://", broker=BROKER_URL, include=["celery.worker"]
)


ScopedSession = None

@worker_init.connect
def bootstrap(
    *args,
    **kwargs
) -> None:
    global ScopedSessio
    engine = create_engine(
        str(settings.POSTGRES_ASYNC_URI), pool_pre_ping=True
    )
    SessionLocal = sessionmaker()
    ScopedSession = scoped_session(SessionLocal)
    
    
    
class DatabaseTask(Task):
    abstract = True
      
    _session = None
    
    
    
    def after_return(
        self,
        *args,
        **kwargs
    ):
        if self._session is not None:
            self._session.remove()
        
    @property
    def session(self):
        if self._session is None:
            self._session = ScopedSession 
            
        return self._session
    
celery_app.conf.update(task_track_started=True, broker_connection_retry_on_startup=True)