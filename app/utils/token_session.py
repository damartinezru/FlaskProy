# -*- coding: utf-8 -*-
import sys
import datetime
from utils.hash_verification import Hash

sys.path.append('.')
from model import User

class Token(object):
    def __init__(self):
        self._user = None
        self.token_value = ""

    # Token valid for max one hour
    def generate_token(self, nick, email):
        exact_time = datetime.datetime.now()
        self.token_value = Hash.hash_info(nick + email +str(datetime.date.today()) + str(exact_time.hour))
        return self.token_value

    def verify_token(self, exist_token, list_users):
        for user in list_users:
            exact_time = datetime.datetime.now()
            aux_generator_token = user["nick"] + user["email"] + str(datetime.date.today()) + str(exact_time.hour)
            if Hash.verify_two_hash(exist_token, aux_generator_token):
                self._user = User(user["name"], user["email"], user["nick"], user["hashed_passwd"])
                return True
        return False

    def getUser(self):
        return self._user
