import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY")


PROJECT_NAME = "Media Soft"

dotenv_path = Path(f"{BASE_DIR}/.env")
load_dotenv(dotenv_path=dotenv_path)

SQL_ENGINE = os.environ.get("SQL_ENGINE")
SQL_USER = os.environ.get("SQL_USER")
SQL_PASSWORD = os.environ.get("SQL_PASSWORD")
SQL_HOST = os.environ.get("SQL_HOST")
SQL_PORT = os.environ.get("SQL_PORT")
SQL_DATABASE = os.environ.get("SQL_DATABASE")