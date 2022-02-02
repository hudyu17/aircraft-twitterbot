import requests

def Route(callsign):
    origin_request = requests.get('https://api.joshdouch.me/callsign-origin_IATA.php?callsign={}'.format(callsign))
    dest_request = requests.get('https://api.joshdouch.me/callsign-des_IATA.php?callsign={}'.format(callsign))

    origin_iata = str(origin_request.content)[2:-1]
    dest_iata = str(dest_request.content)[2:-1]

    if origin_iata == 'n/a' or dest_iata == 'n/a':
        route = 'Flight ' + callsign

    else: 
        origin_name = str((requests.get('https://api.joshdouch.me/IATA-airport.php?iata={}'.format(origin_iata)).content))[2:-1]
        dest_name = str((requests.get('https://api.joshdouch.me/IATA-airport.php?iata={}'.format(dest_iata)).content))[2:-1]

        route = 'Flight ' + callsign + ' from ' + origin_name + ' (' + origin_iata + ') to ' + dest_name + ' (' + dest_iata + ')'

    return route