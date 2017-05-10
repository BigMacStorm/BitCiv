# engine is going to maintain all of the submodules, and will act as the root for the objects.

import entMgr

class Engine:
    def __init__(self):
        self.entityMgr = entMgr.EntityMgr(self)

    def run(self):
        import time

        self.oldTime = time.time()
        self.runTime = 0
        while(True):
            now = time.time()
            delTime = now - self.oldTime
            self.oldTime = now

            self.entityMgr.tick(delTime)
