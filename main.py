from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def index():
    return render_template('index.html')

@sock.route('/ws')
def websocket(ws):
    while True:
        data = ws.receive()
        if data:
            response = f"You said: {data}"
            ws.send(response)

if __name__ == '__main__':
    app.run()
