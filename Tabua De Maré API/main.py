from flask import Flask
from routes.send import send_route

app = Flask(__name__)

@app.route("/")
def mainpage():
    return "ok"

app.register_blueprint(send_route, url_prefix="/send")

app.run(host="192.168.18.64", port=3000)