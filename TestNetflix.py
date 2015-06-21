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
        self.assertEqual(j, 0)

        s = "1234\n"
        i, j = netflix_read(s)
        self.assertEqual(i, 15)
        self.assertEqual(j, 1234)

        s = "1467\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  15)
        self.assertEqual(j, 1467)

    def test_read_2 (self) :
        s    = "30:\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  30)
        self.assertEqual(j, 0)

        s    = "5466\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  30)
        self.assertEqual(j, 5466)

        s    = "6788\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  30)
        self.assertEqual(j, 6788)

        s    = "12:\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  12)
        self.assertEqual(j, 0)

        s    = "3444\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  12)
        self.assertEqual(j, 3444)

    def test_read_3 (self) :
        s    = "2044:\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  2044)
        self.assertEqual(j, 0)

        s    = "345667\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  2044)
        self.assertEqual(j, 345667)

        s    = "4521\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  2044)
        self.assertEqual(j, 4521)

        s    = "2212:\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  2212)
        self.assertEqual(j, 0)

        s    = "3411\n"
        i, j = netflix_read(s)
        self.assertEqual(i,  2212)
        self.assertEqual(j, 3411)

    # ----
    # eval
    # ----
    
    def test_eval_1 (self) :
        v = netflix_eval(2043, 1417435)
        self.assertEqual(v, 3.4)

    def test_eval_2 (self) :
        v = netflix_eval(2043, 2312054)
        self.assertEqual(v, 4.1)

    def test_eval_3 (self) :
        v = netflix_eval(10851, 1417435)
        self.assertEqual(v, 4.3)

    def test_eval_4 (self) :
        v = netflix_eval(10851, 2312054)
        self.assertEqual(v, 1.4)


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        netflix_print(w, 1, 10234, 4.6)
        self.assertEqual(w.getvalue(), "4.6\n")

    def test_print_2 (self) :
        w = StringIO()
        netflix_print(w, 10851, 0, 32)
        self.assertEqual(w.getvalue(), "10851:\n")

    def test_print_3 (self) :
        w = StringIO()
        netflix_print(w, 2041, 0, 32)
        self.assertEqual(w.getvalue(), "2041:\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1:\n10233\n10044\n2:\n21550\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:\n4.5\n4.5\n2:\n4.5\n")

    def test_solve_2 (self) :
        r = StringIO("10851:\n1417435\n2312054\n462685\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10851:\n4.3\n1.4\n2.8\n")

    def test_solve_3 (self) :
        r = StringIO("2043:\n1417435\n2312054\n462685\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "2043:\n3.4\n4.1\n1.9\n")

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
