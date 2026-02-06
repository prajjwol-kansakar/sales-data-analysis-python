from flask import Flask, jsonify, render_template
from scrapinggoldprice import run_scraper

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/run-scraper")
def run_scraper_api():
    result = run_scraper()
    return jsonify(result)


@app.route("/api/bullion")
def get_data():
    import json
    return jsonify(json.load(open("data/bullion.json")))


if __name__ == "__main__":
    app.run()
