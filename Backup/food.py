import string
import random
from entity import Entity


class Food(Entity):

    def __init__(self, engine):
        self.engine = engine
        self.health = 1000
        self.location = self.generate_location()
        self.name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10))

