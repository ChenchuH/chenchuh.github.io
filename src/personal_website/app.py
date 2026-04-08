from flask import Flask, render_template
from flask_frozen import Freezer
from datetime import datetime

app = Flask(__name__)
app.config["FREEZER_RELATIVE_URLS"] = True
freezer = Freezer(app)

@app.route("/")
def home():
    return render_template("index.html", year = datetime.now().year)

@app.route("/projects/")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True)