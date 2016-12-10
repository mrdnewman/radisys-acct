#!/usr/bin/env python

import os
import sys
import statvfs
from time import sleep
import platform
import commands
import subprocess



os.system('clear')

get_os = platform.linux_distribution()[0]
get_ver = platform.linux_distribution()[1]
get_arch = platform.processor()
#get_arch = commands.getoutput("uname -m")
get_cpu = int(commands.getoutput("nproc"))
get_free_space = int(commands.getoutput("df -k / | awk '{ print $4 }' | tail -1"))

sup_arch = 'x86_64'
sup_os = 'Ubuntu'
sup_ver = '14.04'
sup_cpu = int(12)
sup_free_space = int(1073741824)
min_disk_size = '1TB'


def get_capacity():

    def getDfDescription():
        df = os.popen("df -h /")
        i = 0
        while True:
            i = i + 1
            line = df.readline()
            if i == 1:
                return (line.split()[0:6])
    def getDf():
        df = os.popen("df -h /")
        i = 0
        while True:
            i = i + 1
            line = df.readline()
            if i == 2:
                return (line.split()[0:6])

    # Disk information
    description = getDfDescription()
    disk_root = getDf()

    df_index = [0, 3]
    for x in df_index:
        print(description[x] + " : " + disk_root[x])


def chk_sys_posture():
    welcome = "\nRadisy Corp.\nWelcome To Head Node Setup\nAn RCORD-1.0 Product\n"
    print '\n'.join('{:^95}'.format(s) for s in welcome.split('\n')); sleep(3)

    print "Checking System Posture...\n"; sleep(3)
    if platform.system() == 'Linux':
        if sup_os != get_os:
            print 'Cannot continue -- OS must be \"Ubuntu\"...\n'; sleep(3)
            platform_info()
            raise SystemExit
        else:
            print 'Platform: Linux  \t[OK]'; sleep(1)
            print 'Distro: Ubuntu \t\t[OK]'; sleep(1)
            if sup_ver != get_ver:
                print '\nFor best perfomance: Recommend using version %s or higher...' % sup_ver; sleep(1)
            else:
                print 'Version: %s \t\t[OK]' % sup_ver; sleep(1)

            if sup_arch != get_arch:
                print '\nFor best performance: Recommend using 64bit Operating System.'
                print 'Current System Architecture: %s' % get_arch; sleep(1)
            else:
                print 'Arch: 64bit \t\t[OK]'; sleep(1)

            if  get_cpu < sup_cpu :
                print '\nFor best performance: A minimum of [12] CPU Cores needed. '
                print 'You only have [%s]...' % get_cpu; sleep(1)
            else:
                print 'CPU Cores [%s] \t\t[OK]' % get_cpu; sleep(1)

            if   get_free_space < sup_free_space :
                print '\nInstall may fail: A minimum of [%s] of free disk recommended...' % min_disk_size
                print 'Current Diposition:\n'
                get_capacity(); sleep(1)
            else:
                print '\nFree Disk Space \t[OK]'; get_capacity(); sleep(1)
    else:
        print 'Cannot continue -- Linux Platform required...\n'
        raise SystemExit


def platform_info():

    print """
     Current System:
     ---------------
     Distro: %s
     Version: %s
     Arch: %s
     """ % (
        get_os,
        get_ver,
        get_arch)

    print """
     Recommended System:
     -------------------
     Distro: %s
     Version: %s
     Arch: %s
     """ % (
        sup_os,
        sup_ver,
        sup_arch)


if __name__=='__main__':
    chk_sys_posture()