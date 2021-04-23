from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def start():
    return render_template("index.html")

@app.route('/per_capita')
def per_capita():
    return render_template("index_per_capita.html")

@app.route("/bubble")
def bubble():
    return render_template("bubble.html")

@app.route("/bubble_per_capita")
def bubble_per_capita():
    return render_template("bubble_per_capita.html")

@app.route("/by_country")
def by_country():
    return render_template("bycountry.html")

@app.route("/by_country_per_capita")
def by_country_per_capita():
    return render_template("bycountry_percapita.html")