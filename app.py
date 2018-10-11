from flask import Flask, render_template, request, jsonify

# Remote RPIO
# from gpiozero import LED
from time import sleep

# red = LED(21)

# while True:
#     red.on()
#     sleep(1)
#     red.off()
#     sleep(1)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'


@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)


@app.route('/json')
def json():
    dictionary = {
        "Key1": "one",
        "Key2": 2
    }
    return jsonify(dictionary)


@app.route('/test', methods=['POST'])
def test():
    print("post request received")
    json = request.get_json()
    print(json)
    print(json["msg"])
    return "Hello From Server"

@app.route('/on')
def on():
    red.on()
    return "Successfully turned on"

@app.route('/off')
def off():
    red.off()
    return "Successfully turned off"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
