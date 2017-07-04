# engine is going to maintain all of the submodules, and will act as the root for the objects.

import entMgr
import worldMgr
import configMgr


class Engine:
    def __init__(self):
        self.configMgr = configMgr.ConfigMgr(self)
        self.worldMgr = worldMgr.WorldMgr(self)
        self.entityMgr = entMgr.EntityMgr(self)

        self.world_refresh_rate = 1
        self.ent_refresh_rate = 0.5
        self.world_size = 10
        self.oldTime = 0;

    def run(self):
        import time

        self.oldTime = time.time()
        while True:
            now = time.time()
            self.entityMgr.tick(now - self.oldTime)
            self.worldMgr.tick(now - self.oldTime)
            self.oldTime = now

