from flask import Flask, render_template, request, jsonify
from motorControl import toggleMotor, moveDirection
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


@app.route('/toggle', methods=['POST'])
def toggle():
    print("Toggle request received")
    json = request.get_json()
    toggleMotor(json)
    return "Toggle request received"

@app.route('/move', methods=['POST'])
def move():
    print("Move request received")
    json = request.get_json()
    moveDirection(json)
    return "Move request received"

#   server.post('/move', (req, res) => {
#     move(motors, req.body);
#     res.end('Command Recieved');
#   });

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
