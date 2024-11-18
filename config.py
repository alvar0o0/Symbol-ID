import os

class Config:
    # Configuración básica
    SECRET_KEY = 'dev'  # En producción usaríamos algo más seguro
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'symbols.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True