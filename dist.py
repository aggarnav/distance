
from math import atan2, cos, sin, sqrt, radians
import re



def calc_distance(origin, destination, planet):
    """great-circle distance between two points on a sphere
       from their longitudes and latitudes"""
    lat1, lon1 = origin
    lat2, lon2 = destination
    if planet.lower()=="earth".lower():
        radius = 6371  # km. earth
    if planet.lower()=="mars".lower():
        radius = 3390 #radius of mars
    if planet.lower()=="moon".lower():
        radius = 1737 #radius of moon

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (sin(dlat / 2) * sin(dlat / 2) + cos(radians(lat1)) * cos(radians(lat2)) *
         sin(dlon / 2) * sin(dlon / 2))
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = radius * c

    return d



xmlfile = open('placemarks.xml','r')
contents = xmlfile.readlines()

nodes = {}
i=0

for content in contents:
    lon = re.findall(r'<longitude>(.+?)</longitude>', content)
    lat = re.findall(r'<latitude>(.+?)</latitude>', content)
    nodes[i] = (float(lat[0]), float(lon[0]))
    i += 1

while True:
    n1 = int(input("Enter the number of the first POI: "))
    planet = (contents[n1].split("@"))[0]
    n2 = int(input("Enter the number of the Second POI: "))
    print ("distance of" + str(nodes[n1]) + "from" + str(nodes[n2]) + "is " + str(calc_distance(nodes[n1], nodes[n2],planet)))
