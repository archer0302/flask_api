from flask import Flask, jsonify
from quotes import funny_quotes
import random

app = Flask(__name__)


@app.route("/api/funny")
def serve_funny_quote():
    quotes = funny_quotes()
    length_of_quotes = len(quotes)
    select_quote = quotes[random.randint(0, length_of_quotes - 1)]
    return jsonify(select_quote)


if __name__ == '__main__':
    app.run(debug=True)
