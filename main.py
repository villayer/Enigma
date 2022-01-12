from flask import Flask, render_template, request
from calculation_script import calculate_serial

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        if request.method == "POST":
            dec_number = request.form["dec_number"]
            res = calculate_serial(int(dec_number))
            return render_template("output.html", res="Votre code est " + res, code=res)
        else:
            return render_template("index.html")
    except ValueError:
        return render_template("output.html", res="ERREUR: Valeur null")


@app.route('/home', methods = ['GET', 'POST'])
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
