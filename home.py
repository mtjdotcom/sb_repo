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

    # __tablename__ = "feedback"

    # id = db.Column(db.Integer, primary_key=True)
    # q1 = db.Column(db.String(4000))
    # q2 = db.Column(db.String(4000))
    # q3 = db.Column(db.String(4000))
    # q4 = db.Column(db.String(4000))
    # q5 = db.Column(db.String(4000))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("landing_page.html", email=Email.query.all())

    email = Email(content=request.form['contents'])
    db.session.add(email)
    db.session.commit()
    return redirect(url_for('thanks'))

@app.route('/feedback')#, methods=['GET', 'POST'])
def feedback():
    # if request.method == "GET":
    #     return render_template("feedback.html", email=Email.query.all())

    # q_1 = Email(q1=request.form['q_1'])
    # q_2 = Email(q2=request.form['q_2'])
    # q_3 = Email(q2=request.form['q_3'])
    # q_4 = Email(q2=request.form['q_4'])
    # q_5 = Email(q2=request.form['q_5'])

    # db.session.add(q_1)
    # db.session.add(q_2)
    # db.session.add(q_3)
    # db.session.add(q_4)
    # db.session.add(q_5)
    # db.session.commit()
    # return redirect(url_for('thanks'))
    return render_template('feedback.html')

@app.route('/thank_you')
def thanks():
    return render_template('thank_you.html')

@app.route('/atad_ssecca')
def login():
     return render_template('login_page.html')
