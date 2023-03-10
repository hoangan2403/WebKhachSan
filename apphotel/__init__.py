from urllib.parse import quote
from flask import Flask
from  urllib.parse import quote
from flask_login import LoginManager
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'Solar'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/hotelappdb?charset=utf8mb4' % quote('an01697769522')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app=app)


login = LoginManager(app=app)


babel = Babel(app=app)


@babel.localeselector
def load_locale():
    return 'vi'