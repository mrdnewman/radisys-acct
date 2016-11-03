import os
import sys
import commands
import os.path
import subprocess
from shutil import copyfile
from time import sleep
from datetime import date

# I am branch cr.3
os.system('clear')

def get_oslevel():
    osname = 'Ubuntu'
    osrel = '14.04'
    get_id = commands.getoutput("lsb_release -i | awk '{ print $3 }'")
    get_rel = commands.getoutput("lsb_release -r | awk '{ print $2 }'")

    print "Checking OS Level..."
    print get_id
    print get_rel

    if get_id != osname and get_rel != osrel:
       print "\nPlease Try Install With Correct OS Version:"
       print "%s" % osname
       print "%s\n" % osrel
       sys.exit(1)


def applydate():
    now = date.today()
    full = "." + str(now.month) + "." + str(now.day) + "." + str(now.year)
    return full

def setsudo():

    sudovar = "/etc/sudoers"
    sudopattern = "headnode ALL=(ALL) NOPASSWD: ALL"
    sudofile = open('%s' % sudovar, 'r')
    readsudo = sudofile.readlines()
    found = False

    print "\nSetting up Head Node for password-less sudo access..."
    print "Checking for %s...\n" % sudovar
    sleep(3.0)

    if os.path.isfile("%s" % sudovar) and os.access("%s" % sudovar, os.R_OK):

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
        copyfile("%s" % sudovar, "%s" % sudovar + applydate())
        print "Creating sudo entry..."
        with open('%s' % sudovar, 'a') as f:
            f.write('%s\n' % sudopattern)
            f.close()
        p = subprocess.Popen(["service", "sudo", "restart"], stdout=subprocess.PIPE)
        output, err = p.communicate()
        print"Restarting sudo service...\n", output



if __name__ == "__main__":
    get_oslevel()
    setsudo()




