import pandas as pd

def createList():
    df = pd.read_csv('cathay-icao.csv')
    aircraft_list = df['icao24'].tolist()

    return aircraft_list

