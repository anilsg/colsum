#!/usr/bin/env python
"""
Filter to take lines of arbitrarily separated numbers from stdin.
Isolate numbers expected to be in columns and sum by columns.
Return sums as a space separated list of numbers.

TODO: Catch ValueError and treat as 0.0.
TODO: Apply a default rounding, say 2 places.
TODO: Support option to vary rounding e.g. "-4".
TODO: Support option to treat comma as separator e.g. "-c / -C".
TODO: Support option for aligned columns (where numbers may be missing) e.g. "-p / -P".
TODO: Use https://docs.python.org/3/library/fileinput.html to greedily read all input.

To compile to a binary::

    sudo apt install cython
    cp colsum.py colsum.pyx
    cython colsum.pyx --embed
    gcc -Os -I /usr/include/python3.8 -o colsum colsum.c -lpython3.8 -lpthread -lm -lutil -ldl
    sudo mv colsum /usr/local/bin
"""

import sys
import string
import itertools


def maketrans():
    """Construct maketrans table for converting non-numerics to spaces."""
    numerics = string.digits + "-" + "."
    notnumerics = "".join(set(string.printable) - set(numerics))
    spaces = " " * len(notnumerics)
    return str.maketrans(numerics + notnumerics, numerics + spaces, ",")


def numlist(line: str, _transtable=maketrans()) -> list:
    """Translate line content to just numbers and split line into a list of float."""
    return [float(num) for num in line.translate(_transtable).split()]


def colsum(lines: list) -> list:
    """Sum all numbers in lines by columns and return as a list of float."""
    lines = [numlist(line) for line in [line.strip() for line in lines] if line]
    columns = [sum(column) for column in itertools.zip_longest(*lines, fillvalue=0.0)]
    return columns


if __name__ == "__main__":
    print("   ".join(str(column) for column in colsum(sys.stdin.readlines())))
