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
    read an int
    s a string

    set movies_id to global if read movies_id
    get customer_id
    return a list of movies_id, customer_id pair
    """
    global movies_id

    customer_id = 0

    if ":" in s :
        s = s[:-2]
        movies_id = int(s)
        assert movies_id != 0
    else :
        assert movies_id != 0
        customer_id = int(s)

    return [movies_id, customer_id]

# ------------
# netflix_eval
# ------------

def netflix_eval (i, j):
    """
    i movies_id
    j customer_id
    return rating
    """
    rating = 4.45566

    return round(rating, 1)

# -------------
# netflix_print
# -------------

def netflix_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i movies_id
    j customer_id
    v rating
    """

    if (j == 0) :
        w.write(str(i) + ":\n")
    else :
        w.write(str(v) + "\n")

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
        v = netflix_eval(i, j)
        netflix_print(w, i, j, v)
