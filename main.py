import makeItTrack
import readNwrite
import threading

# every minute check tracking aircraft altitude
def main():
    inAir = makeItTrack.getInAir()
    trackingPlanes = readNwrite.readTrackingPlanes()
    makeItTrack.altCheck(inAir, trackingPlanes)
    readNwrite.writeTrackingPlanes(trackingPlanes)
    threading.Timer(10.0, main).start()




# if new msg in telegram - add a/c to trackingPlanes
def msgRecieved(reg):
    inAir = makeItTrack.getInAir()
    trackingPlanes = readNwrite.readTrackingPlanes()
    if makeItTrack.addPlaneToTrack(inAir, reg, trackingPlanes):
        sendMsg = f"a/c wit reg={reg} is tracking now. It is {inAir[reg]['type']}, callsign - {inAir[reg]['callsign']}"
        trackingPlanes[reg] = inAir[reg]
        readNwrite.writeTrackingPlanes(trackingPlanes)
        return sendMsg


print(main())
#main()
#{'6040': {'type': 'H60', 'callsign': 'No data', 'altitude': 'No data', 'Lat/Long': ['36.162827', '-76.00771']}, '1704': {'type': 'C130', 'callsign': 'C1704', 'altitude': '300', 'Lat/Long': ['26.895183', '-81.989012']}, '1372277': {'type': 'EC45', 'callsign': '01172277', 'altitude': '5400', 'Lat/Long': ['31.351536', '-110.218634']}, '2002': {'type': 'C30J', 'callsign': 'C2002', 'altitude': '1750', 'Lat/Long': ['34.331177', '-77.815321']}, '160984': {'type': 'BE9L', 'callsign': 'RFNK24', 'altitude': '2900', 'Lat/Long': ['27.883627', '-97.472922']}, '168980': {'type': 'B737', 'callsign': 'CNV6603', 'altitude': '20825', 'Lat/Long': ['38.842667', '-26.118144']}, '6596': {'type': 'AS65', 'callsign': 'C6596', 'altitude': '375', 'Lat/Long': ['25.902603', '-80.220043']}, 'B18912': {'type': 'A359', 'callsign': 'CAL024', 'altitude': '35000', 'Lat/Long': ['28.920822', '127.100408']}, 'CNAOI': {'type': 'C130', 'callsign': 'RMAF237', 'altitude': '13950', 'Lat/Long': ['26.983167', '-13.350185']}, '162668': {'type': 'B06', 'callsign': 'VV7E106', 'altitude': '500', 'Lat/Long': ['30.991196', '-86.486745']}, 'CCAWL': {'type': 'A20N', 'callsign': 'JAP7224', 'altitude': '35000', 'Lat/Long': ['-9.83972', '-78.18448']}, '1120381': {'type': 'H60', 'callsign': 'R20381', 'altitude': '2025', 'Lat/Long': ['34.838837', '-78.981498']}, 'C168': {'type': 'CL60', 'callsign': 'DAF2256', 'altitude': '28025', 'Lat/Long': ['64.642548', '-24.965771']}, 'CCAWE': {'type': 'A320', 'callsign': 'JAT658', 'altitude': '37975', 'Lat/Long': ['-20.559842', '-71.636602']}, '6514': {'type': 'AS65', 'callsign': 'C6514', 'altitude': '1900', 'Lat/Long': ['29.673886', '-95.088286']}, '2714': {'type': 'C27J', 'callsign': 'C2714', 'altitude': '21000', 'Lat/Long': ['26.98884', '-80.49334']}, 'PTMSP': {'type': 'C525', 'callsign': 'PPISO', 'altitude': '10000', 'Lat/Long': ['-21.689712', '-51.946818']}, '600343': {'type': 'K35R', 'callsign': 'No data', 'altitude': '25000', 'Lat/Long': ['33.79213', '42.103958']}, '000175': {'type': 'C17', 'callsign': 'RCH335', 'altitude': '25300', 'Lat/Long': ['41.013242', '-72.099405']}, '166714': {'type': 'C560', 'callsign': 'ATILA27', 'altitude': '18675', 'Lat/Long': ['25.664154', '51.41744']}, '119355': {'type': 'GLEX', 'callsign': 'No data', 'altitude': '32025', 'Lat/Long': ['35.655075', '42.176113']}, '8223835': {'type': 'DHC6', 'callsign': 'CONGO63', 'altitude': '6000', 'Lat/Long': ['38.968643', '-104.820198']}, '580122': {'type': 'K35R', 'callsign': 'WYLIE89', 'altitude': '475', 'Lat/Long': ['40.680535', '-89.726362']}, '973091': {'type': 'D328', 'callsign': 'No data', 'altitude': '26975', 'Lat/Long': ['20.614334', '-69.686672']}, '9800008': {'type': 'C560', 'callsign': 'PAT008', 'altitude': '40000', 'Lat/Long': ['40.016024', '-86.431129']}, '985308': {'type': 'C30J', 'callsign': 'TEAL81', 'altitude': '25000', 'Lat/Long': ['26.180839', '-81.633013']}, '080329': {'type': 'B350', 'callsign': 'SHADY06', 'altitude': '26000', 'Lat/Long': ['35.122227', '-88.213319']}, '130604': {'type': 'C30J', 'callsign': 'CFC2540', 'altitude': '29000', 'Lat/Long': ['47.105372', '-77.066838']}, '000178': {'type': 'C17', 'callsign': 'RCH825', 'altitude': '30000', 'Lat/Long': ['39.310357', '-90.703708']}, '840071': {'type': 'LJ35', 'callsign': 'COUGR61', 'altitude': '37950', 'Lat/Long': ['39.437576', '-95.114434']}, '2MUJJ': {'type': 'EA50', 'callsign': '2MUJJ', 'altitude': 'No data', 'Lat/Long': ['51.335598', '0.034388']}, '125756': {'type': 'C30J', 'callsign': 'RCH043', 'altitude': '26000', 'Lat/Long': ['43.077106', '10.016276']}, '074637': {'type': 'C30J', 'callsign': 'RCH160', 'altitude': '24000', 'Lat/Long': ['39.826883', '14.320557']}, '088601': {'type': 'C30J', 'callsign': 'HKY747', 'altitude': '26000', 'Lat/Long': ['49.39961', '15.362134']}, 'ST16': {'type': 'F260', 'callsign': 'BAF191', 'altitude': '1100', 'Lat/Long': ['50.488168', '4.109904']}, '115740': {'type': 'C30J', 'callsign': 'HKY740', 'altitude': '23000', 'Lat/Long': ['52.230363', '7.763581']}, '165858': {'type': 'C30J', 'callsign': 'LAWLS19', 'altitude': '21000', 'Lat/Long': ['34.061371', '40.616847']}, '018': {'type': 'C295', 'callsign': 'PLF042', 'altitude': '1000', 'Lat/Long': ['50.081143', '19.649464']}, 'EM003': {'type': 'S92', 'callsign': '@@@@@@@@', 'altitude': '1625', 'Lat/Long': ['52.265268', '-0.291111']}, '145791': {'type': 'C30J', 'callsign': 'RCH421', 'altitude': '25975', 'Lat/Long': ['41.808553', '10.955444']}, '100214': {'type': 'C17', 'callsign': 'RCH808', 'altitude': '26250', 'Lat/Long': ['36.476462', '-5.381017']}, '580125': {'type': 'K35R', 'callsign': 'HOBO11', 'altitude': '34000', 'Lat/Long': ['52.669947', '8.311785']}, '258': {'type': 'LJ45', 'callsign': 'IRL258', 'altitude': '23450', 'Lat/Long': ['51.925735', '-6.874161']}, '9100516': {'type': 'BE20', 'callsign': 'YANK03', 'altitude': '27975', 'Lat/Long': ['54.91274', '24.205128']}, '164441': {'type': 'C130', 'callsign': 'CNV3851', 'altitude': '4925', 'Lat/Long': ['37.365899', '14.543092']}, '147': {'type': 'TBM7', 'callsign': 'CTM1287', 'altitude': '29000', 'Lat/Long': ['38.353597', '23.816807']}, '947318': {'type': 'C130', 'callsign': 'RECH402', 'altitude': '23000', 'Lat/Long': ['45.001536', '1.711054']}, 'PA474': {'type': 'LANC', 'callsign': 'PA474', 'altitude': '1100', 'Lat/Long': ['52.000081', '-1.702256']}, '105700': {'type': 'C30J', 'callsign': 'RCH040', 'altitude': '1725', 'Lat/Long': ['49.441983', '7.683334']}, '2RBTS': {'type': 'C25B', 'callsign': 'ORT03B', 'altitude': '41000', 'Lat/Long': ['51.118919', '-2.964554']}, '2MINI': {'type': 'EA50', 'callsign': '2MINI', 'altitude': '25000', 'Lat/Long': ['54.853386', '-3.582458']}, '165856': {'type': 'C30J', 'callsign': 'HKY144', 'altitude': '23800', 'Lat/Long': ['50.316615', '18.938805']}, '580089': {'type': 'K35R', 'callsign': 'HOBO20', 'altitude': '38000', 'Lat/Long': ['52.450477', '12.064807']}, 'ZZ178': {'type': 'C17', 'callsign': 'RRR6629', 'altitude': '475', 'Lat/Long': ['54.661463', '-6.207775']}, '2801': {'type': 'A319', 'callsign': 'CEF589', 'altitude': '24000', 'Lat/Long': ['49.202736', '16.383579']}, '947310': {'type': 'C130', 'callsign': 'RCH302', 'altitude': '22900', 'Lat/Long': ['44.554728', '2.035485']}, '600023': {'type': 'B52', 'callsign': 'SPICY61', 'altitude': '23000', 'Lat/Long': ['51.383428', '2.526327']}, '605': {'type': 'A319', 'callsign': 'HUAF366', 'altitude': '36000', 'Lat/Long': ['50.966125', '22.394516']}, '043142': {'type': 'C30J', 'callsign': 'HKY163', 'altitude': '22000', 'Lat/Long': ['47.677395', '19.067401']}, 'ST25': {'type': 'F260', 'callsign': 'BAF192', 'altitude': '1300', 'Lat/Long': ['50.454289', '4.076362']}, '5704': {'type': 'D228', 'callsign': 'PCT401', 'altitude': '1950', 'Lat/Long': ['54.049476', '10.523852']}, '2DAVE': {'type': 'EA50', 'callsign': '2DAVE', 'altitude': '41000', 'Lat/Long': ['46.267524', '2.075867']}, 'MM62178': {'type': 'C30J', 'callsign': 'IAM4673', 'altitude': '14775', 'Lat/Long': ['44.305963', '10.567237']}, '064634': {'type': 'C30J', 'callsign': 'RCH044', 'altitude': '25975', 'Lat/Long': ['49.920029', '11.430383']}, '074636': {'type': 'C30J', 'callsign': 'RCH540', 'altitude': '3225', 'Lat/Long': ['49.461799', '7.869774']}, 'ZZ335': {'type': 'A332', 'callsign': 'RRR2300', 'altitude': '38000', 'Lat/Long': ['34.789465', '27.711868']}}