# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.timeslot_booking import TimeslotBooking
from .api.timeslot_id import TimeslotId


routes = [
    dict(resource=TimeslotBooking, urls=['/timeslot/booking'], endpoint='timeslot_booking'),
    dict(resource=TimeslotId, urls=['/timeslot/<id>'], endpoint='timeslot_id'),
]