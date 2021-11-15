from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy 
import pymysql
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))



pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager(app)
db = SQLAlchemy(app)