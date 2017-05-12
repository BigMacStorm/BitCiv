# will handle the entities

import world

class WorldMgr:

    def __init__(self, engine):
        self.engine = engine
        self.world = world.World()
        print("running world manager")