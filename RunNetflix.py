#!/usr/bin/env python3

# ---------------------------
# tumrod/cs373-netflix/RunNetflix.py
# Copyright (C) 2015
# Tipparat Umrod
# ---------------------------

# -------
# imports
# -------

import sys

from Netflix import netflix_solve

# ----
# main
# ----

if __name__ == "__main__" :
    netflix_solve(sys.stdin, sys.stdout)

"""
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
# That creates the file Collatz.html
"""
