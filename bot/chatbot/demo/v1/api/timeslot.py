""" This file handles contains multiple functions related to bookings.
Each function requests respective information from the timeslot container"""
import requests
import json

def get_available_time(id):

    BASE_URL = "http://localhost:8085/v1/timeslot/{}".format(id)
    url = BASE_URL
    json_data=requests.get(url).json()
    return json_data


def post_timeslot_movie(name, no_tickets, timeslot, ticket_type):

    url = 'http://127.0.0.1:8085/v1/timeslot/booking'
    data = {
        "name": name,
        "tickets": no_tickets,
        "timeslot": timeslot,
        "ttype": ticket_type
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r


def patch_cancel_timeslot(id, name):

    url = 'http://127.0.0.1:8085/v1/timeslot/booking'
    data = {"booking_id": id,
            "name": name       
    }
    headers = {'content-type': 'application/json'}
    r = requests.patch(url, data=json.dumps(data), headers=headers)
    return r
    #return r['status_cancelation']



