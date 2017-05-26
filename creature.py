import random
import string

# TODO implement memory for food locations
# TODO implement smell function which will change direction to food


class Creature:

    def __init__(self, engine):
        self.engine = engine
        self.health = 100
        self.location = (2, 2)
        self.state = "idle"
        self.rate = 0
        self.direction = (0, 0)
        self.display = 'x'
        self.name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10))

    def __str__(self):
        temp = ""
        temp += "Location is: "
        temp += str(self.location)
        temp += "\nHealth: "
        temp += str(self.health)
        temp += "\nState: "
        temp += self.state
        temp += "\nDirection: "
        temp += str(self.direction[0]) + " " + str(self.direction[1])
        temp += "\n"
        return temp

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def tick(self, delTime):
        # print(type(self.location))
        self.health -= delTime
        self.rate += delTime
        if self.rate > 1:
            self.rate = 0
            if self.health < 0:
                self.engine.entityMgr.kill_ent(self)
            self.decision()
            print(self)

    def decision(self):
        if self.state == "idle":
            if self.health < 97:
                self.state = "hungry"
        elif self.health < 0:
                self.state = "dead"
        elif self.state == "hungry":
            if self.health > 97:
                self.state = "idle"
            self.search()

    def generatelocation(self):
        return 0, 0

    def eat(self):
        pass

    def idle(self):
        pass

    def move(self):
        oldLoc = self.location
        self.location = (self.location[0]+self.direction[0], self.location[1]+self.direction[1])
        if self.location[0] < 0 or self.location[0] > self.engine.worldMgr.world.worldSize or self.location[1] < 0 or self.location[1] > self.engine.worldMgr.world.worldSize:
            self.location = oldLoc
            self.direction = (random.randint(-1, 1), random.randint(-1, 1))
            self.move()

    def search(self):
        if self.direction == (0, 0):
            self.direction = (random.randint(-1, 1), random.randint(-1, 1))
        else:
            self.move()

    def smell(self):
        pass