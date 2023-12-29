import socketio


sio = socketio.Client()

sio.connect('http://127.0.0.1:5000')
@sio.on('connect')
def on_connect():
    print('Connected to Flask Socket.IO server')
    sio.send("Robot Connected..")

@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from Flask Socket.IO server')

@sio.on('message') 
def on_message(data):
    print('Received data:', data)
    # sio.emit('message',{'message':'receved form robot.'})
    # if data=='stop':
    #     sio.disconnect()
    #     print('Disconnected from Flask Socket.IO server')
    




try:


    print('Connected to Flask Socket.IO server. Listening for messages...')
    # message = input('Enter a message to send: ')
    # sio.emit('send_message', {'message': message})


    sio.wait()

except KeyboardInterrupt:

    sio.disconnect()
    print('Disconnected from Flask Socket.IO server')
