# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from v2.api.database import dbQuery

class CinemaName(Resource):

    def get(self, name):
        command = "Select * from cinema WHERE cinema_name='{}'".format(name)
        result = dbQuery('cinema.db', command)
        result = result[0]
        return {"id": result[0],"name": result[1],"address":result[2],"phone": result[3]}, 200, None  