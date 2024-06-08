#!/usr/bin/env python3
# CSS hard-stop gradient generator
# https://css-tricks.com/books/greatest-css-tricks/hard-stop-gradients/
from math import floor
from itertools import pairwise
from sys import argv


def gradient_stops(colours):
    percent_step=100. / len(colours)
    stops=[]
    for x in range(len(colours)):
        stops.append(floor(percent_step * x + 0.5))

    for cl, st in zip(colours, pairwise(stops)):
        # <colour> <position as percentage>,
        yield "{cl} {st[0]}%, {cl} {st[1]}%,\n".format(cl=cl, st=st)


def cssify(stopstr):
    return """background-image: linear-gradient(
    to bottom,
    {stopstr}
);
""".format(stopstr=stopstr.replace("\n","\n    ")[:-1])


if (( $# == 0 )); then
    print "No arguments! If you're writing the colours in CSS notation with a hash/number sign in front, you have to quote them so that the shell doesn't interpret them as comments."
else
    gradient_stops $@ | cssify
fi
