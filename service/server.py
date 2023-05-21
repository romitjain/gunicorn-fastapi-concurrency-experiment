"""
Gunicorn server execution
"""

import os
import shlex
import subprocess
from dotenv import load_dotenv

here = os.path.dirname(os.path.realpath(__file__))
config = os.path.join(here, "gunicorn_config.py")

load_dotenv()

# Runs Gunicorn server with app_module define
def execute():
    """
    Starts the gunicorn server
    """

    address = f"{os.getenv('HOST')}:{os.getenv('PORT')}"

    # Define gunicorn execution with arguments
    cmd = f"gunicorn -b {address} -c {config} --worker-class uvicorn.workers.UvicornWorker service.app:app --threads 1"

    subprocess.run(shlex.split(cmd))

if __name__ == "__main__":
    execute()
