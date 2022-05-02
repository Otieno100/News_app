# from distutils.debug import DEBUG
import os
class Config :
    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q=Apple&from=2022-04-29&sortBy=popularity&apiKey=11a3f56ac5454a2e8cb356446f33ab49'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    # SECRET_KEY = os.environ.get('SECRET_KEY')

class prodConfig (Config):
        pass
class DevConfig(Config):

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production' : prodConfig
    }    