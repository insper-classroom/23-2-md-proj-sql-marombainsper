import os

from fastapi import FastAPI
from .routes import register_routes

from .config import get_config

def create_app(config = "dev"):
    settings = get_config(config=config)

    app = FastAPI(title="Maromba Insper Microservice")

    register_routes(app)

    return app
  

