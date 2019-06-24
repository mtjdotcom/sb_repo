from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

app.config["DEBUG"] = True

email = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("landing_page.html", email=email)

    email.append(request.form['contents'])
    return redirect(url_for(index))

