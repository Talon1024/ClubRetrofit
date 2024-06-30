#!/usr/bin/env python3
# CSS hard-stop gradient generator
# https://css-tricks.com/books/greatest-css-tricks/hard-stop-gradients/
from math import floor
from itertools import tee
from sys import argv, stdin


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def gradient_stops(colours):
    percent_step=100. / (len(colours) - 1)
    stops=[]
    for x in range(len(colours)):
        stops.append(floor(percent_step * x + 0.5))

    for cl, st in zip(colours, pairwise(stops)):
        # <colour> <position as percentage>,
        yield "{cl} {st[0]}%, {cl} {st[1]}%,".format(cl=cl, st=st)


def cssify(stopstr):
    return """background-image: linear-gradient(
    to bottom,
    {stopstr}
);
""".format(stopstr=stopstr.replace("\n","\n    ")[:-1])


if __name__ == "__main__":
    args = argv
    if len(args) == 1:
        if not stdin.isatty():
            stdin_stuff = stdin.read().split("\n")
            args = stdin_stuff
        else:
            print("No arguments! If you're writing the colours in CSS notation with a hash/number sign in front, you have to quote them so that the shell doesn't interpret them as comments.")
            exit(0)

    stops = "\n".join(gradient_stops(args))
    print(cssify(stops))
