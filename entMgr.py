# will handle the entities

import entity

class EntityMgr:

    def __init__(self, engine):
        self.engine = engine
        self.entList = []
        self.entList.append(entity.Entity(self.engine))
        print("running entity manager")

    def tick(self, delTime):
        for ent in self.entList:
            ent.tick(delTime)

