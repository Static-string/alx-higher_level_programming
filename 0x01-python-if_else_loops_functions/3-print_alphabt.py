#!/usr/bin/python3
for a in range(97, 123):
    ch = chr((a))
    if ch != 'q' and ch != 'e':
        print("{}".format(ch), end="")
