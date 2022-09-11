import flask
import os
import planesBackEnd
from re import sub

app = flask.Flask(__name__)

@app.route("/<reg>")
def index(reg):
    reg = sub(r'[^\w\s]', '', reg)
    planesBackEnd.addPlaneToTrack(str(reg))
    print(reg)

def main():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))