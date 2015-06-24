#!/usr/bin/env python3

# ---------------------------
# tumrod/cs373-netflix/Netflix.py
# Copyright (C) 2015
# Tipparat Umrod
# ---------------------------

from numpy     import mean, sqrt, square, subtract
from urllib.request import urlopen
import json

# --------------
# netflix_global
# --------------

movies_id = 0

avg_avg_movies = 3.2281371945                           # average of all the movies
#avg_avg_customer = 3.67413045111
movie_avg = {}
viewer_avg = {}
expected = {}

# ------------
# netflix_init
# ------------

def netflix_init () :
    """
    init all of the cache by calling json_cache(cache_url)
    """
    global movie_avg
    global viewer_avg
    global expected

    movie_avg = json_cache('http://www.cs.utexas.edu/users/ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json')
    expected = json_cache('http://www.cs.utexas.edu/users/ebanner/netflix-tests/pam2599-probe_solutions.json')
    viewer_avg = json_cache('http://www.cs.utexas.edu/~ebanner/netflix-tests/ezo55-Average_Viewer_Rating_And_True_Variance_Cache.json')

# -------------
# netflix_cache
# -------------

def json_cache(file_url):
    """
    input file_url, cache file in .json
    return a dictionary of cache

    """

    url = urlopen(file_url)
    cache = json.loads(url.read().decode(url.info().get_param('charset') or 'utf-8'))

    return cache

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
    assert(type(s) is str)

    customer_id = 0

    if ":" in s :
        s = s[:-2]
        movies_id = int(s)
        assert movies_id != 0
    else :
        assert movies_id != 0
        customer_id = int(s) 

    assert (type(movies_id) is int)
    assert (type(customer_id) is int)

    return [movies_id, customer_id]


# ------------
# netflix_eval
# ------------

def netflix_eval (i, j):
    """
    i movies_id
    j customer_id
    return rating with 1 decimal place
    
    """
    assert (type(i) is int)
    assert (type(j) is int)

    m_id = str(i)
    rating = 0
    movies_diff = movie_avg[m_id]-avg_avg_movies

    if(j != 0) :
        assert (j != 0)

        v_id = str(j)
        rating = viewer_avg[v_id][0] + viewer_avg[v_id][1]/200
        rating += movie_avg[m_id] + movies_diff/2
        rating /= 2

        if (rating > 5.0):
            rating = 5.0
        elif (rating < 0.0):
            rating = 0.0

    assert(rating >= 0.0 and rating <= 5.0)

    return round(rating, 1)


# ------------
# netflix_rmse
# ------------

def netflix_rmse (rating_iterable):
    """
    taking in an iterable
    return truncated root mean square error
    """

    assert (hasattr(rating_iterable, "__iter__"))
    
    total_viewer = 0
    rmse = 0

    for i,j,k in rating_iterable:

        if (j!=0):
            assert(j != 0)
            assert(str(i) in expected.keys())
            assert(str(j) in expected[str(i)].keys())

            total_viewer += 1
            rmse += square(k-expected[str(i)][str(j)])

    assert (total_viewer > 0)

    rmse = sqrt(rmse/total_viewer)
    return str('%.2f'%(rmse))

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
    
    if (j != 0) :
        w.write(str(v) + "\n")
    else :
        w.write(str(i) + ":\n")


# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """
    netflix_init()              # init all of the caches

    rating_generator = list(((i,j,(netflix_eval(i,j))) for i, j in (netflix_read(s) for s in r)))

    for i,j,v in rating_generator:
        netflix_print(w,i,j,v)

    rmse = netflix_rmse(rating_generator)

    w.write("RMSE: "+rmse)

