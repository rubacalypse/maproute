from bs4 import BeautifulSoup
from collections import namedtuple
import json


def main():
  loc = namedtuple('loc', ['city', 'other_name', 'country'])
  soup = BeautifulSoup(open('citycountry.html'))
  table = soup.find('table')
  rows = table.findChildren('tr')
  city = []
  for row in rows:
    cells = row.findChildren('td')
    city.append(cells[0])


  citycountry_str = [str(c) for c in city]
  clean_str = [c.replace('<td>', '').replace('</td>', '') for c in
      citycountry_str]

  loc_tuples = []
  for s in clean_str:
    split = s.split(',')
    if '(' in split[0]:
      to_remove = split[0][split[0].index('('):split[0].index(')')+1]
      other = split[0][split[0].index('(')+1:split[0].index(')')]
      split[0] = split[0].replace('(', '').replace(other, '').replace(')','')
    else:
      other = ''
    
    loc_tuple = loc(city=split[0].lower(), other_name=other, country=split[1].lower())
    loc_tuples.append(loc_tuple)


  with open('cities.json', 'w') as f:
    json.dump(loc_tuples, f)



if __name__ == '__main__':
  main()
