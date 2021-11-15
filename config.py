
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

USER=os.environ.get('USERDB')
SENHA=os.environ.get('PASSWDDB')
DB=os.environ.get('DB')
SERVIDOR=os.environ.get('URL')
SECRET=os.environ.get('SECRETKEY')


#SQLALCHEMY_DATABASE_URI = f'mysql://{USER}:{SENHA}@{SERVIDOR}/{DB}'
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
SECRET_KEY = SECRET
DEBUD = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True


