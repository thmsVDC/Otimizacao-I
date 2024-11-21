from flask import Flask

from config import Config

app = Flask(__name__)
from app import routes

app.config["SECRET_KEY"] = Config.SECRET_KEY
