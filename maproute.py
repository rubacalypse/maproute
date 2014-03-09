import subprocess
from subprocess import Popen, PIPE 
from sys import argv


def main():
    dest = argv[1]
    print "host to traceroute is: %s" % dest
    args = ['traceroute', dest]
    print args
    process = subprocess.Popen(args, stdout=PIPE)
    print process
    (output, err) = process.communicate()
    rc = process.poll()
    print rc
    '''
        not sure if I should be dealing with an interrupted traceroute
        if rc < 0:
            print "traceroute terminated"
    '''
if __name__ == '__main__':
    main()
