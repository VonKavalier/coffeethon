#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Coffeethon.py: Help you keep track of the number of cup of coffee drank."""

import sys
import getopt

__author__ = "Von"
__copyright__ = "Copyright 2018, Planet Earth"


def manage_file(filename, sum, number):
    """Change value of the coffee counter."""
    number = int(number)
    file = open(filename, "r")
    current = int(file.read())
    if sum is True:
        current += number
    else:
        current -= number
    file.close()
    file = open(filename, "w")
    file.write(str(current))
    file.close()


def clear(filename):
    """Reset the counter to 0."""
    file = open(filename, "w")
    file.write("0")
    file.close()


def watch(filename):
    """Display the counter in cool way."""
    file = open(filename, "r")
    current = file.read()
    print("Today you drank " + current + " cups of coffee")
    for i in range(int(current)):
        print("☕️", end=" ")
    file.close()


def main(argv):
    """Main function."""
    filename = "/tmp/coffeethon.txt"

    try:
        file = open(filename)
    except IOError:
        # If not exists, create the file
        file = open(filename, 'w+')
        file.write("0")
        file.close()
    try:
        opts, args = getopt.getopt(
            argv,
            "harcw",
            [
                "add",
                "remove",
                "clear",
                "watch"
            ]
        )
    except getopt.GetoptError as e:
        print(str(e))
        print('coffeethon.py --add [number]')
        print('coffeethon.py --remove [number]')
        print('coffeethon.py --clear')
        print('coffeethon.py --watch')
        sys.exit(2)
    for opt, arg in opts:
        number = 1
        if len(sys.argv) > 2:
            number = sys.argv[2]
        if opt == '-h':
            print('coffeethon.py --add [number]')
            print('coffeethon.py --remove [number]')
            print('coffeethon.py --clear')
            print('coffeethon.py --watch')
            sys.exit()
        elif opt in ("-a", "--add"):
            manage_file(filename, True, number)
        elif opt in ("-r", "--remove"):
            manage_file(filename, False, number)
        elif opt in ("-c", "--clear"):
            clear(filename)
        elif opt in ("-w", "--watch"):
            watch(filename)

if __name__ == "__main__":
    main(sys.argv[1:])
