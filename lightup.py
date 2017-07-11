#!/usr/bin/env python3
# lightup (alpha release)
# Thanks to wavexx(acpilight) for udev idea
# Copyright 2017, Aswin Babu Karuvally

# import the serious stuff
import os
import shutil
import argparse


# set or get the brightness
def brightness(brightness_file_path, function, value):
    if function == 'get':
        brightness_file = open(brightness_file_path, 'r')
        print("current brightness is " + brightness_file.readline().rstrip())
        brightness_file.close()
    
    elif function == 'set':
        brightness_file = open(brightness_file_path, 'w')
        brightness_file.write(value)


# copy executable, symlink and set permissions
def install_lightup(brighntess_file_path):
    # set permission
    os.chmod(brightness_file_path, 0o666)
    
    # copy and symlink essential files
    os.makedirs('/opt/lightup')
    try:
        shutil.copyfile('lightup.py', '/opt/lightup/lightup.py')
        os.symlink('/opt/lightup/lightup.py', '/usr/bin/lightup')
    except:
        print('error: unable to copy the application files, exiting...')
        exit()


# the main function
def main():
    # set some essential variables
    brightness_file_path = '/sys/class/backlight/intel_backlight/brightness'
    
    # parse run-time arguments
    parser = argparse.ArgumentParser(description=
        'lightup, adjust your backlight brightness')
    parser.add_argument('-i', '--install', help='Install lightup', action='store_true')
    parser.add_argument('-b', '--brightness', help='set backlight')
    arguments = parser.parse_args()
    
    # install lightup
    if arguments.install:
        if not os.getuid() != '0':
            print('please run the installer as root')
            exit()
        else:
            install_lightup(brightness_file_path)
    
    # set brightness
    elif arguments.brightness:
        brightness(brightness_file_path, 'set', arguments.brightness)
    
    # return current brightness
    else:
        brightness(brightness_file_path, 'get', None)


# run the main function
main()