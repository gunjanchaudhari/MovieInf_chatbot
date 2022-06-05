# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from v2.api.database import dbQuery


class CinemaNameNowShowing(Resource):

    def get(self, name):
        try:    
            command = "Select id from cinema WHERE cinema_name='{}'".format(name)   
            result = dbQuery('cinema.db', command)
            cinema_id= int(result[0][0])
            command = "Select movie_id from time_slot WHERE cinema_id={} AND now_showing=1".format(cinema_id)
            result = dbQuery('cinema.db', command)
            movie_id = list(dict.fromkeys(result))
            now_showing = []
            for results in movie_id:
                command = "Select movie_name from movies WHERE id={}".format(results[0])
                movie = dbQuery('cinema.db', command)
                now_showing.append(movie[0][0])

            return {"movies": now_showing}, 200, None
        except:
            return {"NowShowing": "Not Found/Error"}, 404, None