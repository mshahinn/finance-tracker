from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100),nullable = False)
    email = db.Column(db.String(100),unique =True,nullable = False)
    password_hash =db.Column(db.String(255),nullable = False)


@app.route("/")
def home():
    return "hello"
if __name__ == "__main__":
    with app.app_context():
       db.create_all()
    app.run(debug=True)