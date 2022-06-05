# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from v2.api.database import dbQuery

class CinemaNameSnacks(Resource):

    def get(self, name):
        try:
            command = "Select snacks from cinema WHERE cinema_name='{}'".format(name)
            result = dbQuery('cinema.db', command)
            print(result[0][0])
            return {"snacks": result[0][0]}, 200, None
        except:
            return {"CinemaSnacks": "Not Found"}, 404, None 