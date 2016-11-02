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
    print "Checking %s...\n" % sudovar
    sleep(3.0)

    if os.path.isfile("%s" % sudovar) and os.access("%s" % sudovar, os.R_OK):
        print "File %s exist and accessible" % sudovar
        print "Backing up %s..." % sudovar
        copyfile("%s" % sudovar, "%s" % sudovar + getdate())



    for line in readsudo:
        if '%s' % sudopattern in line:
            found = "True"
            print "%s already set. Nothing to do...\n" % sudovar
            sudofile.close()

    if not found:
        print "Creating sudo entry in %s..." % sudovar
        with open('%s' % sudovar, 'a') as f:
            f.write('%s\n' % sudopattern)
            f.close()
        p = subprocess.Popen(["service", "sudo", "restart"], stdout=subprocess.PIPE)
        output, err = p.communicate()
        print"Restarted sudo service...\n", output


if __name__ == "__main__":
    setsudo()



