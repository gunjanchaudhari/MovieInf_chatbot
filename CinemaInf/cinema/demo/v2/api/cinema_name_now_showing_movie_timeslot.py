# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from flask import jsonify
from . import Resource
from .. import schemas
from v2.api.database import dbQuery


class CinemaNameNowShowingMovieTimeslot(Resource):

    def get(self, name, movie):
        try:    
            command = "Select id from cinema WHERE cinema_name='{}'".format(name)   
            result = dbQuery('cinema.db', command)
            cinema_id= int(result[0][0])
            command = "Select id from movies WHERE movie_name='{}'".format(movie)
            result = dbQuery('cinema.db', command)
            movie_id= int(result[0][0])
            command = "Select * from time_slot WHERE cinema_id={} AND now_showing=1 AND movie_id={}".format(cinema_id, movie_id)
            result = dbQuery('cinema.db', command)
            day = []
            daily ={}
            for res in result:
                day.append(res[5])
            day_id = list(dict.fromkeys(day))
            print(day_id)
            for days in day_id:
                times = {}
                for res in result:
                    if(res[5]==days):
                        times['id'] = res[0]
                        times['start_time'] = res[3]
                command = "Select day from week_day WHERE id={}".format(days)
                dayy = dbQuery('cinema.db', command)
                daily[dayy[0][0]]= times
            print(daily)
            return daily, 200, None
        except:
            return {"NowShowing": "Not Found/Error"}, 404, None 