# Dependency: pip install flask requests
from flask import Flask, request
from app import routes, models

# Define Flask webserver
app = Flask(__name__)

#global variables initialized
colleges = ""
machines = {}

#json directories - edit before deploying
queuefilepath = "./queue.json"
watchfilepath = "./watch.json"
usersfilepath = "./users.json"

