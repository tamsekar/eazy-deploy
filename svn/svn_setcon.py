#! /usr/bin/env python

from __future__ import print_function
from collections import OrderedDict
from collections import namedtuple
import pwd
import glob
import re
import sys
import platform
import os
import pprint
import pdb
# pdb.set_trace()


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


def cpuinfo():
    ''' Return the information in /proc/cpuinfo
    as a dictionary in the following format:
    cpu_info['proc0']={...}
    cpu_info['proc1']={...}

    '''

    cpuinfo=OrderedDict()
    procinfo=OrderedDict()

    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                # end of one processor
                cpuinfo['proc%s' % nprocs] = procinfo
                nprocs=nprocs+1
                # Reset
                procinfo=OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''

    return cpuinfo

def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    meminfo=OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo


def netdevs():
    ''' RX and TX bytes for each of the network devices '''

    with open('/proc/net/dev') as f:
        net_dump = f.readlines()

    device_data={}
    data = namedtuple('data',['rx','tx'])
    for line in net_dump[2:]:
        line = line.split(':')
        if line[0].strip() != 'lo':
            device_data[line[0].strip()] = data(float(line[1].split()[0])/(1024.0*1024.0),
                                                float(line[1].split()[8])/(1024.0*1024.0))

    return device_data

def process_list():

    pids = []
    for subdir in os.listdir('/proc'):
        if subdir.isdigit():
            pids.append(subdir)

    return pids

dev_pattern = ['sd.*','mmcblk*']

def size(device):
    nr_sectors = open(device+'/size').read().rstrip('\n')
    sect_size = open(device+'/queue/hw_sector_size').read().rstrip('\n')

    # The sect_size is in bytes, so we convert it to GiB and then send it back
    return (float(nr_sectors)*float(sect_size))/(1024.0*1024.0*1024.0)

def detect_devs():
    for device in glob.glob('/sys/block/*'):
        for pattern in dev_pattern:
            if re.compile(pattern).match(os.path.basename(device)):
                print('Device:: {0}, Size:: {1} GiB'.format(device, size(device)))


def getusers():
    users = pwd.getpwall()
    for user in users:
        print('{0}:{1}'.format(user.pw_name, user.pw_shell))

def sysstat():
    cpuinfo()

def main():
    dist()
    detect_devs()
    #getusers()

if __name__ == "__main__":
    main()
    cpuinfo()
    cpuinfo = cpuinfo()
    for processor in cpuinfo.keys():
        print ("""
        CPU: %s
        """ % (cpuinfo[processor]['model name']))
    meminfo = meminfo()
    print (bcolors.OKGREEN + "Memory" + bcolors.ENDC)
    print('Total memory: {0}'.format(meminfo['MemTotal']))
    print('Free memory: {0}'.format(meminfo['MemFree']))
    netdevs = netdevs()
    for dev in netdevs.keys():
        print (bcolors.OKGREEN + "Network" + bcolors.ENDC)
        print('{0}: {1} MiB {2} MiB'.format(dev, netdevs[dev].rx, netdevs[dev].tx))
    pids = process_list()
    print (bcolors.OKGREEN + "Processes" + bcolors.ENDC)
    print('Total number of running processes:: {0}'.format(len(pids)))
