from flask import Flask, request, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setup SCSS jika diperlukan
Scss(app, static_dir='static', asset_dir='assets')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calculate", methods=["POST"])
def faktorial():
    num1 = int(request.form['num1'])
    angka = 1
    for i in range(1, num1 + 1):
        angka *= i
    return render_template('index.html', hasil=f"Hasilnya adalah {angka}")

if __name__ == "__main__":
    app.run(debug=True)