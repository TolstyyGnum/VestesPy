# -*- coding: utf-8 -*-
import vestespy
import time

def ondata(req, res, data):
	print("CHUNK LENGTH:", len(data))
	print(data)

def onend(req, res):
	res.send_all("OK")

def onrequest(server, req, res):
	print(req.headers)
	req.on("end", onend)
	req.on("data", ondata)

server = vestespy.Server(("localhost", 8000), debug=True)
server.on("request", onrequest)

server.serve_forever()