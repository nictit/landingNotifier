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



def landing_msg(planeReg, inAir):
    msg = f"🟢 Самолет заходит на посадку.\n" \
          f"Тип: _{inAir[planeReg]['type']}_\n" \
          f"Бортовой: _{planeReg}_\n" \
          f"Позывной: _{inAir[planeReg]['callsign']}_"
    return msg

def outOfRange_msg(planeReg, trackingPlanes):
    msg = f"🔴 Самолет вне зоны доступа.\n" \
          f"Тип: _{trackingPlanes[planeReg]['type']}_\n" \
          f"Бортовой: _{planeReg}_\n" \
          f"Позывной: _{trackingPlanes[planeReg]['callsign']}_"
    return msg

def alreadyTracking_msg(planeReg, inAir):
    msg = f"🟡 Самолет уже в списке отслеживаемых.\n" \
          f"Тип: _{inAir[planeReg]['type']}_\n" \
          f"Бортовой: _{planeReg}_\n" \
          f"Позывной: _{inAir[planeReg]['callsign']}_"
    return msg

def willTrack_msg(planeReg, inAir):
    msg = f"✅ Самолет добавлен в список отслеживаемых.\n" \
          f"Тип: _{inAir[planeReg]['type']}_\n" \
          f"Бортовой: _{planeReg}_\n" \
          f"Позывной: _{inAir[planeReg]['callsign']}_"
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
            msg = msg + theUserAcDict[plane]['type'] + ' (' + theUserAcDict[plane]['callsign'] + ', ' + plane + ') - ' + theUserAcDict[plane]['status'] + '\n'
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
