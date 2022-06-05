# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from v2.api.database import dbQuery


class MovieNameCinema(Resource):

    def get(self, name):
        try:
            command = "Select id from movies WHERE movie_name='{}'".format(name)
            result = dbQuery('cinema.db', command)
            id = result[0][0]
            command = "Select cinema_id from time_slot WHERE movie_id={}".format(id)
            result = dbQuery('cinema.db', command)
            movie_id = list(dict.fromkeys(result))
            cinemas=[]
            for ids in movie_id:
                command = "Select cinema_name from cinema WHERE id={}".format(ids[0])
                result = dbQuery('cinema.db', command)
                cinemas.append(result[0][0])
            return {'cinema_list':cinemas}, 200, None
        except:
            return {"MovieInformation": "Not Found/ Error"}, 404, None