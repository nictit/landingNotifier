# read and write trackingPlanes dict into json file

import json

def readTrackingPlanes():
    with open('trackingPlanes.json') as json_file:
        try:
            trackingPlanes = json.load(json_file)
            return trackingPlanes
        except:
            print('tracking Planes (json file) error')
            return 'tracking Planes (json file) error'


def writeTrackingPlanes(trackingPlanes):
    if isinstance(trackingPlanes, dict): #if tracking planes is correct dict
        print('ok its dict')
        with open('trackingPlanes.json', 'w') as json_file:
            try:
                json.dump(trackingPlanes, json_file)
                print('====writeTrackingPlanes finished', trackingPlanes)
                return trackingPlanes
            except:
                print('tracking Planes (json file) error')
                return 'tracking Planes (json file) error'
    else:
        print('trackingPlanes has incorrect format')
        return 'trackingPlanes has incorrect format'

def clearTrackingPlanes(chat_id):
    trackingPlanes = readTrackingPlanes()
    if trackingPlanes:
        for plane in trackingPlanes.keys():
            for ids in trackingPlanes[plane]['chat_id']:
                if ids == chat_id:
                    trackingPlanes[plane]['chat_id'].remove(ids)
    writeTrackingPlanes(trackingPlanes)
    msg = 'all planes were deleted'
    return msg

def clearTrackingPlane(chat_id, plane):
    trackingPlanes = readTrackingPlanes()
    if trackingPlanes:
        for ids in trackingPlanes[plane]['chat_id']:
            if ids == chat_id:
                trackingPlanes[plane]['chat_id'].remove(ids)
    writeTrackingPlanes(trackingPlanes)
    msg = plane + '  was deleted'
    return msg

def clearAll():
    writeTrackingPlanes('{}')
    msg = 'ALL were deleted'
    return 'ok'