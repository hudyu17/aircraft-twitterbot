import requests
from staticmap import StaticMap, CircleMarker, IconMarker

def Map(states):
    lat = states[0][6]
    long = states[0][5]

    m = StaticMap(500, 500, url_template='http://a.tile.osm.org/{z}/{x}/{y}.png')

    marker = IconMarker((long - 2, lat + 2.22), './cathay-bot/cathay-logo.png', 2, 2)
    m.add_marker(marker)

    circle_marker = CircleMarker((long, lat), '#FFFFFF', 16)
    circle_outline = CircleMarker((long, lat), '#00645A', 20)
    m.add_marker(circle_outline)
    m.add_marker(circle_marker)

    image = m.render(zoom=4)
    return image