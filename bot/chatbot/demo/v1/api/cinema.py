""" This file handles contains multiple functions related to cinema.
Each function requests respective information from the Cinema container"""

import requests

def get_cinema_info(name):

    BASE_URL = "http://127.0.0.1:8080/v2/cinema/{}".format(name)
    url = BASE_URL
    json_data=requests.get(url).json()
    return json_data

def get_list_cinema():

    BASE_URL = "http://127.0.0.1:8080/v2/cinema"
    url = BASE_URL
    json_data=requests.get(url).json()
    return json_data['cinema_list']

def get_snacks(cinema):

    BASE_URL = "http://127.0.0.1:8080/v2/cinema/{}/snacks".format(cinema)
    url = BASE_URL
    json_data=requests.get(url).json()
    return json_data["snacks"]
    

def get_now_showing(cinema):
    BASE_URL = "http://127.0.0.1:8080/v2/cinema/{}/now_showing".format(cinema)
    url = BASE_URL
    json_data=requests.get(url).json()
    return json_data['movies']

def get_timings(cinema, movie):
    BASE_URL = "http://127.0.0.1:8080/v2/cinema/{}/now_showing/{}".format(cinema,movie)
    url = BASE_URL
    json_data=requests.get(url).json()
    return json_data

"""functions for movies"""

def get_cinema(movie):
    BASE_URL = "http://127.0.0.1:8080/v2/movie/{}/cinema".format(movie)
    url = BASE_URL
    json_data=requests.get(url).json()
    return json_data['cinema_list']
    

def get_info(movie):
    BASE_URL = "http://127.0.0.1:8080/v2/movie/{}".format(movie)
    url = BASE_URL

    json_data=requests.get(url).json()
    print(json_data)
    return json_data


def get_movie_showing():
    BASE_URL = "http://127.0.0.1:8080/v2/movie"
    url = BASE_URL
    print(url)
    json_data=requests.get(url).json()
    print(json_data,"json data")
    return json_data['movies']
