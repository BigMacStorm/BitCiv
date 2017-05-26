# engine is going to maintain all of the submodules, and will act as the root for the objects.

import entMgr
import worldMgr


class Engine:
    def __init__(self):
        self.worldMgr = worldMgr.WorldMgr(self)
        self.entityMgr = entMgr.EntityMgr(self)

        self.world_refresh_rate = 0.5
        self.ent_refresh_rate = 1
        self.world_size = 20

    def run(self):
        import time

        self.oldTime = time.time()
        while True:
            now = time.time()
            delTime = now - self.oldTime
            self.oldTime = now

            self.entityMgr.tick(delTime)
            self.worldMgr.tick(delTime)
