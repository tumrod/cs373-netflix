#!/usr/bin/env python3

# ---------------------------
# tumrod/cs373-netflix/Netflix.py
# Copyright (C) 2015
# Tipparat Umrod
# ---------------------------


movies_id = 0

# ------------
# netflix_read
# ------------

def netflix_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    customer_id = 0
    if ":" in s :
        s = s[:-1]
        movies_id = int(s)
    else :
        customer_id = int(s)

    #a = s.split()
    return [movies_id, customer_id]

# ------------
# netflix_eval
# ------------

def netflix_eval (i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """

    assert i > 0
    assert j > 0


    return 1

# -------------
# netflix_print
# -------------

def netflix_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + ":\n" + str(j) + "\n" + str(v) + "\n")

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = netflix_read(s)
        v    = netflix_eval(i, j)          #enable only lazy-cache
        netflix_print(w, i, j, v)
