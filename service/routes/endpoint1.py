import time
import logging
from fastapi import APIRouter

from ..logger import APP_LOGGER_FORMAT

logger = logging.getLogger("app1")
endpoint1 = APIRouter()

@endpoint1.get("/e1/p1")
def path1():
    logger_format = APP_LOGGER_FORMAT.format(endpoint="endpoint1", path="path1")
    updated_output_format = logging.Formatter(logger_format)

    for child_logger in logger.handlers:
        child_logger.setFormatter(updated_output_format)

    start_time = time.time()
    logger.info(f"Started request at: {start_time} on endpoint endpoint1 on path: path1")

    wait_time = 10

    time.sleep(wait_time)

    processed_time = time.time()-start_time
    logger.info(f"Request completed in {processed_time} on path: path1")

    return processed_time

@endpoint1.get("/e1/p2")
async def path2():
    logger_format = APP_LOGGER_FORMAT.format(endpoint="endpoint1", path="path2")
    updated_output_format = logging.Formatter(logger_format)

    for child_logger in logger.handlers:
        child_logger.setFormatter(updated_output_format)

    start_time = time.time()
    logger.info(f"Started request at: {start_time} on endpoint endpoint1 on path: path2")

    wait_time = 1

    time.sleep(wait_time)

    processed_time = time.time()-start_time
    logger.info(f"Request completed in {processed_time} on path: path2")

    return processed_time