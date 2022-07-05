from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY=os.getenv('SECRET_KEY')
# COMMON_DB='postgresql://jfojszyitrmbii:f5bb5c5468fbfc793228f84f6b11fea6cfb88de98776bebf5f50a65c798f6eaf@ec2-44-206-11-200.compute-1.amazonaws.com:5432/dat4dhpej8rit3'
COMMON_DB='sqlite:///common.db'

class Config(object):
    SECRET_KEY=SECRET_KEY
    SQLALCHEMY_DATABASE_URI=COMMON_DB
    SQLALCHEMY_TRACK_MODIFICATIONS=False