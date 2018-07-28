from flask import Flask, jsonify, render_template, request
from carfunctions import Forward, Left, Right, Stop, Backward
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/control")
def control():

    q = request.args.get("q")

    if q == "forward":
        Forward()
    elif q == "left":
        Left()
    elif q == "right":
        Right()
    elif q == "stop":
        Stop()
    elif q == "backward":
        Backward()

    response = "Moving {}".format(q)

    return response, 200, {'content-Type': 'text/plain'}
