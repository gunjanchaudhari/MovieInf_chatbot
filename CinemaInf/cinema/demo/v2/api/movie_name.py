# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from v2.api.database import dbQuery


class MovieName(Resource):

    def get(self, name):
        try:    
            command = "Select * from movies WHERE movie_name='{}'".format(name)   
            result = dbQuery('cinema.db', command)
            return {"movie": name, "genre":result[0][2] ,"cast":result[0][2] }, 200, None
        except:
            return {"NowShowing": "Not Found/Error"}, 404, None