from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
app.debug = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.init_app(app)
login.login_view = 'login'



@login.user_loader
def load_user(user_id):
    return None


from app.routes import index_blueprint, login_blueprint, logout_blueprint, register_blueprint, user_blueprint
from app import models


app.register_blueprint(index_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(logout_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(user_blueprint)


if __name__ == "__main__":
    app.debug = True
    app.run()
