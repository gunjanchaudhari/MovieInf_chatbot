# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from v2.api.database import dbQuery

class Movie(Resource):

    def get(self):
        try:    
            command = "Select movie_id from time_slot WHERE now_showing=1"
            result = dbQuery('cinema.db', command)
            now_showing = []
            movie_id = list(dict.fromkeys(result))
            for movies in movie_id:
                command = "Select movie_name from movies WHERE id={}".format(movies[0])
                movie = dbQuery('cinema.db', command)
                now_showing.append(movie[0][0])
            return {"movies": now_showing}, 200, None
        except:
            return {"NowShowing": "Not Found/Error"}, 404, None
    