import os
from typing import List, Type

from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()

user_db = os.getenv("USER_DB")
password_db = os.getenv("PASSWORD_DB")
host_db = os.getenv("DB_HOST")
port_db = os.getenv("DB_PORT")
name_db = os.getenv("DB_NAME")

basedir = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):
    CONFIG_NAME: str = "base"
    USE_MOCK_EQUIVALENCY: bool = False
    DEBUG: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


class DevelopmentConfig(Settings):
    CONFIG_NAME: str = "dev"
    SECRET_KEY: str = os.getenv(
        "DEV_SECRET_KEY", "You can't see California without Marlon Widgeto's eyes"
    )
    DEBUG: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    TESTING: bool = False
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///{0}/app-dev.db".format(basedir)


class TestingConfig(Settings):
    CONFIG_NAME: str = "test"
    SECRET_KEY: str = os.getenv("TEST_SECRET_KEY", "Thanos did nothing wrong")
    DEBUG: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URL: str = f"mysql+mysqlconnector://{user_db}:{password_db}@{host_db}:{port_db}/{name_db}"


class ProductionConfig(Settings):
    CONFIG_NAME: str = "prod"
    SECRET_KEY: str = os.getenv("PROD_SECRET_KEY", "I'm Ron Burgundy?")
    DEBUG: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    TESTING: bool = False
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///{0}/app-prod.db".format(basedir)


def get_config(config):
    return config_by_name[config]


EXPORT_CONFIGS: List[Type[Settings]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]
config_by_name = {cfg().CONFIG_NAME: cfg() for cfg in EXPORT_CONFIGS}