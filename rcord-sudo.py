import os
import sys
import commands
import os.path
import subprocess
from shutil import copyfile
from time import sleep
from datetime import date

os.system('clear')
sys.tracebacklimit = 0

def applydate():
    now = date.today()
    full = "." + str(now.month) + "." + str(now.day) + "." + str(now.year)
    return full

def get_oslevel():
    osname = 'Ubuntu'
    osrel = '14.04'
    get_id = commands.getoutput("lsb_release -i | awk '{ print $3 }'")
    get_rel = commands.getoutput("lsb_release -r | awk '{ print $2 }'")

    if get_id != osname or get_rel != osrel:
       print "\nThis install requires the following OS and Release:"
       print "OS: %s" % osname
       print "REL: %s\n" % osrel
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
        print "Cannot continue, sudo file must exist and be accessible\n"
        print "Please resolve and re-execute program..."
        raise SystemExit

    if not found:
        print "Backing up %s..." % sudovar
        try:
            copyfile("%s" % sudovar, "%s" % sudovar + applydate())
        except EnvironmentError:
            print "FAILED\n"
        else:
            print "OK\n"

        print "Creating sudo entry..."
        try:
            f = open('%s' % sudovar, 'a')
        except IOError:
            print "FAILED"
            print "Try creating entry manually and re-execute program..."
            raise SystemExit
        else:
            f.write("%s" % sudopattern)
            f.close()
            print "OK\n"

        print "Restarting sudo service..."
        try:
            subprocess.check_output(["service", "sudo", "restart"])
        except subprocess.CalledProcessError as e:
            print e.output
            print "Failed service restart. Try manual restart, re-execute script...\n"
            raise SystemExit
        else:
            print "OK\n"


if __name__ == "__main__":
    get_oslevel()
    setsudo()
