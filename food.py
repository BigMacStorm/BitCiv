import string
import random


class Food:

    def __init__(self, engine):
        self.engine = engine
        self.health = 1000
        self.location = self.generate_location()
        self.rate = 0
        self.display = 'o'
        self.name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10))

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
        self.rate += delTime
        if self.rate > self.engine.ent_refresh_rate:
            self.rate = 0
            if self.health < 0:
                self.engine.entityMgr.kill_ent(self)
                self.engine.entityMgr.food_count -= 1
            #print(self)

    def generate_location(self):
        return random.randint(0, self.engine.worldMgr.world.worldSize), \
               random.randint(0, self.engine.worldMgr.world.worldSize)

