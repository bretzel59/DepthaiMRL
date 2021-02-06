#!/usr/bin/env python3

# using websocket message interface
# first - install the websocket library
# for python 3 run the following
# pip3 install websockets jsonpickle

# websocket example
msg = {
        "msgId":1612651487089,
        "name":"python",
        "method":"onDepthAi",
        "historyList":[],
        "data":["teacup"]
    }



# reference - https://pypi.org/project/websocket_client/

# from websocket import create_connection
# import jsonpickle

# ws = create_connection("ws://localhost:8888/api/messages")
# print("sending message ....")
# ws.send(jsonpickle.encode(msg))
# # ... send more stuff if you want
# ws.close()

# http GET example
import http.client
import json


object_found = 'teacup'
connection = http.client.HTTPConnection('localhost', 8888)
headers = {'Content-type': 'application/json'}
connection.request("GET", "/api/service/python/exec/onDepthAi('" + object_found + "')")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))
print(response.read().decode())