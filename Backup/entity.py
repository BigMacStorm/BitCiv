import string
import random


class Entity:

    def __init__(self, engine):
        self.engine = engine
        self.health = 100
        self.name = "bob"
        self.location = self.generate_location()

    def __str__(self):
        temp = ""
        temp += "Location is: "
        temp += str(self.location)
        temp += "\nHealth: "
        temp += str(self.health)
        temp += "\n"
        return temp

    def tick(self, delTime):
        self.health -= delTime
        if self.health < 0:
            self.engine.entityMgr.kill_ent(self)
        print(self)

    def generate_location(self):
        return random.uniform(0, self.engine.worldMgr.world.worldSize), \
               random.uniform(0, self.engine.worldMgr.world.worldSize)

