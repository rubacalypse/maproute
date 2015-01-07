#!/usr/bin/python

from traceroute.util import perform_traceroute, get_ips, get_hop_text, parse_hops
from geo.util import ip_to_location, get_lat_long, airport_json_to_tuples, city_json_to_tuples, us_city_json_to_tuples, city_in_hop
from mapmaker.mapmaker import plot_lat_long
from sys import argv, path
from operator import itemgetter, attrgetter, methodcaller
from collections import namedtuple

def main():
    dest = argv[1]
    hops = perform_traceroute(dest)
    hop_text = get_hop_text(hops)
    ips = get_ips(hops[1:])
    locs = {ip: ip_to_location(ip) for ip in ips}
    parsed_hops = parse_hops(hops[1:])
    airport_tuples = airport_json_to_tuples()
    world_city_tuples = city_json_to_tuples()
    us_city_tuples = us_city_json_to_tuples()
    
    ''' debug printing
    print "actual traceroute: %s\t\t" % hops
    print "hop text: %s\t" % hop_text
    print "actual traceroute: %s\t\t" % hops
    print "actual traceroute: %s\t\t" % hops
    print "parsed_hops: %s\t\t" % parsed_hops
    print "hop text: %s\t" % hop_text
    print "ips: %s\t" % ips
    ip_locs = zip(ips, hop_text)
    print "ip to loc: %s\t\t\t" % ip_locs
    '''

    plot_list = []
    plot_point = namedtuple('plot_point', ['ip', 'coords']) 
    for hop in parsed_hops:
      total = []
      #print hop
      world = city_in_hop(hop.text, world_city_tuples)
      us = city_in_hop(hop.text, us_city_tuples)
      airport = city_in_hop(hop.text, airport_tuples)
      ''' more debug printing
      #print "world: %s\n\nus: %s\n\nairport: %s\n" % (world, us, airport)
      #print "world len: %d\nus len: %d\nairport len: %d\n" % (len(world), len(us), len(airport))
      '''
      total = world + us + airport
      if len(total) == 0:
        continue
      sorted_results = sorted(total, key=lambda city: len(city[0]))
      #print "total: %s\nlen total: %d\nsorted: %s\n" % (total, len(total), sorted_results)
      city_to_plot = plot_point(ip=hop.ip, coords=sorted_results[-1])
      plot_list.append(city_to_plot)

    '''plotting'''
    coords = {hop.ip: get_lat_long(hop.coords) for hop in plot_list}
    print coords 
    for coord in coords.items():
      if coord[1] != None:
        plot_lat_long(coord)


if __name__ == '__main__':
    main()

