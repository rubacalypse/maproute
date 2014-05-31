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
    geo = [ip_to_location(ip) for ip in ips]
    print geo
#libaa libcaca geoip


def get_ips(lines):
    hops = [line.split()[2] for line in lines if line != '']
    ips = [hop.strip("()") for hop in hops if hop != '*']
    return ips


def ip_to_location(ip):
    gi = pygeoip.GeoIP("/usr/share/GeoIP/GeoLiteCity.dat")
    output = gi.record_by_addr(ip)
    city, region, country = "", "", ""
    print type(output)
    if output is not None:
        if "city" in output:
            city = output['city']
        if "region_code" in output:
            region = output['region_code']
        if "country_name" in output:
            country = output['country_name']
    return city, region, country


if __name__ == '__main__':
    main()

