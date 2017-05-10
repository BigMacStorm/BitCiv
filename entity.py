class Entity:

    def __init__(self, engine):
        self.engine = engine
        self.lifeTime = 0

    def tick(self, delTime):
        self.lifeTime += delTime
        print(self.lifeTime)


