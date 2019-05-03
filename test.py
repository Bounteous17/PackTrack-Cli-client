import socketio

my_username = input('My username: ')
username = input('To username: ')
message = input('Message: ') 

sio = socketio.Client()

sio.connect('http://localhost:5000', namespaces=['/messages', '/private'])
"""
@sio.on('connect', namespace='/messages')
def on_connect():
    print('I\'m connected to the /messages namespace - message from user!')
    sio.emit('message from user', message, namespace='/messages')

@sio.on('from flask', namespace='/messages')
def on_connect(data):
    print(f'{data} - from flask!')
"""
@sio.on('connect', namespace='/private')
def on_connect():
    print(f'I\'m connected to the /private namespace - username ({my_username})!')
    sio.emit('username', my_username, namespace='/private')
    print(f'I\'m connected to the /private namespace - private_message ({message})!')
    sio.emit('private_message', {'username': username, 'message': message}, namespace='/private')


"""@sio.on('connect', namespace='/private')
def on_connect():
    print('I\'m connected to the /private namespace - private_message!')
    sio.emit('private_message', {'username': username, 'message': message}, namespace='/private')
"""
@sio.on('new_private_message', namespace='/private')
def on_connect(data):
    print(f'{data} - new_private_message')


