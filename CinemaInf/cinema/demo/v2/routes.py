# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.cinema import Cinema
from .api.cinema_name import CinemaName
from .api.cinema_name_snacks import CinemaNameSnacks
from .api.cinema_name_now_showing import CinemaNameNowShowing
from .api.cinema_name_now_showing_movie_timeslot import CinemaNameNowShowingMovieTimeslot
from .api.movie_name_cinema import MovieNameCinema
from .api.movie_name import MovieName
from .api.movie import Movie
from .api.movie_name_cinema_cin_name_timeslot import MovieNameCinemaCinNameTimeslot


routes = [
    dict(resource=Cinema, urls=['/cinema'], endpoint='cinema'),
    dict(resource=CinemaName, urls=['/cinema/<name>'], endpoint='cinema_name'),
    dict(resource=CinemaNameSnacks, urls=['/cinema/<name>/snacks'], endpoint='cinema_name_snacks'),
    dict(resource=CinemaNameNowShowing, urls=['/cinema/<name>/now_showing'], endpoint='cinema_name_now_showing'),
    dict(resource=CinemaNameNowShowingMovieTimeslot, urls=['/cinema/<name>/now_showing/<movie>/timeslot'], endpoint='cinema_name_now_showing_movie_timeslot'),
    dict(resource=MovieNameCinema, urls=['/movie/<name>/cinema'], endpoint='movie_name_cinema'),
    dict(resource=MovieName, urls=['/movie/<name>'], endpoint='movie_name'),
    dict(resource=Movie, urls=['/movie'], endpoint='movie'),
    dict(resource=MovieNameCinemaCinNameTimeslot, urls=['/movie/<name>/cinema/<cin_name>/timeslot'], endpoint='movie_name_cinema_cin_name_timeslot'),
]