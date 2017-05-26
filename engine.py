# engine is going to maintain all of the submodules, and will act as the root for the objects.

import entMgr
import worldMgr

class Engine:
    def __init__(self):
        self.entityMgr = entMgr.EntityMgr(self)
        self.worldMgr = worldMgr.WorldMgr(self)

        self.world_refresh_rate = 0.5
        self.ent_refresh_rate = 1

    def run(self):
        import time

        self.oldTime = time.time()
        self.runTime = 0
        while(True):
            now = time.time()
            delTime = now - self.oldTime
            self.oldTime = now

            self.entityMgr.tick(delTime)
            self.worldMgr.tick(delTime)
