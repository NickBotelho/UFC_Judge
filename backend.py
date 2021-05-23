from flask import Flask, jsonify, request, render_template, send_file
from flask_cors import CORS, cross_origin
from model import GetWinnerPrediction

app = Flask(__name__, template_folder = 'frontend/server/build/')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/predict", methods = ["POST"])
@cross_origin(supports_credentials=True)
def postPrediction():
    if request.method == "POST":
        res = {"status": 200}
        red = request.json['red']
        blue = request.json['blue']
        print("POSTING fight stats...predicting...")
        winner = GetWinnerPrediction(red, blue)
        res['winner'] = winner
        return jsonify(res), res['status']

@app.route("/", methods = ["GET"])
@cross_origin(supports_credentials=True)
def serveHomepage():
    return render_template("index.html")

@app.route("/main.js", methods = ["GET"])
@cross_origin(supports_credentials=True)
def serveMain():
    return render_template("main.js")

@app.route("/components/c53d0741f4541d2d44a8f74583c49224.png", methods = ["GET"])
@cross_origin(supports_credentials=True)
def serveArrow():
    return send_file("frontend/server/build/c53d0741f4541d2d44a8f74583c49224.png", mimetype = "image/gif")

@app.route('/<path:text>', methods=['GET', 'POST'])
def all_routes(text):
    
    print(text)
    return render_template("index.html")
     

# app.run(debug = True)