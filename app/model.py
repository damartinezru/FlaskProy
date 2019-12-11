# -*- coding: utf-8 -*-
class User(object):

    def __init__(self, name, email, nick, passwd):
        self._name = name
        self._email = email
        self._nick = nick
        self._pass = passwd

    def getName(self):
        return self._name

    def getEmail(self):
        return self._email

    def getNick(self):
        return self._nick

    def getPass(self):
        return self._pass
