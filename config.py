import os

#ключ для подписи данных
SECRET_KEY = os.urandom(32)

#захват папки в которой запущен скрипт
basedir = os.path.abspath(os.path.dirname(__file__))

#включение режима отладки
DEBUG = True

#URI базы данных
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:2009@localhost:5432/mydb'

# отключение системы событий и предупреждений Flask-SQLAlchemy.
SQLALCHEMY_TRACK_MODIFICATIONS = False