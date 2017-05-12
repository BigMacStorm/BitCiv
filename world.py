class World:

    def __init__(self, engine):
        self.engine = engine
        self.knowledge = {}
        self.worldSize = 10
        self.rate = 0

    def tick(self, delTime):
        self.rate += delTime
        if self.rate > 3:
            self.rate = 0
            self.getknowledge()
            self.printMap()

    def getknowledge(self):
        self.knowledge = {}
        for ent in self.engine.entityMgr.entList:
            self.knowledge[ent.location] = ent.display
            print("Adding char to mem")

    def printMap(self):
        print("=========================")
        for x in range(0, 10):
            for y in range(0, 10):
                if (x, y) in self.knowledge:
                    print(self.knowledge[(x, y)], end='')
                else:
                    print(" ", end='')
            print('')
        print("=========================")
