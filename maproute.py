import pygeoip
from subprocess import check_output
from sys import argv


def main():
    arg = argv[1]
    perform_traceroute(arg)


def perform_traceroute(arg):
    output = check_output("traceroute %s" % arg, shell=True)
    hops = output.split("\n")
    ips = get_ips(hops[1:])
    print ips
    geo = []
    for hop in hops[1:]:
        geo.append(hop)
    #print geo
    #print "\n".join(hops[1:])
#libaa libcaca geoip


def get_ips(hops):
    ips = [(hop.split())[2] for hop in hops if hop != '' and hop != '*']
    print ips
    return ips


def ip_to_location(ip):
    gi = pygeoip.GeoIP("/usr/share/GeoIP/GeoLiteCity.dat")
    output = gi.record_by_addr(ip)
    city = output['city']
    region = output['region_code']
    country = output['country_name']
    return city, region, country


if __name__ == '__main__':
    main()

