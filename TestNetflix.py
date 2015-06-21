#!/usr/bin/env python3

# ---------------------------
# tumrod/cs373-netflix/TestNetflix.py
# Copyright (C) 2015
# Tipparat Umrod
# ---------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase
from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s    = "35 100 20 150\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  35)
        self.assertEqual(j, 100)

    # ----
    # eval
    # ----
    
    def test_eval_1 (self) :
        v = netflix_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = netflix_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = netflix_eval(201, 210)
        self.assertEqual(v, 89)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        netflix_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        netflix_print(w, 5, 100, 32)
        self.assertEqual(w.getvalue(), "5 100 32\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
