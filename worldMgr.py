# will handle the entities

import world

class WorldMgr:

    def __init__(self, engine):
        self.engine = engine
        self.world = world.World(self.engine)
        print("running world manager")

    def tick(self, delTime):
        self.world.tick(delTime)
