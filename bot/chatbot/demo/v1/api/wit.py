"""This file contains the main logic to handle the chatbot conversation
which depends on the intents receieved from wit.ai. If an exception occours,
the replies are handled by rivebot"""

from .credentials import TOKEN
import requests

import v1.api.cinema as cin
import v1.api.timeslot as times
import random

greeting=['Hello, human!','Hi','Hi there','hi user!']

import json
import os
from rivescript import RiveScript
file = os.path.dirname(__file__)
brain = os.path.join(file, 'brain')
bot = RiveScript()
bot.load_directory(brain)
bot.sort_replies()


conversations = {
  "name": 0,
  "tickets": 0,
  "timeslot": 0,
  "ttype": 0,
  "booking_id": 0,
  "intent": 0
}



flag = 0
def saving_Conversation(name, no_ticket,timeslot,ttype, booking_id, intent):
    if name!=0:
        conversations['name'] = name
    if no_ticket!=0:
        conversations['tickets'] = no_ticket 
    if timeslot!=0:
        conversations['timeslot'] = timeslot 
    if ttype!=0:
        conversations['ttype'] = ttype  
    if booking_id!=0:
        conversations['booking_id'] = booking_id
    if intent!=0:
        conversations['intent'] = intent
    json_object = json.dumps(conversations, indent = 4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    return {"message": "success"}


def load_Conversation():
    with open('sample.json', 'r') as openfile:
        
        json_object = json.load(openfile)
    return json_object


def ask_wit(expression):
    result = requests.get('https://api.wit.ai/message?v=20211122&q={}'.format(expression),
                        headers={'Authorization': TOKEN})

    jsonResult = result.json()
    print(jsonResult)
    global flag

    try:
        try:

            if  jsonResult['intents'][0]['name'] == 'Greetings':
                answer= "{},My name is Jake, I can with information related to movies or even booking tickets. What is your name?".format(random.choice(greeting))
                flag = 1

            elif jsonResult['intents'][0]['name'] == 'user':
                    user = jsonResult['entities']['wit$contact:contact'][0]['value']
                    answer= "Nice to meet you {} How can I help you today?".format(user)
                    conversations=load_Conversation()
                    saving_Conversation(user,conversations['tickets'],conversations['timeslot'],conversations['ttype'],conversations['booking_id'], conversations['intent'])
                    flag=0


            elif  jsonResult['intents'][0]['name'] == 'cinemainf':
                    name = jsonResult['entities']['wit$location:location'][0]['value']
                    cinema = cin.get_cinema_info(name)
                    answer= "{} is located at {} and the phone number is {}. What else would you like to know?".format(cinema['name'], cinema['address'], cinema['phone'])
                    flag=0

            elif  jsonResult['intents'][0]['name'] == 'address':
                    name = jsonResult['entities']['wit$location:location'][0]['value']
                    cinema = cin.get_cinema_info(name)
                    answer = "{} is located at {}".format(name, cinema['address'])
                    flag=0

            elif jsonResult['intents'][0]['name'] == 'phone':
                    name = jsonResult['entities']['wit$location:location'][0]['value']
                    cinema = cin.get_cinema_info(name)
                    answer = "you can reach {} at {}".format(name, cinema['phone'])
                    flag=0

            elif  jsonResult['intents'][0]['name'] == 'snacks':
                    name = jsonResult['entities']['wit$location:location'][0]['value']
                    cinema = cin.get_cinema_info(name)
                    answer = "You can have {} at".format(cinema['snacks'], name)
                    flag=0
            elif  jsonResult['intents'][0]['name'] == 'cinemalist':
                    cinema = cin.get_list_cinema()
                    answer = "You can watch movies at {}".format(cinema)
                    
                    flag=0

            elif  jsonResult['intents'][0]['name'] == 'movietime' or jsonResult['intents'][0]['name'] == 'booking':
                    cinema = jsonResult['entities']['wit$location:location'][0]['value']
                    movie = jsonResult['entities']['movie:movie'][0]['value']
                    cinema = cin.get_timings(cinema, movie)
                    answer = "{} is shown at {}. Which timeslot would you like to choose please enter the id".format(movie, cinema)
                    flag=0

            elif  jsonResult['intents'][0]['name'] == 'timeslot':
                    timeslot = jsonResult['entities']['wit$location:location'][0]['value']
                    answer= "How many tickets do you wish to buy?"
                    conversations=load_Conversation()
                    saving_Conversation(conversations['name'],conversations['tickets'],timeslot , conversations['ttype'],conversations['booking_id'], conversations['intent'])
                    flag=0

            elif  jsonResult['intents'][0]['name'] == 'tickets':
                    tickets = jsonResult['entities']['ticket:ticket'][0]['value']
                    answer= "We have gold_seats, platinum_seats and silver_seats. which one would you like?"

                    conversations=load_Conversation()
                    saving_Conversation(conversations['name'],tickets,conversations['timeslot'],conversations['ttype'],conversations['booking_id'], conversations['intent'])
                    flag=0

            elif  jsonResult['intents'][0]['name'] == 'ttype':
                    ttype = jsonResult['entities']['seats:seats'][0]['value']
                    answer= "would you like to confirm your booking?"

                    conversations=load_Conversation()
                    saving_Conversation(conversations['name'],conversations['tickets'],conversations['timeslot'],ttype,conversations['booking_id'], 'book')
                    flag=0
                 

            elif  jsonResult['intents'][0]['name'] == 'nowCinema':
                    cinema = jsonResult['entities']['wit$location:location'][0]['value']
                    movies = cin.get_now_showing(cinema)
                    list = ", ".join([x for x in movies[:-1]])
                    list = list + " or " + movies[-1]+ "'"
                    answer = "At {} you can watch {}".format(cinema, list)
                    flag=0

            elif  jsonResult['intents'][0]['name'] == 'get_cinemas':
                    list = cin.get_movie_showing()
                    answer = "You can watch movies at {}".format(list)
                    flag=0
                    

            elif  jsonResult['intents'][0]['name'] == 'movie_info':
                    movie = jsonResult['entities']['movie:movie'][0]['value']
                    list = cin.get_info(movie)
                    print(list)
                    answer = "{} is of {} genre and {} have acted in it".format(movie, list['genre'], list['cast'])
                    flag=0

            elif  jsonResult['intents'][0]['name'] == 'nowMovie' or 'nowshowing':
                    movies = cin.get_movie_showing()
                    list = ", ".join([x for x in movies[:-1]])
                    list = list + " and " + movies[-1]+ "'"
                    answer = "You can watch {} right now".format(list)
                    flag=0

            # elif  jsonResult['intents'][0]['name'] == 'nowshowing':
            #         print("yes")
            #         list = cin.get_movie_showing()
            #         answer = "These are the movies you can watch right now {}".format(list)
            #         flag=0
            
            elif jsonResult['intents'][0]['name'] == 'CancelBooking':
                    booking_id = jsonResult['entities']['booking_id:booking_id'][0]['value']
                    conversations=load_Conversation()
                    answer="Are you sure you want to cancel the booking_id {}, you cannot undo this".format(booking_id)
                    saving_Conversation(conversations['name'], conversations['ticket'], conversations['timeslot'], conversations['ttype'] , booking_id, 'cancel',)
                    flag=0


            elif jsonResult['intents'][0]['name'] == 'AnswerThanks':
                answer= "You are welcome!"

        except KeyError as err:
            answer = "I don't understand please try again:("

    except:
        answer = bot.reply('localusere',expression)
        print('rivebot',answer)

        if flag == 1:
            user = expression
            answer= "Nice to meet you {} what do you need?".format(user)
            conversations=load_Conversation()
            saving_Conversation(user,conversations['tickets'],conversations['timeslot'],conversations['ttype'], conversations['booking_id'], conversations['intent'])
            flag = 0
        conversations=load_Conversation()
        if conversations['intent']=='book':
            if "Yes" in answer:
                conversations=load_Conversation()
                booking = {conversations['name'],conversations['ticket'], conversations['timeslot'], conversations['ttype']}
                r = times.post_timeslot_movie(booking)
                answer = 'Dear {}. Your booking details are {}, we are waiting for you, see you! please remember the booking id in case you want to cancel the ticket'.format(conversations['name'],r )
            if "No" in answer:
                answer = 'No worries, see you!'

        if conversations['intent']=='cancel':

            if "Yes" in answer:
                conversations=load_Conversation()
                name={}
                name = {conversations['booking_id'], conversations['name']}
                r = times.patch_cancel_timeslot(name) 
                answer = 'Your appointment has been {}!'.format(r)
    
            if "No" in answer:
                answer = 'The booking has not been cancelled, can i help you with anything else!'


        if "ERR" in answer:
            answer = "I don't understand :("

    
    return answer
