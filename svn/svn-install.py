#!/usr/bin/env python

from sys import platform

def platform_check():
    if platform == "linux" or platform == "linux2":
        print "Linux"
    elif platform == "darwin":
        print "OS X"
    elif platform == "win32":
        print "Windows"
    else:
        print "Unknown OS"


print "platform.linux_distribution()"

def main():
    platform_check()

if __name__ == "__main__":
    main()
