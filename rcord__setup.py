#!/usr/bin/env python

import os
import platform
import commands
from time import sleep

os.system('clear')


kern_rel = commands.getoutput("uname -r | cut -c1-5")
get_os = platform.linux_distribution()[0]
get_ver = platform.linux_distribution()[1]
get_arch = platform.processor()
get_cpu = int(commands.getoutput("nproc"))
get_free_space = int(commands.getoutput("df -k / | awk '{ print $4 }' | tail -1"))
get_cpu_virt = int(commands.getoutput("egrep -c '(vmx|svm)' /proc/cpuinfo"))

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
        print 'Platform: Linux \t\t\t[OK]'; sleep(1)
    else:
        print 'Cannot continue -- Linux Platform required...\n'
        raise SystemExit

    if get_os == 'Ubuntu':
        if get_ver == "14.04":
            print 'OS Type: Ubuntu \t\t\t[OK]'; sleep(1)
            print 'OS Version: 14.04 \t\t\t[OK]'; sleep(1)
        else:
            print '\nTo avoid install issues: Recommend using Ubuntu 14.04 Trusty.'
            print '\nCurrent OS version: %s\n' % get_ver
    else:
        print 'Cannot continue -- Operating System must be Ubuntu!'
        raise SystemExit

    if kern_rel > "3.10.0":
        print 'Kernel Rel: %s \t\t\t[OK]' % kern_rel; sleep(1)
    else:
        print 'Cannot continue -- Kernel version too low!'
        raise SystemExit

    if get_arch == "x86_64":
        print 'Arch: 64bit \t\t\t\t[OK]'; sleep(1)
    else:
        print '\nFor best performance: Recommend using 64bit Operating System.'
        print 'Current System Architecture: %s\n' % get_arch; sleep(1)

    if get_cpu < sup_cpu:
        print '\nFor best performance: A minimum of [12] CPU Cores needed. '
        print 'You only have [%s]...\n' % get_cpu; sleep(1)
    else:
        print 'CPU Cores [%s] \t\t\t\t[OK]' % get_cpu; sleep(1)

    if get_cpu_virt != 0:
        print "CPU Virtual Extensions: Present \t[OK]"; sleep(1)
    else:
        print 'Install may fail: To run KVM, a processor that supports hardware virtualization is needed.'
        print 'Try enabling virtual support within the BIOS...'; sleep(1)

    if get_free_space < sup_free_space:
        print '\nInstall may fail: A minimum of [%s] of free disk recommended...' % min_disk_size
        get_capacity(); sleep(3)
    else:
        print '\nFree Disk \t\t\t\t[OK]'; get_capacity(); sleep(3)


if __name__ == '__main__':
    chk_sys_posture()


