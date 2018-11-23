# coffeethon
Little script to keep count of how many coffees drank during the day

## Usages :

```
# Add 1 coffee
$ ./coffeethon.py -a
You added 1 cups of coffee
```
```
# Add more
$ ./coffeethon.py -a 6
You added 6 cups of coffee
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
You removed [number] cups of coffee
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

## Tips :

- Add a cron job to clear the data everyday :
`0 0 * * * python coffeethon.py -c`

## TODO :

- Add plural only if necessary
