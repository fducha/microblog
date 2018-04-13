from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


application = Flask(__name__)
application.config.from_object(Configuration)
db = SQLAlchemy(application)
migarate = Migrate(app=application, db=db)

from app import routes, models