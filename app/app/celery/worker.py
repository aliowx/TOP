import logging
import math 
import random
import rapidjson
import requests
from datetime import datetime, timedelta, UTC
from app.core.celery_app import celery_app
from sqlalchemy import text
from fastapi.encoders import jsonable_encoder
from app import crud, models, schemas
from app.core.celery_app import DatabaseTask, celery_app
from app.core.config import settings
from app.celery.celeryworker_pre_start import redis_client
 

@celery_app.task(name="app.celery.worker.test_celery")
def test_celery(word: str) -> str:
    return f"test task return {word}"


namespace = "job worker"
logger = logging.getLogger(__name__)

@celery_app.task(
    base=DatabaseTask,
    bind=True,
    acks_late=True,
    max_retries=4,
    soft_time_limit=240,
    time_limit=360,
    name='add event'  
)
def add_event(self, event: dict)->str:
    create_event = crud.airport.create(db=self.session, obj_in=event)
    