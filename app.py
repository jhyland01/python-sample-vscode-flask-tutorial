from flask import Flask
from datetime import datetime
import re
from flask import *
import test

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    data = request.args
    keyword = data["Nhyp"]
    print(type(keyword))
    value = test.test_fn(int(keyword)) # output here is the string "you input:"
    return render_template("results.html", hyp=value)

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")