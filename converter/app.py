from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://open.er-api.com/v6/latest/"


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    currencies = [
        "USD",
        "EUR",
        "RUB",
        "GBP",
        "CNY",
        "JPY",
        "KZT",
        "BYN"
    ]

    if request.method == "POST":

        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]

        response = requests.get(API_URL + from_currency)
        data = response.json()

        rate = data["rates"][to_currency]

        result = round(amount * rate, 2)

    return render_template(
        "index.html",
        currencies=currencies,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)