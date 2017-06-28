# will handle the entities


import creature
import food


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


