import planesBackEnd
from re import sub
import flask
import os
import TGapi

app = flask.Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    chat_id, user_name, msg_text = TGapi.WH_analyse(flask.request.json)
    print(str(chat_id), str(user_name), str(msg_text))
    reg = sub(r'[^\w\s]', '', msg_text)
    planesBackEnd.addPlaneToTrack(str(reg))

def main():
    TGapi.deleteWH()
    print('setting WH')
    TGapi.setWH('https://whereismyairbot.herokuapp.com')
    print('WH set')
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5050)))