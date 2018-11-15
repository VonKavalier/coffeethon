# coffeethon
Little script to keep count of how many coffees drank during the day

## Usages :

```
# Add 1 coffee
$ ./coffeethon.py -a
```
```
# Add more
$ ./coffeethon.py -a 6
```
```
# See how many were drank
$ ./coffeethon.py -w
Today you drank 7 cups of coffee
☕️ ☕️ ☕️ ☕️ ☕️ ☕️ ☕️
```
```
# You can rectify the amount by specifying how many to remove
$ ./coffeethon.py -r [number]
```
```
# Possibility to start from 0 again
$ ./coffeethon.py -c
```
```
# Get help
$ ./coffeethon -h
coffeethon.py --add [number]
coffeethon.py --remove [number]
coffeethon.py --clear
coffeethon.py --watch
```
