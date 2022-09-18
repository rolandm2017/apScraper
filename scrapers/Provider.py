from enum import Enum

class Provider:
    rentCanada = "rentCanada"
    rentFaster = "rentFaster"
    rentSeeker = "rentSeeker"

    def __init__(self, source):
        self.type = source  # the only place this should really need to be defined.

    def get_type(self):
        return self.type