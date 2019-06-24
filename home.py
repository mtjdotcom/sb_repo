from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="mtjdotcom",
    password="bigbutts.com",
    hostname="mtjdotcom.mysql.pythonanywhere-services.com",
    databasename="mtjdotcom$emails",)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Comment(db.Model):

    __tablename__ = "emails"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))


email = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("landing_page.html", email=email)

    email.append(request.form['contents'])
    return redirect(url_for(index))

