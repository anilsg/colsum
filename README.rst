======
colsum
======

----------------------------------------------------------------
Filter to sum columns of numbers in text instead of a Vim plugin
----------------------------------------------------------------

Usage
=====

Currently the basic filter takes no arguments or options.
Pipe line-based text containing columns of numbers into ``colsum``.
The filter will locate numbers contained in the text by sequential order, and calculate totals.
The output is the ordered sums of the columns contained in the text::

    $ echo -e "1,234 5 6\n7 foo 8 bar 9 0\n" | colsum
    1241.0   13.0   15.0   0.0

The primary use-case is to select lines in Vim and then pipe through ``colsum`` to return the totals.

1. In Vim highlight the lines that contain your ordered columns of numbers.
2. Type ``:`` to enter command mode.
3. Type the command ``!colsum`` and lines will be replaced by the sums.

This avoids any ``vimrc`` content or plugins and is a lot simpler than the usual ``awk`` solutions.
The source can also be quickly customised to suit individual use-cases.

Features
========

There are several TODOs listed in the docstring.
The current implementation is all I needed to get started.

- Text is processed as lines and numerics identified in sequence.
- Each line is then treated as a sequence of numbers.
- Numbers so identified are then summed by columns.
- The output is just the space separated list of sums.

Strings of numerics that are not valid floats will throw an exception.

Compiling with Cython
=====================

Given the variety of environmental differences I prefered to compile the Python using Cython and place it in ``/usr/local/bin``.
This ensures robust accessibility and independence when starting Vim from inside or outside of virtual environments.

- You may have to ``sudo apt install cython``
- Make the source code available as ``pyx``: ``cp colsum.py colsum.pyx``
- Generate the C file: ``cython colsum.pyx --embed``
- Compile the binary: ``gcc -Os -I /usr/include/python3.8 -o colsum colsum.c -lpython3.8 -lpthread -lm -lutil -ldl``
- Install the binary: ``sudo mv colsum /usr/local/bin/colsum``

Too easy.
