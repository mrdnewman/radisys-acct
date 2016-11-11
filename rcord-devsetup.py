

import os
import platform


os.system('clear')

def intro_dev():

        get_os = platform.linux_distribution()[0]
        get_ver = platform.linux_distribution()[1]
        get_arch = platform.processor()
        sup_arch = 'x86_64'
        sup_os = 'Ubuntu'
        sup_ver = '14.04'

        welcome = "\nRadisy Corp.\nWelcome To Development Server Setup\n"

        print '\n'.join('{:^95}'.format(s) for s in welcome.split('\n'))
        print "Checking System Posture...\n"

        if platform.system() == 'Linux':
                print 'Platform: Linux -- OK'
                if sup_os == get_os and sup_ver == get_ver:
                        print 'Distro: Ubuntu -- Ok'
                        print 'Version: %s -- OK' % sup_ver
                else:
                    print 'Highly Recommend: Using a Ubuntu distro!'
                if sup_ver == get_ver:
                    print 'Version %s -- OK' % sup_ver
                else:
                    print 'Highly Recommend: Using a %s OS version!' % sup_ver
                if sup_arch == get_arch:
                        print 'Arch: 64bit -- OK'
                else:
                    print 'Highly Recommend: Using a 64bit OS!'
        else:
                print 'Cannot continue -- Linux Platform required...\n'
                raise SystemExit


if __name__ == '__main__':
    intro_dev()












