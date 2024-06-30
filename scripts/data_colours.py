#!/usr/bin/env python3
# Data file to hexadecimal colours

from sys import argv, stdin

if stdin.isatty():
    print("Give me a raw RGB data file name, or pipe the raw RGB data to me.")
    exit(0)

if len(argv) < 2 or argv[1] == "-":
    file_to_read = stdin.buffer
else:
    file_to_read = open(argv[1], "rb")

while True:
    coolour = file_to_read.read(3)
    if len(coolour) < 3:
        break
    print("#{:02x}{:02x}{:02x}".format(*coolour))

file_to_read.close()
