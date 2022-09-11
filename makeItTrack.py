#altitude cheker and add plane to tracking aircraft functions
import readNwrite
import NowInAir


#inAir = {'08-6202': {'type': 'C30J', 'callsign': 'No data', 'altitude': '9150'}, '6593': {'type': 'AS65', 'callsign': 'C6593', 'altitude': '550'}, 'A40-024': {'type': 'NH90', 'callsign': 'BSMN81', 'altitude': '2025'}, 'A47-012': {'type': 'P8', 'callsign': 'BLKT02', 'altitude': '13000'}, 'CC-AWC': {'type': 'A320', 'callsign': 'JAT651', 'altitude': '34025'}, '555': {'type': 'A320', 'callsign': 'MJN575', 'altitude': '475'}, 'A40-020': {'type': 'NH90', 'callsign': 'DEST124', 'altitude': '-150'}, '1207': {'type': 'P180', 'callsign': 'YASAT10', 'altitude': '8400'}, 'A54-006': {'type': 'PC21', 'callsign': 'TANG22', 'altitude': '1475'}, 'N52-009': {'type': 'EC35', 'callsign': 'TAIP49', 'altitude': '1575'}, 'N52-013': {'type': 'EC45', 'callsign': 'TAIP53', 'altitude': '975'}, '1208': {'type': 'P180', 'callsign': 'YASAT09', 'altitude': '10375'}, 'A40-008': {'type': 'NH90', 'callsign': 'BSMN82', 'altitude': '1525'}, 'A54-001': {'type': 'PC21', 'callsign': 'VIPR05', 'altitude': '20975'}, '165834': {'type': 'B737', 'callsign': 'CNV7014', 'altitude': '5175'}, 'A27-21': {'type': 'HAWK', 'callsign': 'PHNX11', 'altitude': '8425'}, '166695': {'type': 'B737', 'callsign': 'CNV7015', 'altitude': '37000'}, '1216': {'type': 'C130', 'callsign': 'NAJIM309', 'altitude': '8300'}, 'A54-010': {'type': 'PC21', 'callsign': 'VIPR42', 'altitude': '25'}, 'A54-018': {'type': 'PC21', 'callsign': 'TANG01', 'altitude': '-100'}, 'A54-030': {'type': 'PC21', 'callsign': 'ALDN76', 'altitude': '5850'}, 'A56-002': {'type': 'FA7X', 'callsign': 'EVY84', 'altitude': '22450'}, 'A54-014': {'type': 'PC21', 'callsign': 'SBOT2', 'altitude': '5550'}, 'A54-003': {'type': 'PC21', 'callsign': 'VANT', 'altitude': '5500'}, '07-7170': {'type': 'C17', 'callsign': 'RCH342', 'altitude': '31000'}, '63-7991': {'type': 'K35R', 'callsign': 'No data', 'altitude': '28000'}, 'A54-044': {'type': 'PC21', 'callsign': 'ALDN51', 'altitude': '775'}, 'A47-008': {'type': 'P8', 'callsign': 'BLKT03', 'altitude': '26000'}, 'A54-029': {'type': 'PC21', 'callsign': 'ROLR31', 'altitude': '275'}, '163562': {'type': 'BE20', 'callsign': 'BLCAT62', 'altitude': '16625'}, 'A39-005': {'type': 'A332', 'callsign': 'XA685', 'altitude': '39004'}, '163839': {'type': 'BE20', 'callsign': 'CNV510', 'altitude': '16000'}, 'A54-031': {'type': 'PC21', 'callsign': 'ROLR29', 'altitude': '2625'}, 'A54-035': {'type': 'PC21', 'callsign': 'ALDN53', 'altitude': '1225'}, '168209': {'type': 'B350', 'callsign': 'TORI209', 'altitude': '23000'}, '03-3120': {'type': 'C17', 'callsign': 'RCH218', 'altitude': '35000'}, '06-6167': {'type': 'C17', 'callsign': 'MOOSE95', 'altitude': '23000'}, 'A39-007': {'type': 'A332', 'callsign': 'DRGN01', 'altitude': '26025'}, 'N52-003': {'type': 'EC35', 'callsign': 'TAIP43', 'altitude': '2250'}, 'A47-009': {'type': 'P8', 'callsign': 'BLKT01', 'altitude': '15000'}, '166375': {'type': 'GLF5', 'callsign': 'VV375', 'altitude': '24850'}, 'T-332': {'type': 'AS32', 'callsign': 'T332', 'altitude': '2325'}, 'G-10': {'type': 'EXPL', 'callsign': 'G10', 'altitude': '400'}, '96-00107': {'type': 'C560', 'callsign': 'POKER44', 'altitude': '36000'}, 'PI-06': {'type': 'PC12', 'callsign': 'T26', 'altitude': '18075'}, '104': {'type': 'TBM7', 'callsign': 'CTM3884', 'altitude': '24000'}, '71-01468': {'type': 'C130', 'callsign': 'ALEV41', 'altitude': '25000'}, '07-7178': {'type': 'C17', 'callsign': 'BNDG150', 'altitude': '29100'}, '0214': {'type': 'M28', 'callsign': 'PLF244', 'altitude': '10300'}, 'CC-2': {'type': 'C295', 'callsign': 'N21', 'altitude': '20575'}, '62-4134': {'type': 'R135', 'callsign': 'JAKE11', 'altitude': 'No data'}, '63-8888': {'type': 'K35R', 'callsign': 'No data', 'altitude': 'No data'}, '15-20754': {'type': 'H60', 'callsign': 'DUKE45', 'altitude': '2425'}, '08-8203': {'type': 'C17', 'callsign': 'RCH816', 'altitude': '31000'}, '61-0310': {'type': 'K35R', 'callsign': 'RCH695', 'altitude': '33475'}, '7T-VPC': {'type': 'GLF4', 'callsign': 'Q7TVPC', 'altitude': '40000'}, '88-00325': {'type': 'BE20', 'callsign': 'YANK02', 'altitude': '26975'}, '91-00516': {'type': 'BE20', 'callsign': 'YANK01', 'altitude': '27975'}, '59-1464': {'type': 'K35R', 'callsign': 'CASA20', 'altitude': '28000'}}
#reg = '6593'

def getInAir():
    inAir = NowInAir.allAcInAir()
    return inAir

def addPlaneToTrack(inAir, reg, trackingPlanes):
    print('addPlaneToTrack started')
    print(inAir.keys())
    print(reg)
    if reg in trackingPlanes.keys():
        print('Already tracking')
        return False
    elif reg in inAir.keys():
        print('Will track this Plane')
        trackingPlanes[reg] = inAir[reg]
        print(trackingPlanes)
        return trackingPlanes
    else:
        print("can't find a/c in air wit reg =", reg)
        return False

def landingNotif(planeReg, inAir):
    msg = f'alert! Plane with reg={planeReg} is landing. Current altitude is {inAir[planeReg]["altitude"]} feet'
    print(msg)

# Check altitude of tracking a/c
# if alt < 1000m and 'alt now' < 'alt before' on more then 3m
#   then notify and delete plane from tracking
# if a/c is out of range then print it
# 3280 (ft) = 1000m
# input - a/c in air and tracking planes
# output - updated tracking plane dict
def altCheck(inAir, trackingPlanes):
    print('altCheck started')
    delList = [] # list to write landed planes because u can't change dict size in loop
    for planeReg in trackingPlanes.keys():
        if planeReg in inAir.keys():
            if (int(inAir[planeReg]['altitude']) < 3280) and (int(trackingPlanes[planeReg]['altitude']) - int(inAir[planeReg]['altitude']) >= 10) and (int(trackingPlanes[planeReg]['altitude']) >= int(inAir[planeReg]['altitude'])):
                landingNotif(planeReg, inAir)
                delList.append(planeReg)
            else:
                trackingPlanes[planeReg] = inAir[planeReg]
        else:
            print(f'a/c wit reg={planeReg} is Out-of-Range now')
    [trackingPlanes.pop(key) for key in delList]
    print('altCheck finished, tracking planes=', trackingPlanes)
    return trackingPlanes

# load tracking planes from file, check alt and write updated dict
def altCheckRnW():
    inAir = getInAir()
    trackingPlanes = readNwrite.readTrackingPlanes()
    altCheck(inAir, trackingPlanes)
    readNwrite.writeTrackingPlanes(trackingPlanes)

# if new msg in telegram - add a/c to trackingPlanes
def regCheck(reg):
    inAir = getInAir()
    trackingPlanes = readNwrite.readTrackingPlanes()
    if addPlaneToTrack(inAir, reg, trackingPlanes):
        sendMsg = f"a/c wit reg={reg} is tracking now. It is {inAir[reg]['type']}, callsign - {inAir[reg]['callsign']}"
        trackingPlanes[reg] = inAir[reg]
        readNwrite.writeTrackingPlanes(trackingPlanes)
        return sendMsg
#addPlaneToTrack(inAir, reg, trackingPlanes)
#addPlaneToTrack(inAir, '08-6202', trackingPlanes)
#print(trackingPlanes)
#altCheck(inAir, trackingPlanes)
#print(trackingPlanes)