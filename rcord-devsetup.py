
#!/usr/bin/env python

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

        welcome = "\nRadisy Corp.\nWelcome To Development Server Setup\nAn RCORD-1.0 Product\n"
        print '\n'.join('{:^95}'.format(s) for s in welcome.split('\n'))
        time.sleep(3)

        print "Checking System Posture...\n"
        time.sleep(3)
        if platform.system() == 'Linux':
                if sup_os != get_os:
                    print 'WARNING...'
                    time.sleep(3)
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

def git_pkg_install():

        git_repo = "pkgrepo/git-repo"
        chk_git_pkg = 'which git'
        getreturn = commands.getstatusoutput(chk_git_pkg)[0]

        print 'Entering Package Deployment...\n'
        time.sleep(3)

        print 'Checking \"Git\" Installation...'
        if getreturn != 0:
            print 'Package does not appear to be installed...'

            print 'Beginning Git Deployment...\n'
            time.sleep(3)

            try:
                subprocess.call("dpkg -i %s/*.deb" % git_repo, shell=True)
            except:
                print 'Cannot continue, package install failure!'
                raise SystemExit
            else:
                print '\nGit Package Deployment: Succeeded\n'
                time.sleep(3)
        else:
            print 'Nothing to do, package already installed...\n'

def vag_pkg_install():

        vag_repo = "pkgrepo/vagrant-repo"
        chk_vag_pkg = 'which vagrant'
        getreturn = commands.getstatusoutput(chk_vag_pkg)[0]

        print 'Checking \"Vagrant\" Installation...'
        time.sleep(3)

        if getreturn != 0:
            print 'Package does not appear to be installed...'

            print 'Beginning Vagrant Deployment...\n'
            time.sleep(3)
            try:
                subprocess.call("dpkg -i %s/*.deb" % vag_repo, shell=True)
            except:
                print 'Cannot continue, package install failure!'
                raise SystemExit
            else:
                print '\nVagrant Package Deployment: Succeeded\n'
                time.sleep(3)
        else:
            print 'Nothing to do, package already installed...\n'


def virtbx_pkg_install():

        virtbx_repo = "pkgrepo/virtbx-repo"
        chk_virtbx_pkg = 'which virtualbox'
        getreturn = commands.getstatusoutput(chk_virtbx_pkg)[0]

        print 'Checking \"VirtualBox\" Installation...'
        time.sleep(3)

        if getreturn != 0:
            print '\nPackage does not appear to be installed...'
            print '\nPlease be patient, this may take some time...\n'

            print '\nBeginning Virtualbox Deployment...\n'
            time.sleep(5)

            try:
                subprocess.call("dpkg -i %s/*.deb" % virtbx_repo, shell=True)
            except:
                print 'Cannot continue, package install failure!\n'
                raise SystemExit
            else:
                print '\n Virtualbox Package Deployment: Succeeded\n'
                time.sleep(3)
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


if __name__=='main':
    intro_dev()
    git_pkg_install()
    vag_pkg_install()
    virtbx_pkg_install()

