import planesBackEnd
from re import sub
import flask
import os
import TGapi

app = flask.Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    print('======', flask.request.json)
    chat_id, user_name, msg_text = TGapi.WH_analyse(flask.request.json)
    print(str(chat_id), str(user_name), str(msg_text))
    reg = sub(r'[^\w\s]', '', msg_text)
    planesBackEnd.addPlaneToTrack(str(reg))
    return 'its ok'

def main():
    TGapi.deleteWH()
    print('setting WH')
    #TGapi.setWH('https://fortesty.herokuapp.com')
    print(TGapi.setWH('https://3ee0-87-226-251-234.ngrok.io'))
    print('WH set')
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))