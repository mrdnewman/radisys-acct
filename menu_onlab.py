import os


os.system('clear')

def boarder_select():

         print("""
1.Customize Pod Config File
2.Quit
            """)

def pod_rules():

        config_path = (os.getcwd() + "/cord/config/")
        print ('''
=======================================================
You'll need to customize POD deployment
by updating the \"onlab_develop_pod.yml\" config file.

You're welcome to do so interactively or
Just \"Quit\" and manually update...

Location: %s

Please re-run main setup script if manual update
is chosen.
=======================================================
           ''') % config_path


def onlab_entries1():
        get_menu = raw_input("Enter SeedServer ip: " )

is_valid = 0
pod_rules()
while not is_valid:
        try:
            boarder_select()
            choice = int(raw_input('Enter your choice [1-2] : '))
            is_valid = 1  ##
        except:
            print 'Invalid input...'

if choice == 1:
    onlab_entries1()
elif choice == 2:
    raise SystemExit











def main_menu_onlab():

    def add_ip_fn():
        get_menu = raw_input("Enter SeedServer ip: ")

    def my_quit_fn():
        raise SystemExit

    def invalid():
        print "INVALID CHOICE!"


    menu = {"1": ("Customize Pod Config File", add_ip_fn),
            "2": ("Quit", my_quit_fn)
            }
    config_path = (os.getcwd() + "/cord/config/")

    print ('''
    =======================================================
    You'll need to customize POD deployment
    by updating the \"onlab_develop_pod.yml\" config file.

    You're welcome to do so interactively or
    Just \"Quit\" and manually update...

    Location: %s

    Please re-run main setup script if manual update
    is chosen.
    =======================================================
    ''') % config_path



    for key in sorted(menu.keys()):
        print key + ":" + menu[key][0]

    ans = raw_input("\nMake A Choice: ")
    while ans != 1 or 2:
        get_val = menu.get(ans, [None, invalid])[1]()




#
# main_menu_onlab()