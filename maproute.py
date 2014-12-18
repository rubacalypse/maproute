import pygeoip
import geopy
from geopy.geocoders import Nominatim
from subprocess import check_output
from sys import argv


def main():
    dest = argv[1]
    print dest
    hops = perform_traceroute(dest)
    ips = get_ips(hops[1:])
    locs = [ip_to_location(ip) for ip in ips]
    coords = [get_lat_lon(loc) for loc in locs if loc != '']

def get_lat_lon(geo):
    geolocator = Nominatim()
    location = geolocator.geocode(geo, timeout=1000)
    if location is None:
      return
    coords = dict()
    coords['ip'] = geo['ip']
    coords['lat'] = location.latitude
    coords['lon'] = location.longitude
    return coords 

def perform_traceroute(dest):
    output = check_output("traceroute -m %d %s" % (20, dest), shell=True)
    hops = output.split("\n")
    return hops
#libaa libcaca geoip


def get_ips(lines):
    ips = [line[line.find("(") + 1 : line.find(")")] for line in lines if "*"
        not in line and line != '']
    return ips


def ip_to_location(ip):
    gi = pygeoip.GeoIP("/Users/ruba/code/maproute/GeoLiteCity.dat")
    output = gi.record_by_addr(ip)
    geo = dict()
    if output is not None:
      if "city" in output and output['city'] != None and output['city'] != '':
            geo['city'] = output['city']
      if "region_code" in output and output['region_code'] != None and \
          output['region_code'] != '':
            geo['region'] = output['region_code']
      if "country_name" in output and output['country_name'] != None and \
        output['country_name'] != '':
            geo['country'] = output['country_name']
      geo['ip'] = ip
    return geo


if __name__ == '__main__':
    main()

