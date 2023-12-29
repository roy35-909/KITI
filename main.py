from flask import Flask,render_template,Response
from flask_socketio import SocketIO, send
from threading import Lock    


app = Flask(__name__)
app.config['SECRET'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")
thread = None
thread_lock = Lock()   



def background_thread():
    print("Generating random sensor values")
    
    st1 = 0
    st2 = 0
    
    while True:
        s1,s2 = 0,1
        if s1==st1:
            pass
        else:
            st1 = s1
            socketio.emit('message', {'id':1,'status':s1})
        if s2 ==st2:
            pass
        else:
            st2 = s2
            socketio.emit('message', {'id':2,'status':s2})
        socketio.sleep(1)
      



# When a Client Connected
@socketio.on('connect')
def on_connect():
    # global thread
    # print('Client connected')

    # global thread
    # with thread_lock:
    #     if thread is None:
    #         thread = socketio.start_background_task(background_thread)
    print('A client connected')
    send("Send From Server")
    
  

#When a Client Disconnected
@socketio.on('disconnect')
def on_disconnect():
    print('A client disconnected')

#Messageing 
@socketio.on('message')
def on_message(message):
    print('Received message: ' + message)
    send(message,broadcast=True)

    
def send_message(message):
    send(message)





#default Index.html page shows.
@app.route('/')
def index():
    return render_template('./index.html')



    



if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0")