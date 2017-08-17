#!/usr/bin/env python

from sys import platform
import subprocess
from subprocess import Popen, PIPE

def platform_check():
    if platform == "linux" or platform == "linux2":
        print "Linux"
    elif platform == "darwin":
        print "OS X"
    elif platform == "win32":
        print "Windows"
    else:
        print "Unknown OS"

def call_shell():
    session = subprocess.Popen(['test.sh'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()

    if stderr:
        raise Exception("Error "+str(stderr))

def main():
    platform_check()
    call_shell()

if __name__ == "__main__":
    main()
