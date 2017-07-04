import random
import string
import food
import math

# TODO implement memory for food locations


class Creature:

    def __init__(self, engine):
        self.engine = engine
        self.max_health = random.randint(80, 120)
        self.breed_chance = random.randint(5, 9)
        self.matable = False
        self.mating_cooldown = random.randint(10,100)
        self.health = self.max_health * 0.5
        self.location = self.generate_location()
        self.state = "idle"
        self.rate = 0
        self.detect_range = 2
        self.direction = (0, 0)
        self.display = 'x'
        self.hunger = 0.7
        self.name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10))

    def __str__(self):
        temp = ""
        temp += "Name is: "
        temp += str(self.name)
        temp += "\nLocation is: "
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
            if self.mating_cooldown >= 0:
                self.mating_cooldown -= self.rate
            if self.health < 0:
                self.engine.entityMgr.kill_ent(self)
                self.engine.entityMgr.creature_count -= 1
            self.decision()
            self.rate = 0
            #print(self)

    def find_creature(self, location):
        for ent in self.engine.entityMgr.entList:
            if ent.location == location and isinstance(ent, Creature) and ent is not self and ent.matable:
                print("Found possible buddy")
                return ent
        return 0

    def find_distance(self, two):
        return math.sqrt(math.pow((two.location[0] - self.location[0]), 2) +
                         math.pow((two.location[1] - self.location[1]), 2))

    def find_direction(self, two):
        first = 0
        second = 0
        if two.location[0] > self.location[0]:
            first = 1
        elif two.location[0] < self.location[0]:
            first = -1
        if two.location[1] > self.location[1]:
            second = 1
        elif two.location[1] < self.location[1]:
            second = -1
        return first, second

    def decision(self):
        # this is a damn mess
        if self.mating_cooldown > 0:
            self.matable = False
        else:
            self.matable = True
        if self.state == "idle":
            if self.health < self.hunger*self.max_health:
                self.state = "hungry"
                self.matable = False
            nearby_friend = self.find_creature(self.location)
            if nearby_friend is not 0:
                print(nearby_friend)
                if random.randint(1, 10) > self.breed_chance and random.randint(1, 10) > nearby_friend.breed_chance:
                    self.engine.entityMgr.populate(1, 0)
                    self.mating_cooldown = random.randint(40, 100)
                    nearby_friend.mating_cooldown = random.randint(40, 100)
            self.wander()
        elif self.health < 0:
            self.state = "dead"
        elif self.state == "hungry":
            search_here = self.find_food(self.location)
            if search_here != 0:
                self.eat(search_here)
            if self.health > self.hunger*self.max_health:
                self.state = "idle"
                self.matable = True
                self.direction = (0, 0)
            self.search()

    def wander(self):
        self.direction = (random.randint(-1, 1), random.randint(-1, 1))
        self.move()

    def generate_location(self):
        return random.randint(0, self.engine.worldMgr.world.worldSize), \
               random.randint(0, self.engine.worldMgr.world.worldSize)

    def eat(self, found_food):
        difference = self.max_health - self.health
        found_food.health -= difference
        self.health += difference
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
                self.direction = self.find_direction(smell)
                #print("Smelt food, moving towards it: " + str(self.direction[0]) + " " + str(self.direction[1]))
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
                        if self.find_distance(best) > self.find_distance(temp):
                            best = temp
        return best

