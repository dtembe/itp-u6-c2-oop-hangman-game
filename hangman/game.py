from .exceptions import *
import random


class GuessAttempt(object):
    def __init__(self, alphabet, hit=None, miss=None):
        self.alphabet = alphabet
        self.hit = hit
        self.miss = miss

        if hit:
            if miss:
                raise InvalidGuessAttempt()

# Adding @property to test. This was suggested online help.
# TODO - read about @property on python docs.

    @property
    def is_hit(self):
        if self.hit is None:
            self.hit = False

        return self.hit

    @property
    def is_miss(self):
        if self.miss is None:
            self.miss = False

        return self.miss


class GuessWord(object):
    pass


class HangmanGame(object):
    pass
