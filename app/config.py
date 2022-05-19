from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')
    SQL_ALCHEMY_DATABASE_URI = 'mysql+pymysql://root'

class DevelopmentConfig(Config):
    DEBUG = True

config={
    'development': DevelopmentConfiog
}
