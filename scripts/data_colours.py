#!/usr/bin/env python3
# Data file to hexadecimal colours

from sys import argv

with open(argv[1], "rb") as dataf:
    while True:
        coolour = dataf.read(3)
        if len(coolour) < 3:
            break
        print("'#{:02x}{:02x}{:02x}'".format(*coolour))
