

import lsb_release
import struct
import os
import commands


os.system('clear')

def intro():

        sup_arch = "x86_64"
        welcome = "\nRadisy Corp.\nWelcome To Development Server Setup\n"
        get_arch = commands.getoutput("arch")

        print '\n'.join('{:^95}'.format(s) for s in welcome.split('\n'))
        print "Checking System Posture..."

        if get_arch == sup_arch:
            print "Using 64bit OS -- OK\n"
        else:
            print "\nShould be using 64bit OS -- highly recommended"
            print "Current Arch: %s" % get_arch
            print "Supported Arch: %s\n" % sup_arch

        print "Checking OS Release..."



if __name__ == '__main__':
    intro()












