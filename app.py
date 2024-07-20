from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO, emit, join_room as socketio_join_room, leave_room as socketio_leave_room
from flask_cors import CORS
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

CORS(app)

socketio = SocketIO(app)

# Data for the app
chat_rooms = {}

@app.route('/')
def join_room_page():
    return render_template('join_room.html')

@app.route('/chat-room/<room_name>')
def chat_room_page(room_name):
    if room_name in chat_rooms:
        return render_template('index.html', room_name=room_name)
    return redirect(url_for('join_room_page'))

@socketio.on('check_room')
def check_room(room_name):
    if room_name in chat_rooms:
        emit('room_exists')
    else:
        chat_rooms[room_name] = {'messages': {}, 'users': []}
        emit('room_created')

@socketio.on('create_room')
def handle_create_room(room_name):
    if room_name not in chat_rooms:
        chat_rooms[room_name] = {'messages': {}, 'users': []}
        emit('update_rooms', list(chat_rooms.keys()), broadcast=True)

@socketio.on('join_room')
def handle_join_room(data):
    room = data.get('room')
    user = data.get('user')
    if not room or not user:
        print("Missing room or user in data:", data)
        return
    if room in chat_rooms:
        socketio_join_room(room)
        chat_rooms[room]['users'].append(user)
        print(f"User {user} joining room {room}")  # Debugging line
        # Emit system notification when a user joins
        emit('room_message', {'user': 'System', 'message': f'{user} has joined the room.', 'message_id': str(uuid.uuid4())}, room=room)
        emit('update_users', chat_rooms[room]['users'], room=room)
    else:
        print("Room does not exist:", room)

@socketio.on('leave_room')
def handle_leave_room(data):
    room = data.get('room')
    user = data.get('user')
    if not room or not user:
        print("Missing room or user in data:", data)
        return
    if room in chat_rooms:
        socketio_leave_room(room)
        chat_rooms[room]['users'].remove(user)
        emit('room_message', {'user': 'System', 'message': f'{user} has left the room.', 'message_id': str(uuid.uuid4())}, room=room)
        emit('update_users', chat_rooms[room]['users'], room=room)

@socketio.on('send_message')
def handle_send_message(data):
    room = data.get('room')
    user = data.get('user')
    message = data.get('message')
    message_id = data.get('message_id')
    if not room or not user or not message or not message_id:
        print("Missing room, user, message, or message_id in data:", data)
        return
    if room in chat_rooms:
        chat_rooms[room]['messages'][message_id] = {'user': user, 'message': message}
        emit('room_message', {'user': user, 'message': message, 'message_id': message_id}, room=room)
    else:
        print("Room does not exist:", room)

@socketio.on('edit_message')
def handle_edit_message(data):
    room = data.get('room')
    message_id = data.get('message_id')
    new_message = data.get('new_message')
    if not room or not message_id or not new_message:
        print("Missing room, message_id, or new_message in data:", data)
        return
    if room in chat_rooms:
        if message_id in chat_rooms[room]['messages']:
            chat_rooms[room]['messages'][message_id]['message'] = new_message
            emit('message_edited', {'message_id': message_id, 'new_message': new_message}, room=room)
        else:
            print("Message ID not found:", message_id)

@socketio.on('delete_message')
def handle_delete_message(data):
    room = data.get('room')
    message_id = data.get('message_id')
    if not room or not message_id:
        print("Missing room or message_id in data:", data)
        return
    if room in chat_rooms:
        if message_id in chat_rooms[room]['messages']:
            del chat_rooms[room]['messages'][message_id]
            emit('message_deleted', {'message_id': message_id}, room=room)
        else:
            print("Message ID not found:", message_id)

if __name__ == "__main__":
    socketio.run(app, debug=True, port=5001)
