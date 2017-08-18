#!/usr/bin/env python

from sys import platform
import subprocess
from subprocess import Popen, PIPE
import sys

def platform_check():
    if platform == "linux" or platform == "linux2":
        print "Linux"
    elif platform == "darwin":
        print "OS X"
    elif platform == "win32":
        print "Windows"
    else:
        print "Unknown OS"

def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"

print("""Python version: %s
dist: %s
linux_distribution: %s
system: %s
machine: %s
platform: %s
uname: %s
version: %s
mac_ver: %s
""" % (
sys.version.split('\n'),
str(platform.dist()),
linux_distribution(),
platform.system(),
platform.machine(),
platform.platform(),
platform.uname(),
platform.version(),
platform.mac_ver(),
))

def call_shell():
    session = subprocess.Popen(['syspack.sh'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()

    if stderr:
        raise Exception("Error "+str(stderr))

def main():
    platform_check()
    call_shell()
    linux_distribution()

if __name__ == "__main__":
    main()
