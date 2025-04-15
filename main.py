from flask import Flask, render_template
from flask_socketio import SocketIO, send
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # for SocketIO session security
socketio = SocketIO(app)

# Simple chatbot logic
def chatbot_response(message):
    responses = [
        "Hello! How can I help you today?",
        "Nice to chat with you!",
        "Tell me more about that.",
        "I'm just a simple chatbot, but I love chatting!",
        "Interesting! Please continue..."
    ]
    return random.choice(responses)

# Serve index.html
@app.route('/')
def index():
    return render_template('index.html')

# Handle message events
@socketio.on('message')
def handle_message(msg):
    print(f"User: {msg}")
    reply = chatbot_response(msg)
    send(reply)  # send back to client

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=10000)
