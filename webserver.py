import os
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/api")
def index():
	return "Online"

def run():
	app.run(host="0.0.0.0",port=os.getenv("PORT") or 6000)

def start_webserver():
	t = Thread(target=run)
	t.start()