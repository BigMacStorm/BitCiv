# will handle the entities

import bit
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

    def populate(self):
        for x in range(0, 5):
            self.entList.append(bit.Bit(self.engine))
        for x in range(0, 5):
            self.entList.append(food.Food(self.engine))

    def kill_ent(self, ent):
        print(ent.name + "has died.")
        self.entList.remove(ent)
