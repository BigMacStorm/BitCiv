from entity import Entity
import random


class Bit(Entity):

    def __init__(self, engine):
        self.engine = engine
        self.health = 100
        self.name = "bob"
        self.location = self.generate_location()
