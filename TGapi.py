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
# 659584153
def sendMsg(chat_id, msg):
    msgJson = {
        "text": msg,
        "chat_id": chat_id,
        "parse_mode": "Markdown"
              }
    sendMsg_response = requests.post(url + 'sendMessage', msgJson)
    return sendMsg_response.json()['ok']



def landing_msg(planeReg, inAir):
    msg = f"Aircraft is landing.\n" \
          f"Reg: _{planeReg}_\n" \
          f"Type: _{inAir[planeReg]['type']}_\n" \
          f"Callsign: _{inAir[planeReg]['callsign']}_"

    print(msg)
    return msg

def outOfRange_msg(planeReg, trackingPlanes):
    msg = f"Aircraft is out-of-range.\n" \
          f"Reg: _{planeReg}_\n" \
          f"Type: _{trackingPlanes[planeReg]['type']}_\n" \
          f"Callsign: _{trackingPlanes[planeReg]['callsign']}_"
    print(msg)
    return msg

#inAir[planeReg]['type']
def alreadyTracking_msg(planeReg, inAir):
    msg = f"Aircraft already tracking.\n" \
          f"Reg: _{planeReg}_\n" \
          f"Type: _{planeReg}_\n" \
          f"Callsign: _{planeReg}_"

    print(msg)
    return msg

def willTrack_msg(planeReg, inAir):
    msg = f"Aircraft is tracking now.\n" \
          f"Reg: _{planeReg}_\n" \
          f"Type: _{inAir[planeReg]['type']}_\n" \
          f"Callsign: _{inAir[planeReg]['callsign']}_"
    print(msg)
    return msg

def notFound_msg(planeReg):
    msg = f'Plane with reg={planeReg} not found.'
    print(msg)
    return msg

# ch - checker is where need to add 'no planes' string ot not
def getStatus_msg(trackingPlanes, chat_id):
    msg = '_Planes Statuses:_\n\n'
    ch = True
    if trackingPlanes:
        for plane in trackingPlanes.keys():
            if trackingPlanes[plane]['chat_id']==chat_id:
                msg = msg + trackingPlanes[plane]['type'] + ' (' + trackingPlanes[plane]['callsign'] + ', ' + plane + ') - ' + trackingPlanes[plane]['status'] + '\n'
                ch = False
    if ch:
        msg = msg +'no planes'
    return msg