#!/usr/bin/python

from traceroute.util import perform_traceroute, get_ips
from geo.util import ip_to_location, get_lat_long
from sys import argv

def main():
    dest = argv[1]
    hops = perform_traceroute(dest)
    ips = get_ips(hops[1:])
    locs = {ip: ip_to_location(ip) for ip in ips}
    coords = {ip: get_lat_long(loc) for ip, loc in locs.items() if loc != ''}
    print ("locations: %s\t" % locs)
    print("coords: %s\t" % coords)


if __name__ == '__main__':
    main()

