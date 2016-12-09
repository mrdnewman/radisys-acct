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
get_cpu = int(commands.getoutput("nproc"))
get_free_space = int(commands.getoutput("df -k / | awk '{ print $4 }' | tail -1"))

sup_arch = 'x86_64'
sup_os = 'Ubuntu'
sup_ver = '14.04'
sup_cpu = int(12)
sup_kilo_cap = int(1288490188)
min_disk_size = '1.2T'


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
            print 'Platform: Linux -- OK'; sleep(1)
            print 'Distro: Ubuntu -- OK'; sleep(1)
            if sup_ver != get_ver:
                print 'Highly Recommend: Using Ubuntu version %s' % sup_ver; sleep(1)
            else:
                print 'Ubuntu version: %s -- OK' % sup_ver; sleep(1)

            if sup_arch != get_arch:
                print 'Highly Recommend: Using a 64bit OS'; sleep(1)
            else:
                print 'Arch: 64bit -- OK'; sleep(1)

            if  get_cpu < sup_cpu :
                print 'Highly Recommend +12 CPU Cores: You only have %s' % get_cpu; sleep(1)
            else:
                print 'CPU Cores %s -- OK' % get_cpu; sleep(1)

            if   get_free_space < sup_kilo_cap :
                print 'Low Disk Capcity: Minimum Free Space Should Be %s' % min_disk_size
                sleep(1); get_capacity()
            else:
                print 'Free Space -- OK'; sleep(1); get_capacity()
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