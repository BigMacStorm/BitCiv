# will handle the entities

# TODO refactor entity class into both a creature class and a food class, maybe a block class
import creature


class EntityMgr:

    def __init__(self, engine):
        self.engine = engine
        self.entList = []
        self.entList.append(creature.Creature(self.engine))
        print("running entity manager")

    def tick(self, delTime):
        for ent in self.entList:
            ent.tick(delTime)

    def kill_ent(self, passed):
        self.entList.remove(passed)


