__author__ = 'xywy'
from websocket import create_connection
ws = create_connection("ws://echo.websocket.org/")
print "Sending 'Hello, World'..."
ws.send("Hello, World")
print "Sent"
print "Reeiving..."
result =  ws.recv()
print "Received '%s'" % result
ws.close()