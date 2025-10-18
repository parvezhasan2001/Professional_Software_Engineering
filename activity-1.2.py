# Week-12
# Activity-1.2

from flask import Flask

app = Flask(__name__)


@app.route("/cal/<int:number>")
def activity_2(number):
    return f"The square of {number} is {number ** 2}"


if __name__ == "__main__":
    app.run(debug=True)
