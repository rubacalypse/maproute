from subprocess import call, check_output, CalledProcessError
from sys import argv


def main():
    arg = argv[1]
    perform_traceroute(arg)


def perform_traceroute(arg):
    output = check_output("traceroute %s" % arg, shell=True)
    routes = output.split("\n")
    print routes[1:]

if __name__ == '__main__':
    main()
