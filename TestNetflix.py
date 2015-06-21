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
        s    = "15:\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  15)

        s = "1234\n"
        i, j = netflix_read(s)
        self.assertEqual(j, 1234)

        s = "1467\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  15)
        self.assertEqual(j, 1467)

    # ----
    # eval
    # ----
    
    def test_eval_1 (self) :
        v = netflix_eval(1, 10)
        self.assertEqual(v, 1)

    def test_eval_2 (self) :
        v = netflix_eval(100, 200)
        self.assertEqual(v, 1)


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        netflix_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1:\n10\n20\n")

    def test_print_2 (self) :
        w = StringIO()
        netflix_print(w, 5, 100, 32)
        self.assertEqual(w.getvalue(), "5:\n100\n32\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1:\n10233\n10044\n2:\n21550\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:\n5\n5\n2:\n5\n")

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
