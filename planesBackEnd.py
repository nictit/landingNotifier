#altitude cheker and add plane to tracking aircraft functions
import readNwrite
import planesInAir
import TGapi

STND = ['B52', 'E3CF', 'E6', 'R135', 'B703', 'R135', 'U2', 'B742', 'E3TF', 'B752', 'B703']


# Check altitude of tracking a/c
# if alt < 1000m and 'alt now' < 'alt before' on more then 3m
#   then notify and delete plane from tracking
# if a/c is out of range then print it
# input - a/c in air and tracking planes
# output - updated tracking plane dict
def checkPlanes():
    inAir = planesInAir.getInAir()
    trackingPlanes = readNwrite.readTrackingPlanes()
    allUsersList = TGapi.allUsers(trackingPlanes)

    stndCheck(inAir, STND, trackingPlanes, allUsersList)
    infoUpdate(inAir, trackingPlanes)

def stndCheck(inAir, STND, trackingPlanes, allUsersList):
    print(inAir.keys())
    print(trackingPlanes.keys())
    for plane in inAir.keys():
        if (inAir[plane]['type'] in STND) and (plane in trackingPlanes.keys()) and (trackingPlanes[plane]['chat_id'] != allUsersList):
            msg = TGapi.stnd_msg(plane, inAir)
            usersList = list(set(allUsersList)-set(trackingPlanes[plane]['chat_id']))
            TGapi.sendTo(msg, usersList)
            trackingPlanes[plane]['chat_id'] += usersList
        elif inAir[plane]['type'] in STND and plane not in trackingPlanes.keys() and inAir[plane]['altitude'].isdigit() and int(inAir[plane]['altitude']) > 1000:
            msg = TGapi.stnd_msg(plane, inAir)
            TGapi.sendTo(msg, allUsersList)
            trackingPlanes[plane] = inAir[plane]
            trackingPlanes[plane]['chat_id'] += allUsersList
    readNwrite.writeTrackingPlanes(trackingPlanes)

def infoUpdate(inAir, trackingPlanes):
    delList = []  # list to write landed planes because u can't change dict size in loop
    for plane in trackingPlanes.keys():
        if plane in inAir.keys(): #if tracking plane in air
            if inAir[plane]['altitude'].isdigit() and trackingPlanes[plane]['altitude'].isdigit(): # if altitude info is correct
                if (int(inAir[plane]['altitude']) < 700) and (int(trackingPlanes[plane]['altitude']) - int(inAir[plane]['altitude']) >= 10):
                    msg = TGapi.landing_msg(plane, inAir)
                    usersList = trackingPlanes[plane]['chat_id']
                    TGapi.sendTo(msg, usersList)
                    delList.append(plane)
                    print(msg)
                else:
                    chat_id = trackingPlanes[plane]['chat_id']
                    trackingPlanes[plane] = inAir[plane]
                    trackingPlanes[plane]['chat_id'] = chat_id
            else:
                chat_id = trackingPlanes[plane]['chat_id']
                trackingPlanes[plane] = inAir[plane]
                trackingPlanes[plane]['chat_id'] = chat_id
        elif trackingPlanes[plane]['status'] != 'out-of-range': # if plane disappeared and status != OoR
            trackingPlanes[plane]['status'] = 'out-of-range'
            msg = TGapi.outOfRange_msg(plane, trackingPlanes)
            usersList = trackingPlanes[plane]['chat_id']
            TGapi.sendTo(msg, usersList)

    [trackingPlanes.pop(key) for key in delList]
    readNwrite.writeTrackingPlanes(trackingPlanes)
    print('altCheck finished, tracking planes=', trackingPlanes.keys())

#try add plane to track
# three possible scinarios: 1. a/c already tracking 2. will be tracked 3. a/c not found
def addPlaneToTrack(plane, chat_id):
    inAir = planesInAir.getInAir()
    trackingPlanes = readNwrite.readTrackingPlanes()
    if plane in trackingPlanes.keys():
        if chat_id in trackingPlanes[plane]['chat_id']:
            msg = TGapi.alreadyTracking_msg(plane, inAir)
            print(msg)
            TGapi.sendMsg(chat_id, msg)
            return False
        else:
            trackingPlanes[plane]['chat_id'].append(chat_id)
            msg = TGapi.willTrack_msg(plane, inAir)
            readNwrite.writeTrackingPlanes(trackingPlanes)
            TGapi.sendMsg(chat_id, msg)

    elif plane in inAir.keys():
        trackingPlanes[plane] = inAir[plane]
        trackingPlanes[plane]['chat_id'].append(chat_id)
        msg = TGapi.willTrack_msg(plane, inAir)
        print(msg)
        TGapi.sendMsg(chat_id, msg)
        readNwrite.writeTrackingPlanes(trackingPlanes)
        return True
    else:
        msg = TGapi.notFound_msg(plane)
        print(msg)
        TGapi.sendMsg(chat_id, msg)
        return False


"""
def getRegion(coord):
    a = requests.get(f'http://api.positionstack.com/v1/reverse?access_key=8a5f09a51acbcff9fb3b5fbd1c20bca4&query={coord[0]},{coord[1]}&language=eng')
    return a.text

coord = ["49.656", "13.269"]
jsoan = json.loads(getRegion(coord))
print(jsoan)
print(jsoan['data'][0]['region'], jsoan['data'][0]['country_code'])
"""
