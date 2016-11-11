

import os
import struct
import commands
import platform




os.system('clear')

def intro_dev():

        get_os = platform.linux_distribution()[0]
        get_rel = platform.linux_distribution()[1]
        get_arch = platform.processor()
        sup_arch = 'x86_64'
        sup_os = 'Ubuntu'
        sup_rel = '14.04'

        welcome = "\nRadisy Corp.\nWelcome To Development Server Setup\n"
        #get_arch = commands.getoutput("arch")

        print '\n'.join('{:^95}'.format(s) for s in welcome.split('\n'))
        print "Checking System Posture...\n"

        if platform.system() == 'Linux':
            try:
                print 'Platform: Linux -- OK...\n'
                if sup_arch == get_arch:
                    try:
                        print '64bit -- OK...'
                        if sup_os == get_os:
                            try:
                                print 'Using Ubuntu -- Ok...'
                                if sup_rel == get_rel:
                                    try:
                                        print 'Release %s -- OK...' % sup_rel
                                    except:
                                        print '%s release is HIGHLY recommended!' % sup_rel
                            except:
                                print 'Ubuntu OS Highly Recommended...'
                    except:
                        print "\nIt's HIGHLY recommeded to us a 64bit OS..."
                        print "Current Arch: %s..." % get_arch
                        print "Supported Arch: %s...\n" % sup_arch

            except:
                print 'Cannot continue -- Linux Platform required...\n'
                raise SystemExit




if __name__ == '__main__':
    intro_dev()












