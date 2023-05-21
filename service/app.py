"""
Fast API app
"""

import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

from .routes import routers

load_dotenv()

def create_app() -> FastAPI:
    """Create a new Fastapi app instance with routes and factory configs registered
    Example::
        >>> from onboarding_risk_detection.factory import create_app
        >>> app = create_app()
    Args:
        None
    Returns:
        Flask app instance
    """
    # Instantiate FastAPI
    app = FastAPI()

    for route in routers:
        app.include_router(route)

    return app

app = create_app()

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8888"))
    uvicorn.run(app, host=host, port=port, workers=1)
