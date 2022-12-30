import planesBackEnd
from re import sub
import flask
import os
import TGapi
import readNwrite

app = flask.Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    #return "True"
    print(flask.request.json)
    if 'callback_query' in flask.request.json.keys():
        chat_id = flask.request.json['callback_query']['message']['chat']['id']
        message_id = flask.request.json['callback_query']['message']['message_id']
        #readNwrite.clearTrackingPlane(chat_id, flask.request.json['callback_query']['data'])
        print('ПРИШЕЛ СОЛБЕК')
        print(flask.request.json['callback_query']['data'])
        plane = flask.request.json['callback_query']['data']
        readNwrite.clearTrackingPlane(chat_id, plane)
        msg, inline_keyboard = TGapi.getStatus_msg(readNwrite.readTrackingPlanes(), chat_id)
        TGapi.editMsgForStatus(chat_id, message_id, msg, inline_keyboard)

    elif 'message' in flask.request.json.keys():
        chat_id, user_name, msg_text = TGapi.WH_analyse(flask.request.json)
        if msg_text == '/start':
            msg = f'Привет, {user_name}!\n' \
                  f'- Чтобы начать следить за самолетом просто напиши мне его бортовой номер.\n' \
                  f'- Когда его высота будет меньше 300 метров я тебе сообщу.\n' \
                  f'- Чтобы проверить текущий статус отслеживаемых самолетов напиши "status".\n' \
                  f'- Чтобы очистить список отслеживаемых самолетов напиши "clear all."'

            TGapi.sendMsg(chat_id, msg)
        elif msg_text.lower()=='status':
            msg, inline_keyboard = TGapi.getStatus_msg(readNwrite.readTrackingPlanes(), chat_id)
            print(msg, user_name)
            TGapi.sendMsgForStatus(chat_id, msg, inline_keyboard)
        elif msg_text.lower()=='stop':
            msg = readNwrite.clearTrackingPlanes(chat_id)
            TGapi.sendMsg(chat_id, msg)
        elif msg_text.lower()=='clear all*':
            msg = readNwrite.clearAll()
            TGapi.sendMsg(chat_id, msg)

        else:
            print(str(chat_id), str(user_name), str(msg_text))
            reg = sub(r'[^\w\s]', '', msg_text)

            planesBackEnd.addPlaneToTrack(reg.upper(), chat_id)
    return 'its ok'

def main():
    TGapi.deleteWH()
    #print(TGapi.setWH('https://whereismyairbot.herokuapp.com'))
    print(TGapi.setWH('https://fortesty.herokuapp.com'))
    print('WH set')
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
