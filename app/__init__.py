from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_cors import CORS

from .api.routes import api
from .auth.routes import auth
from .site.routes import site

from .helpers import JSONEncoder
from .models import db as root_db, login_manager, ma

app = Flask(__name__)

app.register_blueprint(api)
app.register_blueprint(auth)
app.register_blueprint(site)

app.config.from_object(Config)

root_db.init_app(app)
migrate = Migrate(app, root_db)

ma.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

app.json_encoder = JSONEncoder

CORS(app)