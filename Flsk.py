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
        readNwrite.clearTrackingPlane(chat_id, flask.request.json['callback_query']['data'])
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
            msg = TGapi.getStatus_msg(readNwrite.readTrackingPlanes(), chat_id)
            print(msg, user_name)
            TGapi.sendMsg(chat_id, msg)
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
    print(TGapi.setWH('https://6e39-87-226-251-234.ngrok.io'))
    print('WH set')
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


#a = {'update_id': 290319888, 'callback_query': {'id': '2832892368755282441', 'from': {'id': 659584153, 'is_bot': False, 'first_name': 'Nick', 'username': 'nictit', 'language_code': 'en'}, 'message': {'message_id': 1826, 'from': {'id': 5642731099, 'is_bot': True, 'first_name': 'Плейнвочер', 'username': 'Whereismyairbot'}, 'chat': {'id': 659584153, 'first_name': 'Nick', 'username': 'nictit', 'type': 'private'}, 'date': 1663739366, 'text': '🔴 Самолет вне зоны доступа.\nТип: R135\nБортовой: 624130\nПозывной: HUNTR53\nВысота: 27975.', 'entities': [{'offset': 34, 'length': 4, 'type': 'italic'}, {'offset': 49, 'length': 6, 'type': 'italic'}, {'offset': 66, 'length': 7, 'type': 'italic'}, {'offset': 82, 'length': 6, 'type': 'italic'}], 'reply_markup': {'inline_keyboard': [[{'text': 'Удалить самолет', 'callback_data': '624130'}]]}}, 'chat_instance': '-5176765374821956987', 'data': '624130'}}
