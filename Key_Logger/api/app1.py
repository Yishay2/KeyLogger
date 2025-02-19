import configparser
import os
from flask import current_app, g, Flask
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = PyMongo(current_app).db
    return db

def create_app():

    app = Flask(__name__)

    @app.route("/api/", methods=["GET"])
    def send_key_logger_data():


db = LocalProxy(get_db)
config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == "__main__":
    app = create_app()