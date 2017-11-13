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

# Adding @property to test. This was suggested on online help.
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
    def __init__(self):
        pass

    def perform_attempt(self):
        pass



class HangmanGame(object):

    def __init__(self):
        pass

    @classmethod
    def select_random_word(cls):
        pass

    def guess(self):
        pass

    def is_won(self):
        pass

    def is_finished(self):
        pass

    def is_lost(self):
        pass
    
