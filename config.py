import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://username:password@localhost:5432/payroll_db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     DEBUG = True

class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #os.environ.get('SECRET_KEY') or 
    # os.environ.get('DATABASE_URL') or 