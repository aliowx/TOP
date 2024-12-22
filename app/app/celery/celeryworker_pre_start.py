import logging
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed
from app.core.config import settings
from cache.redis import redis_connect_sync
import redis

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

redis_client = redis_connect_sync()

MAX_TRIES = 60 * 5  # 5 minutes
WAIT_SECONDS = 1

@retry(
    stop=stop_after_attempt(MAX_TRIES),
    wait=wait_fixed(WAIT_SECONDS),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        # Placeholder for actual initialization logic
        client = redis.from_url(
            str(settings.REDIS_URI))
        ping = client.ping()
        if not ping:
            raise Exception('there not be ping ')
        
    except Exception as e:
        logger.error('celery')
        logger.exception(e)
        logger.error(e)
        raise e

def main() -> None:
    logger.info("Initializing services")
    init()
    logger.info("Service finished initializing")

if __name__ == "__main__":
    main()
