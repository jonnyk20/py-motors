from flask import Flask, render_template, request, jsonify
from motorControl import moveDirection

from time import sleep

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/json')
def json():
    dictionary = {
        "Key1": "one",
        "Key2": 2
    }
    return jsonify(dictionary)


@app.route('/move', methods=['POST'])
def move():
    print("Move request received")
    json = request.get_json()
    moveDirection(json)
    return "Move request received"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
