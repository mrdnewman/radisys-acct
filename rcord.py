import os
import os.path
import subprocess
from shutil import copyfile
from time import sleep
from datetime import date

os.system('clear')

def getdate():
    now = date.today()
    full = "." + str(now.month) + "." + str(now.day) + "." + str(now.year)
    return full

def setsudo():

    sudovar = "/etc/sudoers"
    sudopattern = "headnode ALL=(ALL) NOPASSWD: ALL"
    sudofile = open('%s' % sudovar, 'r')
    readsudo = sudofile.readlines()
    found = False

    print ""
    print "Setting up Head Node for password-less sudo access..."
    print "Checking for %s...\n" % sudovar
    sleep(3.0)

    if os.path.isfile("%s" % sudovar) and os.access("%s" % sudovar, os.R_OK):
        print "%s is accessible..." % sudovar

        for line in readsudo:
            if '%s' % sudopattern in line:
                found = "True"
                print "Sudo parameters already set. Nothing to do...\n"
                sudofile.close()
    else:
        print "Failed to change %s" % sudovar
        raise SystemExit

    if not found:
        print "Backing up %s...\n" % sudovar
        copyfile("%s" % sudovar, "%s" % sudovar + getdate())
        print "Creating sudo entry..."
        with open('%s' % sudovar, 'a') as f:
            f.write('%s\n' % sudopattern)
            f.close()
        p = subprocess.Popen(["service", "sudo", "restart"], stdout=subprocess.PIPE)
        output, err = p.communicate()
        print"Restarting sudo service...\n", output


if __name__ == "__main__":
    setsudo()