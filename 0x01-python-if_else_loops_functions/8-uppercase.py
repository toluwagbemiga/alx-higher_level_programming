#!/usr/bin/python3
def uppercase(str):
    for a in str:
        a = ord(a)
        if a >= 97 and a <= 122:
            a -= 32
        a = chr(a)
        print("{}".format(a), end='')
    print("")
