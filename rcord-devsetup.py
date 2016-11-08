

import lsb_release_ex
import struct
import os
import commands


os.system('clear')

def intro():

        welcome = "\n\n\nRadisy Corp.\nWelcome To Development Server Setup\n\n\n"
        get_arch = commands.getoutput("arch")

        print '\n'.join('{:^95}'.format(s) for s in welcome.split('\n'))
        print "Checking Sytem Architecture..."

        if get_arch == "x86_64":
            print "Using 64bit OS -- OK\n"
        else:
            print "\nShould be using 64bit OS -- highly recommended"
            print "Current Arch: %s\n" % get_arch










