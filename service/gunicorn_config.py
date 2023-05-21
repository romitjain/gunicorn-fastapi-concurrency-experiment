import os
import logging
from dotenv import load_dotenv

from service.logger import logging_config

load_dotenv()

def set_logging_config():
    logging.config.dictConfig(logging_config)

def when_ready(server):
    """
    Called just after the server is started.
    The callable needs to accept a single instance variable for the Arbiter
    """
    # Set logger
    set_logging_config()

timeout = os.environ.get("timeout")
workers = os.environ.get("workers")
threads = 1