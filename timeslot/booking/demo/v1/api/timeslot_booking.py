# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from v1.api.database import dbQuery

class TimeslotBooking(Resource):

    def post(self):
        name = str(g.json.get('name'))
        no_ticket = int(g.json.get('tickets'))
        timeslot = int(g.json.get('timeslot'))
        ttype = str(g.json.get('ttype'))
        try:
            print(name, no_ticket, timeslot, ttype)
            
            command = "Select start_time,availability, {}, day_id from timeslot WHERE id={}".format(ttype, timeslot)
            result = dbQuery('bookings.db', command)
            print(result)
            start_time = result[0][0]
            available = (int(result[0][1]) - no_ticket)
            number = (int(result[0][2]) - no_ticket)
            day= result[0][3]
            print(available)
            print(number)
            command = "Select * from book WHERE name='{}'".format(name)
            result = dbQuery('bookings.db', command)
            print(result)
            if result:
                for res in result:
                    print(res)
                    if res[3] != timeslot:
                        print("im here")
                        command = "Select start_time, day_id from timeslot WHERE id={}".format(res[0][3])
                        result = dbQuery('bookings.db', command)
                        print(result)
                        if result[0][0] == start_time and result[0][1] == day:
                            return {"Message": "Insert Unsuccesful"}, 404, None
            print("ih here")
            command = ("""INSERT INTO book (name, no_ticket, timeslot, ttype) VALUES ('{}',{},{},'{}');""").format(name,no_ticket,timeslot,ttype)
            print(command)
            result = dbQuery('bookings.db', command)
            
            command = "Select * from book WHERE name='{}'".format(name)
            results = dbQuery('bookings.db', command)
            command = ("""UPDATE timeslot SET availability = {}, {} = {} WHERE id = {}""").format(available,ttype, number, timeslot)

            result = dbQuery('bookings.db', command)
            print(results)
            id = str(results[0][0])
            namef = str(results[0][1])
            tickets = str(results[0][2])
            print(id, namef, tickets)
            return {"id": id, "name": namef, "tickets": tickets}, 200, None
    
        except:
            return {"message": "insertion Error"}, 404, None

    def patch(self):
        booking_id = int(g.json.get('booking_id'))
        name = str(g.json.get('name'))
        try: 
            command = "DELETE from book WHERE id={} AND name='{}'".format(booking_id, name)    
            result = dbQuery('bookings.db', command)
            print(result)
            return {"status_cancelation": "Cancelled"}, 200, None
        except:
            return {"status_cancelation": "No possible Cancel"}, 404, None