#!/usr/bin/env python

import os
import platform
import commands
import subprocess
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
        print '\nWARNING: Potential Performance Issues!'
        print 'Recommend using 64bit Operating System.'
        print 'Current System Architecture: %s\n' % get_arch; sleep(1)

    if get_cpu < sup_cpu:
        print '\nWARNING: Potential Peformance Issues!'
        print 'A minimum of [12] CPU Cores needed. '
        print 'You only have [%s]...\n' % get_cpu; sleep(1)
    else:
        print 'CPU Cores [%s] \t\t\t[OK]' % get_cpu; sleep(1)

    if get_cpu_virt != 0:
        print "CPU Virtual Extensions: Present \t[OK]"; sleep(1)
    else:
        print 'WARNING: Install May Fail!'
        print 'KVM needs a processor that supports hardware virtualization...'
        print 'Try enabling virtual support within the BIOS...'; sleep(3)

    if get_free_space < sup_free_space:
        print '\nWARNING: Install May Fail!'
        print 'A minimum of [%s] of free disk recommended...' % min_disk_size
        get_capacity(); sleep(3)
    else:
        print '\nFree Disk \t\t\t\t[OK]'; get_capacity()

def git_pkg_install():

    git_repo = "pkgrepo/git-repo"
    chk_git_pkg = 'which git'
    git_ex_stat = commands.getstatusoutput(chk_git_pkg)[0]

    print '\nEntering Package Deployment...\n'; sleep(3)

    print 'Checking \"Git\" Installation...'
    if git_ex_stat != 0:
        print 'Package does not appear to be installed...'

        print '\n*** Beginning Git Deployment ***\n'; sleep(3)
        try:
            subprocess.call("dpkg -i %s/*.deb" % git_repo, shell=True)
        except:
            print 'Cannot continue, package install failure!'
            raise SystemExit
        else:
            print '\nGit Package Deployment: SUCCEEDED\n'; sleep(3)
    else:
        print 'Nothing to do, package already installed...\n'


def docker_pkg_install():
    docker_repo = "pkgrepo/docker-repo/docker"
    docker_auf_repo = "pkgrepo/docker-repo/auf_support"
    chk_git_pkg = 'which docker'
    getreturn = commands.getstatusoutput(chk_git_pkg)[0]

    print 'Checking \"Docker\" Installation...'
    if getreturn != 0:
        print 'Package does not appear to be installed...'

        # Installing AUF Storage Drivers for Docker "auf_tools"...
        print '\n*** PREREQ: Installing AUF Storage Drivers for Docker ***\n\n'; sleep(3)
        try:
            subprocess.call("dpkg -i %s/*.deb" % docker_auf_repo, shell=True)
        except:
            print 'AUF Drivers -- FAILED. Expect virtual performance degrades...\n'; sleep(3)
        else:
             print '\nAUF Driver Deployment: SUCCEEDED\n'; sleep(3)

        print '\n*** Beginning Docker Deployment ***\n'; sleep(3)
        try:
            subprocess.call("dpkg -i %s/*.deb" % docker_repo, shell=True)
        except:
            print 'Cannot continue, package install failure!'
            raise SystemExit
        else:
            print '\nDocker Package Deployment: SUCCEEDED\n\n'; sleep(3)
    else:
        print 'Nothing to do, package already installed...\n\n'


if __name__ == '__main__':
    chk_sys_posture()
    git_pkg_install()
    docker_pkg_install()


