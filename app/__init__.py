from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
login_blueprint = Blueprint('login_blueprint', __name__, template_folder="templates")
db = SQLAlchemy()
db.init_app(app)
login = LoginManager(app)
login.login_view = 'login_blueprint.login'
migrations = Migrate(app, db, render_as_batch=True)

from app import routes, models
from app.blueprints import user_routes
