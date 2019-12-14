from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

from database import Contact

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts-collection.db'
db = SQLAlchemy(app)

# Import db, Contact from this class and use queries
# For ex) db.session.query(Contact).filter_by(phone_num='01012345678').count()