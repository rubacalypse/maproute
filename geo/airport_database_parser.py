from collections import namedtuple
import json
import pprint

def parse_airport_dataset():
  airport = namedtuple('airport', ['icao', 'iata', 'airport', 'city',
    'country', 'lat', 'lon'])
  vals = list()

  with open('GlobalAirportDatabase.txt', 'r') as f:
    for line in f:
      split = line.split(':')
      icao_v = split[0]
      iata_v = split[1]
      airport_v = split[2]
      #city_v = split[3].replace(" ", "").lower()
      city_v = split[3].lower()
      country_v = split[4].lower()
      lat_v = float(split[5]) + float(split[6])/60 + float(split[7])/3600
      lon_v = float(split[9]) + float(split[10])/60 + float(split[11])/3600
      tup = airport(icao=icao_v, iata=iata_v, airport=airport_v, city=city_v,
          country=country_v, lat=lat_v, lon=lon_v)
      vals.append(tup)
    return vals

def main():
  tuples = parse_airport_dataset()
  with open('airport_data.json', 'w') as f:
    json.dump(tuples, f)
    

if __name__ == '__main__':
  main() 
