"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
# Create a file handler to log to a file
file_handler = logging.FileHandler('login.log')
file_handler.setLevel(logging.INFO)  # Set the desired logging level for this handler
file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s'))
app.logger.addHandler(file_handler)

# Create a console handler to log to the console (optional)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Set the desired logging level for this handler
console_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s'))
app.logger.addHandler(console_handler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
