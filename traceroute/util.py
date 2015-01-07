from subprocess import check_output
from collections import namedtuple
import re

def perform_traceroute(dest):
    output = check_output("traceroute -m %d %s" % (22, dest), shell=True)
    hops = output.split("\n")
#    print hops
    return hops
#libaa libcaca geoip


def parse_hops(lines):
  hops = []
  hop = namedtuple('hop', ['ip', 'text'])
  for line in lines:
    text_str = re.sub("[\W\d]+", "", line.strip()).lower()
    if "*" not in line and line != '':
      ip_str = line[line.find("(") + 1 : line.find(")")]  
    else:
      ip_str = ''
    new = hop(ip=ip_str, text=text_str)
    hops.append(new)

  return hops


def get_ips(lines):
    #get the IP from the traceroute hops
    ips = [line[line.find("(") + 1 : line.find(")")] for line in lines if "*"
        not in line and line != '']
    return ips


def get_hop_text(lines):
  text = [re.sub("[\W\d]+", "_", line.strip()).lower() for line in lines]
  return text
