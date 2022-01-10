from flask import Flask, render_template, request, url_for

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


def calculate_serial(decimal_number):
    decimal_number += 167
    hex_number = hex(decimal_number).lstrip("0x").rstrip("L").upper()

    hex_str = str(hex_number)
    # remove A
    hex_str = hex_str[1:]

    hex_str = hex_str[2] + hex_str[3] + hex_str[0] + hex_str[1]

    hex_int = int(hex_str, 16)

    hex_int = "000" + str(hex_int)

    return hex_int


if __name__ == '__main__':
    app.run(debug=True)
