# will handle the entities

# TODO refactor entity class into both a creature class and a food class, maybe a block class
import creature
import food
import math


class EntityMgr:

    def __init__(self, engine):
        self.engine = engine
        self.entList = []
        self.populate()
        print("running entity manager")

    def tick(self, delTime):
        for ent in self.entList:
            ent.tick(delTime)

    def kill_ent(self, passed):
        self.entList.remove(passed)

    def populate(self, creatures=4, foods=2):
        for x in range(creatures):
            self.entList.append(creature.Creature(self.engine))
        for x in range(foods):
            self.entList.append(food.Food(self.engine))

    def distance(self, one, two):
        return math.sqrt(math.pow((two.location[0] - one.location[0]), 2) +
                         math.pow((two.location[1] - one.location[1]), 2))

    def direction(self, one, two):
        first = 0
        second = 0
        if two.location[0] > one.location[0]:
            first = 1
        elif two.location[0] < one.location[0]:
            first = -1
        if two.location[1] > one.location[1]:
            second = 1
        elif two.location[1] < one.location[1]:
            second = -1
        print("Found")
        print(first)
        print(second)
        return first, second


