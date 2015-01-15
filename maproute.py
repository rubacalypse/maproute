#!/usr/bin/python

from traceroute.util import perform_traceroute, parse_hops
from geo.util import ip_to_location, get_lat_long, airport_json_to_tuples, city_json_to_tuples, us_city_json_to_tuples, city_in_hop
from mapmaker.mapmaker import plot_lat_long
from sys import argv, path
from operator import itemgetter, attrgetter, methodcaller
from collections import namedtuple
from PIL import Image


#TODO: logging module, idiot
def main():
    dest = argv[1]
    hops = perform_traceroute(dest)
    
    ''' get traceroute text and IPs in tuples'''
    parsed_hops = parse_hops(hops[1:])
    
    ''' generate tuples from airport, world cities and us cities databases '''
    airport_tuples = airport_json_to_tuples()
    world_city_tuples = city_json_to_tuples()
    us_city_tuples = us_city_json_to_tuples()
    
    '''building plot point list'''
    plot_list = []
    plot_point = namedtuple('plot_point', ['ip', 'coords']) 
    for hop in parsed_hops:
      total = []
      '''check which cities show up in the hop text strings '''
      world = city_in_hop(hop.text, world_city_tuples, plot_list)
      us = city_in_hop(hop.text, us_city_tuples, plot_list)
      airport = city_in_hop(hop.text, airport_tuples, plot_list)
      total = world + us + airport
      if len(total) == 0:
        continue
      '''sort by length of city name
         correct match will most likely be the longest city '''
      sorted_results = sorted(total, key=lambda city: len(city[0]))
      city_to_plot = plot_point(ip=hop.ip, coords=sorted_results[-1])
      '''append correct city to plot point list'''
      plot_list.append(city_to_plot)



    '''plotting on map'''
    coords = [(hop.ip, get_lat_long(hop.coords)) for hop in plot_list]
    plot_lat_long(coords)
    

if __name__ == '__main__':
    main()

