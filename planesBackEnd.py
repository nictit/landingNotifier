#altitude cheker and add plane to tracking aircraft functions
import readNwrite
import planesInAir
import TGapi


# Check altitude of tracking a/c
# if alt < 1000m and 'alt now' < 'alt before' on more then 3m
#   then notify and delete plane from tracking
# if a/c is out of range then print it
# 3280 (ft) = 1000m
# input - a/c in air and tracking planes
# output - updated tracking plane dict
def altCheck():
    print('altCheck started')
    inAir = planesInAir.getInAir()
    trackingPlanes = readNwrite.readTrackingPlanes()
    delList = [] # list to write landed planes because u can't change dict size in loop
    for planeReg in trackingPlanes.keys():
        if (planeReg in inAir.keys()) and inAir[planeReg]['altitude'].isdigit() and trackingPlanes[planeReg]['altitude'].isdigit():
            if (int(inAir[planeReg]['altitude']) < 1000) and (int(trackingPlanes[planeReg]['altitude']) - int(inAir[planeReg]['altitude']) >= 10) and (int(trackingPlanes[planeReg]['altitude']) >= int(inAir[planeReg]['altitude'])):
                msg = TGapi.landing_msg(planeReg, inAir)
                delList.append(planeReg)
                print(msg)
                TGapi.sendMsg(trackingPlanes[planeReg]['chat_id'], msg)
            else:
                chat_id = trackingPlanes[planeReg]['chat_id']
                trackingPlanes[planeReg] = inAir[planeReg]
                trackingPlanes[planeReg]['chat_id'] = chat_id
        elif trackingPlanes[planeReg]['status'] != 'out-of-range':
            print(f'a/c wit reg={planeReg} is Out-of-Range now or have no altitude data')
            trackingPlanes[planeReg]['status'] = 'out-of-range'
            msg = TGapi.outOfRange_msg(planeReg, trackingPlanes)
            TGapi.sendMsg(trackingPlanes[planeReg]['chat_id'], msg)
    [trackingPlanes.pop(key) for key in delList]
    readNwrite.writeTrackingPlanes(trackingPlanes)
    print('altCheck finished, tracking planes=', trackingPlanes.keys())

#try add plane to track
# three possible scinarios: 1. a/c already tracking 2. will be tracked 3. a/c not found
def addPlaneToTrack(reg, chat_id):
    inAir = planesInAir.getInAir()
    trackingPlanes = readNwrite.readTrackingPlanes()
    print('addPlaneToTrack started')
    print(inAir.keys())
    print(reg)
    if reg in trackingPlanes.keys():
        print('Already tracking')
        msg = TGapi.alreadyTracking_msg(reg, inAir)
        print(msg)
        TGapi.sendMsg(chat_id, msg)
        return False
    elif reg in inAir.keys():
        print('Will track this Plane')
        trackingPlanes[reg] = inAir[reg]
        trackingPlanes[reg]['chat_id'] = chat_id
        print(trackingPlanes.keys())
        msg = TGapi.willTrack_msg(reg, inAir)
        print(msg)
        TGapi.sendMsg(chat_id, msg)
        trackingPlanes[reg] = inAir[reg]
        readNwrite.writeTrackingPlanes(trackingPlanes)
        return True
    else:
        print("can't find a/c in air wit reg =", reg)
        msg = TGapi.notFound_msg(reg)
        print(msg)
        TGapi.sendMsg(chat_id, msg)
        return False


