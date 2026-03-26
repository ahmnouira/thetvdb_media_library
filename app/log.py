import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def log_error(error: str):
    logging.error(error)


def log_info(message: str):
    logging.info(message)
