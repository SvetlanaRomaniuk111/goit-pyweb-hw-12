import configparser
import os
from dotenv import load_dotenv


class Config:
    # Завантаження змінних з файлу .env
    load_dotenv()

    config = configparser.ConfigParser()
    config.read('config.ini')

    DB_URL = config['database']['DB_URL']
    SECRET_KEY = os.getenv('SECRET_KEY')


config = Config()
