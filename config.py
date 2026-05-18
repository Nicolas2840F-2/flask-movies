# config.py
import os
from pathlib import Path
from dotenv import load_dotenv

basedir = Path(__file__).resolve().parent
load_dotenv(dotenv_path=basedir / '.env')

class Config:
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3306/ProyectoPY'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:1234@localhost:3306/ProyectoPY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
