import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # 👈 prints to terminal
        logging.FileHandler("app.log"),  # 👈 saves to file
    ],
)

logger = logging.getLogger(__name__)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # more precise than time.time()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        logger.info(f"{func.__name__}() took {end - start:.4f} seconds")
        return result

    return wrapper
