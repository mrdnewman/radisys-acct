import os
import sys
import commands
import os.path
import subprocess
from shutil import copyfile
from time import sleep
from datetime import date

os.system('clear')

def opened_w_error(filename, mode="r"):
    try:
        f = open(filename, mode)
    except IOError, err:
        yield None, err
    else:
        try:
            yield f, None
        finally:
            f.close()


#with opened_w_error("/etc/passwd", "a") as (f, err):
#    if err:
#       print "IOError:", err
#    else:
#        f.write("guido::0:0::/:/bin/sh\n")

def applydate():
    now = date.today()
    full = "." + str(now.month) + "." + str(now.day) + "." + str(now.year)
    return full

def get_oslevel():
    osname = 'Ubuntu'
    osrel = '14.04'
    get_id = commands.getoutput("lsb_release -i | awk '{ print $3 }'")
    get_rel = commands.getoutput("lsb_release -r | awk '{ print $2 }'")

    if get_id != osname and get_rel != osrel:
       print "\nPlease Try Install With Correct OS Version:"
       print "%s" % osname
       print "%s\n" % osrel
       sys.exit(1)
    else:
        print "Checking OS Level..."
        print get_id
        print get_rel
        print "OK\n"

def setsudo():
    sudovar = "/etc/sudoers"
    sudopattern = "headnode ALL=(ALL) NOPASSWD: ALL"
    sudofile = open('%s' % sudovar, 'r')
    readsudo = sudofile.readlines()
    found = False

    print "Setting up Head Node for password-less sudo access..."
    print "Checking for %s..." % sudovar
    sleep(3.0)

    if os.path.isfile("%s" % sudovar) and os.access("%s" % sudovar, os.R_OK):
            print "OK\n"
            for line in readsudo:
                if '%s' % sudopattern in line:
                    found = "True"
                    print "Sudo parameters already set. Nothing to do...\n"
                    sudofile.close()
    else:
        print "Unable to change %s\n" % sudovar
        raise SystemExit

    if not found:
        print "Backing up %s..." % sudovar
        try:
            copyfile("%s" % sudovar, "%s" % sudovar + applydate())
        except EnvironmentError:
            print "Error backing up %s\n" % sudovar
        else:
            print "OK\n"

        print "Creating sudo entry..."
        with open('%s' % sudovar, 'a') as f:
                f.write('%s\n' % sudopattern)
                f.close()
        try:
            p = subprocess.Popen(["service", "sudo", "restart"], stdout=subprocess.PIPE)
            output, err = p.communicate()
            print"Restarting sudo service...", output
        except EnvironmentError:
            print "Couldn't restart service -- please look into this!"
            raise SystemExit
        else:
            print "OK\n"




if __name__ == "__main__":
    get_oslevel()
    setsudo()




