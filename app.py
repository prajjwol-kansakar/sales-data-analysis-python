from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/bullion")
def bullion_data():
    return jsonify(
        __import__("json").load(open("data/bullion.json"))
    )

@app.route("/api/latest-screenshot")
def latest_screenshot():
    folder = "data/screenshots"
    files = sorted(os.listdir(folder), reverse=True)
    return {"url": f"/screenshot/{files[0]}"} if files else {}

@app.route("/screenshot/<filename>")
def screenshot(filename):
    return send_from_directory("data/screenshots", filename)

if __name__ == "__main__":
    app.run()
