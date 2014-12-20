from subprocess import check_output


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

