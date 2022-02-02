import requests
import defMap
import defRoute
import parse
import os
from dotenv import load_dotenv, find_dotenv
from config import create_api

load_dotenv(find_dotenv())

def makeTweets(airborne_list, api):
    for aircraft in airborne_list:
        try:
            media = api.media_upload('cathay-bot/images/working-img-{}.png'.format(aircraft[1]))
            api.update_status(status = aircraft[0], media_ids = [media.media_id])
            print("Tweet posted")
        except Exception as e:
            print(e)

def main():
    api = create_api()
    username = os.getenv('osky_user')
    pword = os.getenv('osky_pass')
    aircraft_list = parse.createList()
    # aircraft_list = ['3c65cf']
    airborne_list = []
    for i in range(len(aircraft_list)):
        response = requests.get('https://{}:{}@opensky-network.org/api/states/all?icao24={}'.format(username, pword, aircraft_list[i])).json()
        if response['states'] and response['states'][0][5] and response['states'][0][6]:
            callsign = str(response['states'][0][1]).strip()
            # print(callsign)
            message = defRoute.Route(callsign)
            image = defMap.Map(response['states'])
            image.save('cathay-bot/images/working-img-{}.png'.format(i))
            airborne_list.append((message, i))
        else:
            print(' no state')
    # print(airborne_list)
    makeTweets(airborne_list, api)

# if __name__ == "__main__":
#     main()