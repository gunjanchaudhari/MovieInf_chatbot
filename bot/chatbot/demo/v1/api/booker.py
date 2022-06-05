"""This file is where the chatbot input is recieved. 
the expression(input) is passed to ask_wit() function 
and the reply recieved is sent back to the chatbot """

from flask import g

from . import Resource
from .wit import ask_wit

class Booker(Resource):

    def get(self):
        expression = g.args.get("expression")
        print("User says: %s" % expression)
        answer = ask_wit(expression)
        print("Returned answer: {}".format(answer))
        return {'answer': answer}, 200, None
