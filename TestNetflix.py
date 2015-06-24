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
from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve, netflix_init, netflix_rmse

movie_avg = {}
viewer_avg = {}
expected = {}

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :


    # ----
    # init
    # ----

    netflix_init()

    
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
        v = netflix_eval(10035, 1651047)
        self.assertEqual(v, 3.4)

    def test_eval_2 (self) :
        v = netflix_eval(2043, 2312054)
        self.assertEqual(v, 4.3)

    def test_eval_3 (self) :
        v = netflix_eval(10851, 1050707)
        self.assertEqual(v, 3.8)

    def test_eval_4 (self) :
        v = netflix_eval(10851, 514376)
        self.assertEqual(v, 3.8)

    def test_eval_5 (self) :                      
        v = netflix_eval(14961, 1143187)
        self.assertEqual(v, 5.0)


    # ------------
    # netflix_rmse
    # ------------

    def test_rmse_1 (self) :
        num_list = [(10005, 793736, 3.3), (10005, 926698, 3.3), (10006, 0, 0), (10006, 1093333, 3.6), (10006, 1982605, 3.3)]
        rmse = netflix_rmse(num_list)
        self.assertEqual(rmse, str(0.95))

    def test_rmse_2 (self) :
        num_list = ((10008, 1813636, 4.3), (10008, 2048630, 3.5), (10008, 930946, 3.7), (1001, 1050889, 4.0))
        rmse = netflix_rmse(num_list)
        self.assertEqual(rmse, str(0.71))

    def test_rmse_3 (self) :
        num_list = {(1006, 0, 0), (1006, 1004708, 4.1), (1006, 762076, 4.2), (1006, 1403722, 3.8)}
        rmse = netflix_rmse(num_list)
        self.assertEqual(rmse, str(0.54))        

    def test_rmse_4 (self) :
        num_list = [(10035, 1651047, 3.4), (10035, 811486, 4.4), (10059, 962754, 2.1)]
        rmse = netflix_rmse(num_list)
        self.assertEqual(rmse, str(0.49))            


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

        r = StringIO("10035:\n1651047\n811486\n10059:\n962754\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10035:\n3.4\n4.4\n10059:\n2.1\nRMSE: 0.49\n")

    def test_solve_2 (self) :
        r = StringIO("10008:\n1813636\n2048630\n930946\n1001:\n1050889\n67976\n1025642\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10008:\n4.3\n3.5\n3.7\n1001:\n4.0\n3.5\n3.3\nRMSE: 0.93\n")

    def test_solve_3 (self) :
        r = StringIO("1006:\n1004708\n762076\n1403722\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1006:\n4.1\n4.2\n3.8\nRMSE: 0.54\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

