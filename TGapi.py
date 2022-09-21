import requests

#https://api.telegram.org/bot5048232576:AAHKQXWuVI-KIFQOEsDEizTGo9A1Ahjk4cw/getUpdates
api_url = 'https://api.telegram.org/bot'
token = '5642731099:AAGRdddqBD79r0K3a1ogprX9lXvHIb7CYFI'
url = api_url + token + '/'

# set up webhook with given url
# return true if all is ok
def setWH(WH_url):
    json1 = {"url": WH_url}
    setWH_response = requests.post(url + 'setWebhook', json1)
    return setWH_response.json()['ok']

def deleteWH():
    deleteWH_response = requests.post(url + 'deleteWebhook')
    return deleteWH_response.json()['ok']


# return chat_id (to response the user) and user's name
#  who triggered webhook with ANY action
# !!! change "[-1]" before setting webhook up !!!
def WH_analyse(WH_triggered):
    chat_id = WH_triggered['message']['from']['id']
    user_name = WH_triggered['message']['from']['first_name']
    msg_text = WH_triggered['message']['text']
    return chat_id, user_name, msg_text

# send message to user, who triggered webhook
# return true if all is ok
# TODO reg should be copiable
# TODO planes status should be filtered by type
# TODO callsigh=link to adsb for inst https://globe.adsbexchange.com/?icao=ae0589

def sendMsg(chat_id, msg):
    msgJson = {
        "text": msg,
        "chat_id": chat_id,
        "parse_mode": "Markdown"
              }
    sendMsg_response = requests.post(url + 'sendMessage', msgJson)
    return sendMsg_response.json()['ok']

def sendTo(msg, userList):
    msgJson = {
        "text": msg,
        "chat_id": '',
        "parse_mode": "Markdown"}
    for user in userList:
        msgJson['chat_id'] = user
        print(msgJson)
        sendMsg_response = requests.post(url + 'sendMessage', msgJson)
    return 'ok'

def sendToOoR(msg, userList, plane):
    msgJson = {
        "text": msg,
        "chat_id": '',
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [[
                {
                    "text": "Удалить самолет",
                    "callback_data": ""
                }]
            ]
        }
    }
    for user in userList:
        msgJson['chat_id'] = user
        msgJson['reply_markup']['inline_keyboard'][0][0]['callback_data'] = plane
        print(msgJson)
        sendMsg_response = requests.post(url + 'sendMessage', msgJson)
        print(sendMsg_response.content)
    return 'ok'

def allUsers(trackingPlanes):
    allUserslList = []
    for reg in trackingPlanes.keys():
        allUserslList = list(set(allUserslList+trackingPlanes[reg]['chat_id']))
    return allUserslList

def stnd_msg(plane, inAir):
    msg = f'⚡️ {inAir[plane]["type"]} появился на радарах, бортовой - {plane}, позывной - {inAir[plane]["callsign"]}.'
    return msg

def landing_msg(plane, inAir):
    msg = f"🟢 Самолет заходит на посадку.\n" \
          f"Тип: _{inAir[plane]['type']}_\n" \
          f"Бортовой: _{plane}_\n" \
          f"Позывной: _{inAir[plane]['callsign']}_"
    return msg

def outOfRange_msg(plane, trackingPlanes):
    msg = f"🔴 Самолет вне зоны доступа.\n" \
          f"Тип: _{trackingPlanes[plane]['type']}_\n" \
          f"Бортовой: _{plane}_\n" \
          f"Позывной: _{trackingPlanes[plane]['callsign']}_\n" \
          f"Высота: _{trackingPlanes[plane]['altitude']}._"
    return msg

def alreadyTracking_msg(plane, inAir):
    print(type(plane))
    print(inAir.keys())
    msg = f"🟡 Самолет уже в списке отслеживаемых.\n" \
          f"Тип: _{inAir[plane]['type']}_\n" \
          f"Бортовой: _{plane}_\n" \
          f"Позывной: _{inAir[plane]['callsign']}_"
    return msg

def willTrack_msg(plane, inAir):
    msg = f"✅ Самолет добавлен в список отслеживаемых.\n" \
          f"Тип: _{inAir[plane]['type']}_\n" \
          f"Бортовой: _{plane}_\n" \
          f"Позывной: _{inAir[plane]['callsign']}_"
    return msg

def notFound_msg(planeReg):
    msg = f'Самолет с бортовым {planeReg} не найден.'
    return msg

def getStatus_msg(trackingPlanes, chat_id):
    msg = '_Текущий статус:_\n\n'
    a = []
    theUserAcDict = theUserAc(trackingPlanes, chat_id)
    if theUserAcDict:
        for plane in theUserAcDict:
            msg = msg + theUserAcDict[plane]['type'] + ' (' + theUserAcDict[plane]['callsign'] + ', ' + plane + ') - ' + theUserAcDict[plane]['status'] + ', alt - ' + theUserAcDict[plane]['altitude'] + 'ft' +'\n'
    else:
        msg = msg + 'самолетов нет'
    return msg


def theUserAc(trackingPlanes: object, chat_id: object) -> object:
    theUserAcDict = {}
    if trackingPlanes:
        for plane in trackingPlanes.keys():
            for ids in trackingPlanes[plane]['chat_id']:
                if ids==chat_id:
                    theUserAcDict[plane] = trackingPlanes[plane]
    return theUserAcDict
