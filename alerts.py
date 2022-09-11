def send_msg(msg):
    pass


def landing_msg(planeReg, inAir):
    msg = f'TELEGRAM alert! Plane {inAir[planeReg]["type"]} (c/s - {inAir[planeReg]["callsign"]}, reg - {planeReg}) is landing. Current altitude is {inAir[planeReg]["altitude"]} feet'
    print(msg)
    return msg

def outOfRange_msg(planeReg, inAir):
    msg = f'TELEGRAM alert! Plane {inAir[planeReg]["type"]} (c/s - {inAir[planeReg]["callsign"]}, reg - {planeReg}) is out-of-range.'
    print(msg)
    return msg

def alreadyTracking_msg(planeReg, inAir):
    msg = f'TELEGRAM Plane {inAir[planeReg]["type"]} (c/s - {inAir[planeReg]["callsign"]}, reg - {planeReg}) was already tracking.'
    print(msg)
    return msg

def willTrack_msg(planeReg, inAir):
    msg = f"TELEGRAM a/c wit reg={planeReg} is tracking now. It is {inAir[planeReg]['type']}, callsign - {inAir[planeReg]['callsign']}"
    print(msg)
    return msg

def notFound_msg(planeReg):
    msg = f'TELEGRAM Plane with reg={planeReg} not found.'
    print(msg)
    return msg

