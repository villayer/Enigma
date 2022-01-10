from flask import Flask, render_template, request
from calculation_script import calculate_serial

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        dec_number = request.form["dec_number"]
        if dec_number is None:
            res = "error!"
        else:
            res = calculate_serial(int(dec_number))
        return render_template("index.html", res=res)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
