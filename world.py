

class World:

    def __init__(self, engine):
        self.engine = engine
        self.knowledge = {}
        self.worldSize = 15
        self.rate = 0

    def tick(self, delTime):
        self.rate += delTime
        if self.rate > self.engine.world_refresh_rate:
            self.rate = 0
            self.getknowledge()
            self.printMap()
            print(self.engine.entityMgr.creature_count)
            print(self.engine.entityMgr.food_count)

    def getknowledge(self):
        self.knowledge = {}
        for ent in self.engine.entityMgr.entList:
            self.knowledge[ent.location] = ent.display

    def printMap(self):
        print("=========================")
        for x in range(0, self.worldSize+1):
            for y in range(0, self.worldSize+1):
                print(" ", end='')
                if (x, y) in self.knowledge:
                    print(self.knowledge[(x, y)], end='')
                else:
                    print("_", end='')
            print('')
        print("=========================")
