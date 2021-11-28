from flask import Flask
from datetime import datetime as dt

app = Flask(__name__)

@app.route("/")
def landing():
    now = dt.now()
    greeting = f'[{now.strftime("%Y-%m-%d %H:%M:%S")}]: Hello from Flask@5000'
    return greeting


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')