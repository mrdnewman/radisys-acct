

import os
import time
import platform
import commands
import subprocess

os.system('clear')

get_os = platform.linux_distribution()[0]
get_ver = platform.linux_distribution()[1]
get_arch = platform.processor()
sup_arch = 'x86_64'
sup_os = 'Ubuntu'
sup_ver = '14.04'


def intro_dev():

        welcome = "\nRadisy Corp.\nWelcome To Development Server Setup\n"

        print '\n'.join('{:^95}'.format(s) for s in welcome.split('\n'))
        time.sleep(2)
        print "Checking System Posture...\n"
        time.sleep(2)

        if platform.system() == 'Linux':
                if sup_os != get_os:
                    print 'WARNING...'
                    time.sleep(2)
                    platform_info()
                else:
                    print 'Platform: Linux -- OK'
                    print 'Distro: Ubuntu -- Ok'
                    if sup_ver != get_ver:
                        print 'Highly Recommend: Using Ubuntu version %s' % sup_ver
                    else:
                        print 'Ubuntu version: %s -- OK' % sup_ver
                    if sup_arch != get_arch:
                        print 'Highly Recommend: Using a 64bit OS\n'
                    else:
                        print 'Arch: 64bit -- OK\n'
        else:
                print 'Cannot continue -- Linux Platform required...\n'
                raise SystemExit


def dev_pkg_install():

        git_repo = '/home/radisys/instpkg/git-repo/'
        git_collect = ['liberror-perl', 'git-man', 'git_']
        chk_git_pkg = 'which git'
        getreturn = commands.getstatusoutput(chk_git_pkg)[0]

        print 'Entering Package Deployment...\n'
        time.sleep(2)

        print 'Checking \"Git\" Installation...'
        if getreturn != 0:
            print 'Package does not appear to be installed...'

            print 'Beginning Package Deployment...\n'
            time.sleep(2)
            os.chdir(git_repo)
            for f in git_collect:
                try:
                    subprocess.call("dpkg -i %s*" % f, shell=True)
                except:
                    print 'Package Install Failure: %s'
                    raise SystemExit
                else:
                    print 'Package Deployment: Succeeded\n'
                    time.sleep(2)
        else:
            print 'Nothing to do, package already installed...\n'


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


if __name__ == '__main__':
    intro_dev()
    dev_pkg_install()












