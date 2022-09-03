import dj_database_url
import django_on_heroku
from decouple import config
from .base import *
 
SECRET_KEY = config('SECRET_KEY')

# 要上傳到heroku ,就要True
DEBUG = True
 
ALLOWED_HOSTS = [
  'ryowu-basic-blog.herokuapp.com',
  'ryowu.blog'
]
 
DATABASES = {'default': dj_database_url.config(default='sqlite://db.sqlite3',conn_max_age=600,ssl_require=False)}

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'verbose': {
      'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
      'datefmt': "%d/%b/%Y %H:%M:%S"
    },
    'simple': {
      'format': "%(levelname)s %(message)s"
    }
  },
  'handlers': {
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler'
    }
  },
  'loggers' : {
    'MYAPP' : {
      'handlers': ['console'],
      'level': 'DEBUG'
    }
  }
}
 
django_on_heroku.settings(locals(),staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']

  
