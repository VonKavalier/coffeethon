#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Coffeethon.py: Help you keep track of the number of cup of coffee drank."""

import sys
import getopt

__author__ = "Tom Celestin"
__copyright__ = "Copyright 2018, Planet Earth"

def printCups(operation, amount, isWatch):
    if isWatch == False:
        if amount == 1:
            print("You " + operation + " " + str(amount) + " cup of coffee")
        else:
            print("You " + operation + " " + str(amount) + " cups of coffee")
    else:
        if amount == 1:
            print("Today you drank " + str(amount) + " cup of coffee")
        else:
            print("Today you drank " + str(amount) + " cups of coffee")
def manage_file(filename, sum, number):
    """Change value of the coffee counter."""
    number = int(number)
    file = open(filename, "r")
    current = int(file.read())
    if sum is True:
        current += number
        printCups("added", number, False)
    else:
        current -= number
        printCups("removed", number, False)
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
    printCups("", int(current), True)
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
