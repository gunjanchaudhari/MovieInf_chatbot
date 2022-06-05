# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from v2.api.database import dbQuery



class Cinema(Resource):

    def get(self):
        try:
            command = "Select cinema_name from cinema"
            result = dbQuery('cinema.db', command)
            cinema=[]
            for cinemas in result:
                cinema.append(cinemas[0])
            return {"cinema_list":cinema}, 200, None
        except:
            return {"unsuccessful"}, 404, None