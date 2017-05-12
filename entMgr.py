# will handle the entities

# TODO refactor entity class into both a creature class and a food class, maybe a block class
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

