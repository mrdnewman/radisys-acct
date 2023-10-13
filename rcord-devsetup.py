
#!/usr/bin/env python

import os
import time
import platform
import subprocess
import logging

def clear_screen():
    os.system('clear')

def intro_dev():
    welcome = """
Radisy Corp.
Welcome To Development Server Setup
An RCORD-1.0 Product
"""
    clear_screen()
    print('\n'.join('{:^95}'.format(s) for s in welcome.split('\n'))
    time.sleep(3)
    print("Checking System Posture...\n")
    time.sleep(3)

    sup_arch = 'x86_64'
    sup_os = 'Ubuntu'
    sup_ver = '14.04'

    get_os, get_ver, get_arch = get_system_info()

    if platform.system() == 'Linux':
        if sup_os != get_os:
            print('WARNING...')
            time.sleep(3)
            platform_info()
        else:
            print('Platform: Linux -- OK')
            print('Distro: Ubuntu -- OK')
            if sup_ver != get_ver:
                print(f'Highly Recommend: Using Ubuntu version {sup_ver}')
            else:
                print(f'Ubuntu version: {get_ver} -- OK')
            if sup_arch != get_arch:
                print('Highly Recommend: Using a 64bit OS\n')
            else:
                print('Arch: 64bit -- OK\n')
    else:
        print('Cannot continue -- Linux Platform required...\n')
        raise SystemExit

def get_system_info():
    dist_info = platform.linux_distribution()
    return dist_info[0], dist_info[1], platform.processor()

def git_pkg_install():
    git_repo = "pkgrepo/git-repo"
    chk_git_pkg = 'which git'

    if subprocess.getstatusoutput(chk_git_pkg)[0] != 0:
        print('Package does not appear to be installed...')
        print('Beginning Git Deployment...\n')
        time.sleep(3)

        try:
            subprocess.call(f"dpkg -i {git_repo}/*.deb", shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Failed to install Git: {e}')
            raise SystemExit
        else:
            print('\nGit Package Deployment: Succeeded\n')
            time.sleep(3)
    else:
        print('Nothing to do, package already installed...\n')

def vag_pkg_install():
    vag_repo = "pkgrepo/vagrant-repo"
    chk_vag_pkg = 'which vagrant'

    if subprocess.getstatusoutput(chk_vag_pkg)[0] != 0:
        print('Package does not appear to be installed...')
        print('Beginning Vagrant Deployment...\n')
        time.sleep(3)

        try:
            subprocess.call(f"dpkg -i {vag_repo}/*.deb", shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Failed to install Vagrant: {e}')
            raise SystemExit
        else:
            print('\nVagrant Package Deployment: Succeeded\n')
            time.sleep(3)
    else:
        print('Nothing to do, package already installed...\n')

def virtbx_pkg_install():
    virtbx_repo = "pkgrepo/virtbx-repo"
    chk_virtbx_pkg = 'which virtualbox'

    if subprocess.getstatusoutput(chk_virtbx_pkg)[0] != 0:
        print('\nPackage does not appear to be installed...')
        print('\nPlease be patient, this may take some time...\n')

        print('\nBeginning Virtualbox Deployment...\n')
        time.sleep(5)

        try:
            subprocess.call(f"dpkg -i {virtbx_repo}/*.deb", shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Failed to install VirtualBox: {e}\n')
            raise SystemExit
        else:
            print('\nVirtualBox Package Deployment: Succeeded\n')
            time.sleep(3)
    else:
        print('Nothing to do, package already installed...\n')

def platform_info():
    get_os, get_ver, get_arch = get_system_info()

    print(f"""
     Current System:
     ---------------
     Distro: {get_os}
     Version: {get_ver}
     Arch: {get_arch}
    """)

    print(f"""
     Recommended System:
     -------------------
     Distro: {sup_os}
     Version: {sup_ver}
     Arch: {sup_arch}
    """)

if __name__ == '__main__':
    logging.basicConfig(filename='setup.log', level=logging.INFO)
    
    try:
        intro_dev()
        git_pkg_install()
        vag_pkg_install()
        virtbx_pkg_install()
    except SystemExit:
        logging.error('Setup process terminated with an error.')
    else:
        logging.info('Setup process completed successfully.')
