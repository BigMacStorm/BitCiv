class World:

    def __init__(self, engine):
        self.engine = engine
        self.knowledge = []

    def tick(self, delTime):
        self.lifeTime += delTime
        print(self.lifeTime)

    def getKnowledge(self):
        # TODO implement this, iterate over entities and store info
        pass

    def printMap(self):
        # TODO print out map, to be used until viewer is implemented
        pass
