# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from v1.api.database import dbQuery

class TimeslotId(Resource):

    def get(self, id):
        print( id)
        command = "Select * from timeslot WHERE id = {}".format(int(id))
        result = dbQuery('bookings.db', command)
        print(result)
        available = result[0][4]
        gold = result[0][8]
        platinum = result[0][9]
        silver = result[0][10]
        return {"available": available, "gold": gold, "platinum": platinum, "silver": silver}, 200, None