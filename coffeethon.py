#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Coffeethon.py: Help you keep track of the number of cup of coffee drank."""

import sys
import getopt
from datetime import datetime

__author__ = "Tom Celestin"
__copyright__ = "Copyright 2018, Planet Earth"


def print_cups(watch, amount, operation=""):
    """Display coffee values"""
    message = ""
    if not watch:
        message = "You " + operation + " "
    else:
        message = "Today you drank "

    message += str(amount) + " cups of coffee"

    if amount < 2:
        message = message.replace("cups", "cup")

    print(message)


def manage_main_file(filename, sum, number):
    """Change value of the coffee counter."""
    if not number.isdigit():
        print("Please enter a valid number")
        return False

    number = int(number)

    file = open(filename, "r")
    current = int(file.read())

    if sum is False and number > current:
        print("You drank less than this !")
        return False

    if sum is False:
        current -= number
        print_cups(False, number, "removed")
    else:
        current += number
        print_cups(False, number, "added")

    file.close()
    file = open(filename, "w")
    file.write(str(current))
    file.close()


def manage_stats_file(filename, number):
    """Change value of the coffee counter."""
    file = open(filename, "r")
    date = datetime.now().date()
    timestamp = date.strftime("%Y%m%d")
    current = timestamp + ":" + number
    file.close()
    file = open(filename, "a")
    file.write(str(current))
    file.write("\n")
    file.close()


def clear(filename):
    """Reset the counter to 0."""
    file = open(filename, "w")
    file.write("0")
    file.close()


def watch(filename):
    """Display the counter in cool way."""
    file = open(filename, "r")
    current = int(file.read())
    print_cups(True, current)
    for i in range(current):
        print("☕️", end=" ")
    file.close()


def main(argv):
    """Main function."""
    main_filename = "/tmp/coffeethon.txt"
    stats_filename = "./logs/stats.txt"
    try:
        main_file = open(main_filename)
        stats_file = open(stats_filename)
    except IOError:
        # If not exists, create the files
        main_file = open(main_filename, 'w+')
        main_file.write("0")
        main_file.close()

        stats_file = open(stats_filename, 'w+')
        stats_file.write("")
        stats_file.close()
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
        number = "1"
        if len(sys.argv) > 2:
            number = sys.argv[2]
        if opt == '-h':
            print('coffeethon.py --add [number]')
            print('coffeethon.py --remove [number]')
            print('coffeethon.py --clear')
            print('coffeethon.py --watch')
            sys.exit()
        elif opt in ("-a", "--add"):
            manage_main_file(main_filename, True, number)
            manage_stats_file(stats_filename, number)
        elif opt in ("-r", "--remove"):
            manage_main_file(main_filename, False, number)
            # manage_stats_file(stats_filename, False, number)
        elif opt in ("-c", "--clear"):
            clear(main_filename)
        elif opt in ("-w", "--watch"):
            watch(main_filename)

if __name__ == "__main__":
    main(sys.argv[1:])
