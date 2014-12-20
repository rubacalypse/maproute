import pygeoip
import geopy
from collections import namedtuple
from geopy.geocoders import Nominatim


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


def get_lat_long(geo):
    geolocator = Nominatim()
    location = geolocator.geocode(geo, timeout=1000)
    if location is None:
      return
    coords = namedtuple('coords', ['lat', 'long'])
    c = coords(location.latitude, location.longitude)
    return c


