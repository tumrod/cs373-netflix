#!/usr/bin/env python3

# ---------------------------
# tumrod/cs373-netflix/Netflix.py
# Copyright (C) 2015
# Tipparat Umrod
# ---------------------------

# ------------
# netflix_read
# ------------

def netflix_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

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

    if (i > j) :
        temp = i
        i = j
        j = temp

    max_cycle_len = 1

    for n in range (i, j+1) :
        c = 1
        index = n

        if (array[n] != 0) :
            c = array[n]
        else :
            while n > 1 :
                if (n % 2) == 0 :
                    n = (n // 2)
                else :
                    n = n + (n << 1) + 1

                # lookup the cycle length if the value has been computed
                if (n <= 1000000 and array[n] != 0) :
                    c += array[n]
                    break;
                    
                c += 1

        assert c > 0
        array[index] = c
        max_cycle_len = max(max_cycle_len, c)

    return max_cycle_len

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
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

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
