#! /usr/bin/env python

from __future__ import print_function
from collections import OrderedDict
import sys
import platform
import os
import pprint


# Color Formatting

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print (bcolors.HEADER + "OS Information" + bcolors.ENDC)



def dist():
    print("""
    System: %s
    Node Name: %s
    Release: %s
    Version: %s
    Machine: %s
    Architecture: %s
    Distribution: %s
    """ % (
    platform.uname()[0],
    platform.uname()[1],
    platform.release(),
    platform.uname()[3],
    platform.uname()[4],
    platform.architecture()[0],
    platform.linux_distribution()[0],
    ))


def main():
    dist()

if __name__ == "__main__":
    main()
