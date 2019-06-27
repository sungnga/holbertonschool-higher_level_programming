#!/usr/bin/python3
for i in range(0, 100):
    if i < 89 and i / 10 < i % 10:
        print("{:02}".format(i), end=", ")
    elif i is 89:
        print("{:02}".format(i))
