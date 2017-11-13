from .exceptions import *
import random


class GuessAttempt(object):
    def __init__(self, alphabet, hit=None, miss=None):
        self.alphabet = alphabet
        self.hit = hit
        self.miss = miss

        if hit and miss:
            raise InvalidGuessAttempt()

    def is_hit(self):
        if self.hit == None:
            self.hit = False

        return self.hit

    def is_miss(self):
        if self.miss == None:
            self.miss = False

        return self.miss


class GuessWord(object):
    pass


class HangmanGame(object):
    pass
