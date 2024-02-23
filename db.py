from flask import Flask
# from flask import render_template
# from flask import request
# from flask import redirect
# from flask import url_for
# from flask import make_response
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_alembic import Alembic
from datetime import datetime
# import os as system

# from app import app

new_data = {}

app = Flask(__name__)
app.config["SECRET_KEY"] = "mySecretKey"


# CREATING NEW DBs:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

db = SQLAlchemy()
db.init_app(app)

alembic = Alembic()
alembic.init_app(app, db)



class Balance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float(127), nullable=False)


class Warehoue(db.Model):
    product_name = db.Column(db.String, primary_key=True)
    product_price = db.Column(db.Float, nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)


class History(db.Model):
    date_transaction = db.Column(db.DateTime, default = datetime.now, primary_key=True)
    user = db.Column(db.String, nullable=False)
    transaction = db.Column(db.String, nullable=False)
    value = db.Column(db.Float, nullable=False)