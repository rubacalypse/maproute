import pygeoip
import geopy
from collections import namedtuple
from geopy.geocoders import Nominatim
import json
import os, sys
import pprint


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
    print geo
    geo_dict = dict()
    geo_dict['city'] = geo.city
    if geo.city is 'new york':
      geo_dict['city'] = 'New York City'
    if geo.city is 'london':
      geo_dict['city'] = 'London'
    if geo.state is not None:
      geo_dict['state'] = geo.state
    geo_dict['country'] = geo.country
    if geo.country == 'england':
      geo_dict['country'] = 'United Kingdom'
    geolocator = Nominatim()
    location = geolocator.geocode(geo_dict, timeout=1000)
    if location is None:
      return
    coords = namedtuple('coords', ['lat', 'long'])
    c = coords(location.latitude, location.longitude)
    return c

def airport_json_to_tuples():
  airport = namedtuple('airport', ['city', 'state', 'country'])
  with open('airport_data.json') as airport_data:
    airport_json = json.load(airport_data)
    tuples = [airport(city=item[3], state=None, country=item[4]) for item in airport_json]
    return tuples

def city_json_to_tuples():
  city = namedtuple('city', ['city', 'state', 'country'])
  with open('cities.json') as cities:
    cities_json = json.load(cities)
    tuples = [city(city=item[0], state=None, country=item[2]) for item in cities_json]
    return tuples

def us_city_json_to_tuples():
  uscity = namedtuple('uscity', ['city', 'state', 'country'])
  with open('us_cities.json') as us_cities:
    cities_json = json.load(us_cities)
    tuples = [uscity(city=item[0], state=item[1], country='usa') for item in cities_json]
    return tuples

def city_in_hop(hop, city_tuples, plot_points):
  correct = [] 
  for tup in city_tuples:
    city = tup.city.replace(' ','')
    if city in hop and len(tup.city) > 3:
        correct.append(tup)
  return correct
