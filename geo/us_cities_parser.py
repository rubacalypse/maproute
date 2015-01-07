import json
from collections import namedtuple

def main():
  city = namedtuple('uscity', ['city', 'state']) 
  cities = []
  with open('us_cities.csv') as f:
    for line in f:
      split = line.split(',')
      print split
      #print "split 1: %s\t split 2: %s\t" % (split[0], split[1])
      #city_str = split[0].replace(' ', '').lower()
      #state_str = split[1].replace(' ', '').lower()
      city_str = split[0].lower()
      state_str = split[1].lower()
      print city_str
      print state_str
      #city_state = city(city=split[0].replace(' ','').lower(), state=split[1].replace(' ', '').lower())
      city_state = city(city=split[0].lower(), state=split[1].lower())
      cities.append(city_state)


  with open('us_cities.json', 'w') as j:
    json.dump(cities, j)
  
if __name__ == '__main__':
  main()
