from flask import Flask
from routes.send import send_route

app = Flask(__name__)

@app.route("/")
def mainpage():
    return "ok", 200

app.register_blueprint(send_route, url_prefix="/send")

app.run(debug=False)
