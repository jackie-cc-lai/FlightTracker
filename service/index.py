from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getFlights")
def getFlights():
    return "Flights"

@app.route("/auth")
def auth():
    return "authenticated"

@app.route('/healthcheck')
def healthcheck():
    response.status = 200
    response.text = "Server OK"
    return response