import os
from flask import Flask, render_template

# HTML dibaca dari folder yang sama dengan app.py
app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/visualisasi")
def visualisasi():
    return render_template("visualisasi.html")


if __name__ == "__main__":
    app.run(debug=True)
