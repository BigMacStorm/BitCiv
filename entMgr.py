# will handle the entities


import creature
import food
import random


class EntityMgr:

    def __init__(self, engine):
        self.engine = engine
        self.entList = []
        self.food_spawn_rate = 2000000
        self.creature_count = 0
        self.food_count = 0
        self.populate()
        print("running entity manager")

    def tick(self, delTime):
        for ent in self.entList:
            ent.tick(delTime)
        if random.randint(0, self.food_spawn_rate) == 5:
            self.populate(0, 1)

    def kill_ent(self, passed):
        self.entList.remove(passed)

    def populate(self, creatures=8, foods=2):
        for x in range(creatures):
            self.entList.append(creature.Creature(self.engine))
            self.creature_count += 1
        for x in range(foods):
            self.entList.append(food.Food(self.engine))
            self.food_count += 1


