from flask import Blueprint, request, abort, jsonify, render_template
from markupsafe import escape

send_route = Blueprint("send", __name__)

APIKEY = "e10adc3949ba59abbe56e057f20f883e"

@send_route.route("/", methods=['POST'], strict_slashes=False)
def send():
    requestJson = request.get_json(force=True)
    if requestJson["api_key"] == APIKEY:
        return requestJson
    else:
        return abort(403)


@send_route.route("/<api_key>/<measure>/<date>/<time>", methods=['POST'], strict_slashes=False)
def send_values(api_key, measure, date, time):
    if request.method == 'POST':
        if (escape(api_key) == APIKEY):
            data = jsonify(
                measure=escape(measure),
                date=escape(date),
                time=escape(time)
            )
            return data
        else:
            return abort(403)
        
    else:
        return abort(405)