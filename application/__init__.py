from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
#from application import routes
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = os.getenv("SECRET")
schooldb = SQLAlchemy(app)

from application import routes 
