from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from models import User


if __name__ == "__main__":

    app = Flask(__name__)
    app.config.from_object(Config)
    app.debug = True
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    from app.routes import index_blueprint, login_blueprint, logout_blueprint, register_blueprint, user_blueprint
    from app import models


    app.register_blueprint(index_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(logout_blueprint)
    app.register_blueprint(register_blueprint)
    app.register_blueprint(user_blueprint)

    app.run()


# if __name__ == "__main__":
#     app.debug = True
#     app.run()
