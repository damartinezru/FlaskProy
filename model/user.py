class User(object):

    def __init__(self):
        self._name = ""
        self._email = ""
        self._nick = ""
        self._pass = ""

    def getName(self):
        return self._name

    def getEmail(self):
        return self._email

    def getNick(self):
        return self._nick

    def getPass(self):
        return self._pass
