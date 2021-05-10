import sys

class Slow_network_exception(Exception):
    def __init__(self, expression, message):
        self.expression= expression
        self.message= message
        print("WEBSITE LOADING TOO SLOW")