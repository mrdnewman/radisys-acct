import netaddr
import os

os.system('clear')


def choice_sub_menu():
    print("""
1. Proceed
2. Change
3. Go back
            """)


def fabric_ip_select():
    print("""
  1. Enter Fabric ip
  2. Go back
                 """)


def seed_select():
    print("""
  1. Enter SeedServer ip
  2. Go back
                 """)


def main_select():
    print("""
1.Customize Pod Config File
2.Quit
      """)




def pod_rules():

        config_path = (os.getcwd() + "/cord/config/")
        print ('''
=================================================================
You'll need to customize POD deployment
by updating the \"onlab_develop_pod.yml\" config file.

You're welcome to do so interactively or
Just \"Quit\" and manually update...

Location: %s

Please re-run main setup script if manual update
is chosen.
=================================================================
           ''') % config_path


def seed_action():
    done = False
    while not done:

        seedip = raw_input("Enter SeedServer ip: ")
        try:
            netaddr.ip.IPAddress(seedip)
            done = True
        except netaddr.core.AddrFormatError:
            print 'Invalid IP Address Format, please try again!'
        else:
            print '\nYou Entered... %s' % seedip

            is_valid = 0
            while not is_valid:
                try:
                    choice_sub_menu()
                    choice = int(raw_input('Enter your choice [1-3] : '))
                    is_valid = 1
                except:
                    print 'Invalid input...'

            if choice == 1:
                fabric_ip_choice()

            elif choice == 2:
                seed_action()

            elif choice == 3:
                seed_choice()

            elif choice > 3:
                print 'Selection out of range: %d' % choice
                is_valid = 0
                seed_action()



def seed_choice():
    is_valid = 0
    while not is_valid:
        try:
            seed_select()
            choice = int(raw_input('Enter your choice [1-2] : '))
            is_valid = 1

        except:
            print 'Invalid input...'

        else:
            if choice == 1:
                seed_action()

            elif choice == 2:
                onlab_menu()

            elif choice > 2:
                print 'Selection out of range: %d' % choice
                is_valid = 0


def fabric_ip_action():
    done = False
    while not done:

        fabric_ip = raw_input("Enter Frabric ip: ")
        try:
            netaddr.IPNetwork(fabric_ip)
            done = True
        except netaddr.core.AddrFormatError:
            print 'Invalid Network Format, please try again!'
        else:
            print '\nYou Entered... %s' % fabric_ip
            is_valid = 0

            while not is_valid:
                try:
                    choice_sub_menu()
                    choice = int(raw_input('Enter your choice [1-3] : '))
                    is_valid = 1
                except:
                    print 'Invalid input...'

            if choice == 1:
                print 'Proceeding with Management ip...'

            elif choice == 2:
                fabric_ip_action()

            elif choice == 3:
                seed_choice()

            elif choice > 3:
                print 'Selection out of range: %d' % choice
                is_valid = 0
                seed_action()


def fabric_ip_choice():
    is_valid = 0
    while not is_valid:
        try:
            fabric_ip_select()
            choice = int(raw_input('Enter your choice [1-2] : '))
            is_valid = 1

        except:
            print 'Invalid input...'
        else:

            if choice == 1:
                fabric_ip_action()

            elif choice == 2:
                seed_choice()

            elif choice > 2:
                print 'Selection out of range: %d' % choice
                is_valid = 0


def onlab_menu():
    is_valid = 0
    pod_rules()
    while not is_valid:
        try:
            main_select()
            choice = int(raw_input('Enter your choice [1-2] : '))
            is_valid = 1
        except:
            print 'Invalid input...'

    if choice == 1:
        seed_choice()
    elif choice == 2:
        raise SystemExit


onlab_menu()