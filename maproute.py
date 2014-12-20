import pygeoip
import geopy
from collections import namedtuple
from geopy.geocoders import Nominatim
from subprocess import check_output
from sys import argv


def main():
    dest = argv[1]
    hops = perform_traceroute(dest)
    ips = get_ips(hops[1:])
    locs = {ip: ip_to_location(ip) for ip in ips}
    coords = {ip: get_lat_lon(loc) for ip, loc in locs.items() if loc != ''}
    print ("locations: %s\t" % locs)
    print("coords: %s\t" % coords)


def perform_traceroute(dest):
    output = check_output("traceroute -m %d %s" % (20, dest), shell=True)
    hops = output.split("\n")
    return hops
#libaa libcaca geoip


def get_ips(lines):
    #get the IP from the traceroute hops
    ips = [line[line.find("(") + 1 : line.find(")")] for line in lines if "*"
        not in line and line != '']
    return ips


def ip_to_location(ip):
    #retrieve IP location information from local GeoLiteCity database
    gi = pygeoip.GeoIP("/Users/ruba/code/maproute/GeoLiteCity.dat")
    output = gi.record_by_addr(ip)
    geo = dict()
    #build the dictionary, make sure it doesn't include Nulls or empty strings
    if output is not None:
      if "city" in output and output['city'] != None and output['city'] != '':
            geo['city'] = output['city']
      if "region_code" in output and output['region_code'] != None and \
          output['region_code'] != '':
            geo['region'] = output['region_code']
      if "country_name" in output and output['country_name'] != None and \
        output['country_name'] != '':
            geo['country'] = output['country_name']
    return geo


def get_lat_lon(geo):
    geolocator = Nominatim()
    location = geolocator.geocode(geo, timeout=1000)
    if location is None:
      return
    coords = namedtuple('coords', ['lat', 'long'])
    c = coords(location.latitude, location.longitude)
    return c




if __name__ == '__main__':
    main()

