from subprocess import call
from sys import argv


def main():
    dest = argv[1]
    print "host to traceroute is: %s" % dest
    call(["traceroute", dest])

if __name__ == '__main__':
    main()
