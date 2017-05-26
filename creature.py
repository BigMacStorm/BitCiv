import random
import string
import food

# TODO implement memory for food locations
# TODO implement smell function which will change direction to food


class Creature:

    def __init__(self, engine):
        self.engine = engine
        self.health = random.randint(80, 120)
        self.max_health = self.health
        self.location = self.generate_location()
        self.state = "idle"
        self.rate = 0
        self.detect_range = 2
        self.direction = (0, 0)
        self.display = 'x'
        self.hunger = 0.80
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
        self.health -= delTime
        self.rate += delTime
        if self.rate > self.engine.ent_refresh_rate:
            self.rate = 0
            if self.health < 0:
                self.engine.entityMgr.kill_ent(self)
            self.decision()
            print(self)

    def decision(self):
        if self.state == "idle":
            if self.health < self.hunger*self.max_health:
                self.state = "hungry"
            self.wander()
        elif self.health < 0:
            self.state = "dead"
        elif self.state == "hungry":
            search_here = self.find_food(self.location)
            if search_here != 0:
                self.eat(search_here)
            if self.health > self.hunger*self.max_health:
                self.state = "idle"
                self.direction = (0, 0)
            self.search()

    def wander(self):
        self.direction = (random.randint(-1, 1), random.randint(-1, 1))
        self.move()

    def generate_location(self):
        return random.randint(0, 10), random.randint(0, 10)

    def eat(self, found_food):
        difference = self.max_health - self.health
        found_food.health -= difference
        self.health += difference
        self.state = "idle"
        # add food to memory at this point, will help searching later

    def move(self):
        oldLoc = self.location
        self.location = (self.location[0]+self.direction[0], self.location[1]+self.direction[1])
        if self.location[0] < 0 or self.location[0] > self.engine.worldMgr.world.worldSize or \
           self.location[1] < 0 or self.location[1] > self.engine.worldMgr.world.worldSize:
            self.location = oldLoc
            self.direction = (random.randint(-1, 1), random.randint(-1, 1))
            self.move()

    def search(self):
        if self.direction == (0, 0):
            self.direction = (random.randint(-1, 1), random.randint(-1, 1))
        else:
            smell = self.sniff()
            if smell is not None:
                self.direction = self.engine.entityMgr.direction(self, smell)
                print("Smelt food, moving towards it: " + str(self.direction[0]) + " " + str(self.direction[1]))
            self.move()

    def find_food(self, location):
        for ent in self.engine.entityMgr.entList:
            if ent.location == location and isinstance(ent, food.Food):
                return ent
        return 0

    def sniff(self):
        best = None
        for x in range(-1*self.detect_range, self.detect_range+1):
            for y in range(-1*self.detect_range, self.detect_range+1):
                temp = self.find_food((self.location[0]+x, self.location[1]+y))
                if self.find_food((self.location[0]+x, self.location[1]+y)) != 0:
                    if best is None and temp is not 0:
                        best = temp
                    elif best is not None and temp is not 0:
                        if self.engine.entityMgr.distance(self, best) > self.engine.entityMgr.distance(self, temp):
                            best = temp
        return best

