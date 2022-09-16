#altitude cheker and add plane to tracking aircraft functions
import readNwrite
import planesInAir
import TGapi

STND = ['B52', 'E3CF', 'E6', 'R135', 'B703', 'R135', 'U2', 'B742', 'E3TF', 'B752']


# Check altitude of tracking a/c
# if alt < 1000m and 'alt now' < 'alt before' on more then 3m
#   then notify and delete plane from tracking
# if a/c is out of range then print it
# 3280 (ft) = 1000m
# input - a/c in air and tracking planes
# output - updated tracking plane dict
def altCheck():
    inAir = planesInAir.getInAir()
    trackingPlanes = readNwrite.readTrackingPlanes()
    allUsersList = allUsers(trackingPlanes)
    for plane in inAir.keys():
        if (inAir[plane]['type'] in STND) and (plane in trackingPlanes.keys()) and (trackingPlanes[plane]['chat_id']!=allUsersList):
            msg = f'⚡️ {inAir[plane]["type"]} появился на радарах, позывной - {inAir[plane]["callsign"]}, бортовой - {plane}'
            for ids in list(set(allUsersList)-set(trackingPlanes[plane]['chat_id'])):
                TGapi.sendMsg(ids, msg)
                trackingPlanes[plane]['chat_id'].append(ids)
                #list(set(trackingPlanes[plane]['chat_id']))
                chat_id = trackingPlanes[plane]['chat_id']
                trackingPlanes[plane] = inAir[plane]
                trackingPlanes[plane]['chat_id'] = chat_id
        elif inAir[plane]['type'] in STND and plane not in trackingPlanes.keys():
            msg = f'⚡️ {inAir[plane]["type"]} появился на радарах, позывной - {inAir[plane]["callsign"]}, бортовой - {plane}'
            trackingPlanes[plane] = inAir[plane]
            for ids in list(set(allUsersList)):
                TGapi.sendMsg(ids, msg)
                trackingPlanes[plane]['chat_id'].append(ids)

    delList = [] # list to write landed planes because u can't change dict size in loop
    for planeReg in trackingPlanes.keys():
        if (planeReg in inAir.keys()) and inAir[planeReg]['altitude'].isdigit() and trackingPlanes[planeReg]['altitude'].isdigit():
            if (int(inAir[planeReg]['altitude']) < 1000) and (int(trackingPlanes[planeReg]['altitude']) - int(inAir[planeReg]['altitude']) >= 10):
                msg = TGapi.landing_msg(planeReg, inAir)
                delList.append(planeReg)
                print(msg)
                for ids in trackingPlanes[planeReg]['chat_id']:
                    TGapi.sendMsg(ids, msg)
            else:
                chat_id = trackingPlanes[planeReg]['chat_id']
                trackingPlanes[planeReg] = inAir[planeReg]
                trackingPlanes[planeReg]['chat_id'] = chat_id
        elif (planeReg not in inAir.keys()) and trackingPlanes[planeReg]['status'] != 'out-of-range':
            trackingPlanes[planeReg]['status'] = 'out-of-range'
            msg = TGapi.outOfRange_msg(planeReg, trackingPlanes)
            print(msg)
            for ids in trackingPlanes[planeReg]['chat_id']:
                TGapi.sendMsg(ids, msg)
    [trackingPlanes.pop(key) for key in delList]
    readNwrite.writeTrackingPlanes(trackingPlanes)
    print('altCheck finished, tracking planes=', trackingPlanes.keys())

#try add plane to track
# three possible scinarios: 1. a/c already tracking 2. will be tracked 3. a/c not found
def addPlaneToTrack(reg, chat_id):
    inAir = planesInAir.getInAir()
    trackingPlanes = readNwrite.readTrackingPlanes()
    if reg in trackingPlanes.keys():
        if chat_id in trackingPlanes[reg]['chat_id']:
            msg = TGapi.alreadyTracking_msg(reg, inAir)
            print(msg)
            TGapi.sendMsg(chat_id, msg)
            return False
        else:
            trackingPlanes[reg]['chat_id'].append(chat_id)
            msg = TGapi.willTrack_msg(reg, inAir)
            readNwrite.writeTrackingPlanes(trackingPlanes)
            TGapi.sendMsg(chat_id, msg)

    elif reg in inAir.keys():
        trackingPlanes[reg] = inAir[reg]
        trackingPlanes[reg]['chat_id'].append(chat_id)
        print(trackingPlanes.keys())
        msg = TGapi.willTrack_msg(reg, inAir)
        print(msg)
        TGapi.sendMsg(chat_id, msg)
        readNwrite.writeTrackingPlanes(trackingPlanes)
        return True
    else:
        msg = TGapi.notFound_msg(reg)
        print(msg)
        TGapi.sendMsg(chat_id, msg)
        return False

def allUsers(trackingPlanes):
    allUserslList = []
    for reg in trackingPlanes.keys():
        allUserslList = list(set(allUserslList+trackingPlanes[reg]['chat_id']))
    return allUserslList

