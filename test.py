
acList = []
# cdn_ships_info = sorted(cdn_ships_info, key=lambda x: int(x[3]))
trackingPlanes = {"624130": {"type": "R135", "callsign": "HUNTR56", "altitude": "1075", "Lat/Long": ["25.072337", "51.334914"], "status": "out-of-range", "chat_id": [659584153]}, "272": {"type": "B703", "callsign": "@@@@@@@@", "altitude": "29600", "Lat/Long": ["31.115744", "35.360825"], "status": "in air", "chat_id": [659584153]}, "950121": {"type": "B703", "callsign": "REDEYE6", "altitude": "32000", "Lat/Long": ["52.937117", "19.20442"], "status": "in air", "chat_id": [659584153]}}
for item in trackingPlanes.items():
    acList.append(list(item))
    print(list(item))

print(acList)
