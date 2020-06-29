# import time
# import eventlet
# from utils import nums
# from itertools import *
# from flask import Flask, render_template
# from flask_socketio import SocketIO
#
# eventlet.monkey_patch()
#
# app = Flask(__name__)
# socketio = SocketIO(app, cors_allowed_origins="*", transports=['websocket'])
#
# automatic_timeout_value = 30
# most_recent = 0
# starting = 0
#
# def crunch(divider, starting):
#
#     socketio.emit('msg from server', {"message": "starting crunch", "time": time.time()-1593360000})
#
#     socketio.sleep(1.0)
#
#     gut_gen = permutations(nums, 4)
#
#     while starting == most_recent and starting + automatic_timeout_value > time.time():
#         current_nums = next(gut_gen)
#         num = sum(current_nums)
#         if not num % divider:
#             print(num, switch)
#             socketio.sleep(1.0)
#             socketio.emit('result', {"result": num, "divider": divider, "time": time.time()-1593360000})
#     else:
#         socketio.sleep(0)
#         socketio.emit('msg from server', {"message": "The server stopped the process.", "time": time.time() - 1593360000})
#         print("Kicking out of while loop.", time.time()-1593360000)
#
# @app.route('/')
# def sessions(methods=['GET', 'POST']):
#     return render_template('session.html')
#
# @socketio.on('connect')
# def connect(methods=['GET', 'POST']):
#     print("connected", time.time())
#     socketio.emit('msg from server', {"message": "server connected: element Astatine", "time": time.time()-1593360000})
#
# @socketio.on('disconnect')
# def disconnect(methods=['GET', 'POST']):
#     global most_recent
#     most_recent = 0
#
# @socketio.on('msg from client')
# def receive(data, methods=['GET', 'POST']):
#     print('received msg: ' + str(data), time.time())
#     responding = "server received " + str(data["message"])
#     socketio.emit('msg from server', {"message": responding, "time": time.time()-1593360000})
#
# @socketio.on('go!')
# def go(data, methods=['GET', 'POST']):
#     global most_recent
#     starting = time.time()
#     most_recent = starting
#     divider = int(data["divider"])
#     print("client wants to GO", time.time())
#     socketio.emit("msg from server", {"message": "hi client, I hear you that you want to GO", "time": time.time()-1593360000})
#     global switch
#     switch = True
#     socketio.emit("msg from server", {"message": "soon gonna start crunch", "time": time.time()-1593360000})
#     socketio.sleep(0)
#     crunch(divider, starting)
#
# @socketio.on('stop!')
# def stop(data, methods=['GET', 'POST']):
#     socketio.sleep(0)
#     print("client wants to stop", time.time()-1593360000)
#     socketio.emit("msg from server", {"message": "hi client, I hear you that you want to stop", "time": time.time()-1593360000})
#     global most_recent
#     most_recent = time.time()
#     socketio.sleep(0)
#
# if __name__ == '__main__':
#     socketio.run(app, debug=False)
#
#
#
