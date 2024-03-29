from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import login_details

app = Flask(__name__)

app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username=login_details.username,
    password=login_details.password,
    hostname=login_details.hostname,
    databasename=login_details.databasename,)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Email(db.Model):

    __tablename__ = "emails"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html", email=Email.query.all())

    email = Email(content=request.form['contents'])
    db.session.add(email)
    db.session.commit()
    return redirect(url_for('thanks'))

# @app.route('/home', methods=['GET', 'POST'])
# def index():
#     if request.method == "GET":
#         return render_template("landing_page_home.html", email=Email.query.all())

#     email = Email(content=request.form['contents'])
#     db.session.add(email)
#     db.session.commit()
#     return redirect(url_for('thanks'))

# @app.route('/hospital', methods=['GET', 'POST'])
# def index():
#     if request.method == "GET":
#         return render_template("landing_page_hospital.html", email=Email.query.all())

#     email = Email(content=request.form['contents'])
#     db.session.add(email)
#     db.session.commit()
#     return redirect(url_for('thanks'))

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/thank_you')
def thanks():
    return render_template('thank_you.html')

@app.route('/atad_ssecca')
def login():
     return render_template('login_page.html')
