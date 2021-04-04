from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def start():
    return render_template("index.html")

@app.route("/chart")
def chart():
    return render_template("chart.html")

@app.route("/by_country")
def by_country():
    return render_template("bycountry.html")