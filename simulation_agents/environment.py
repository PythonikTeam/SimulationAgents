from GUI import *
import random


class Environment:
    def __init__(self, amountAgents):
        self.coordinates = {}
        self.amountAgents = amountAgents
        self.foodCoordinates = []
        self.waterCoordinates = []

    def createEnvironment(self):
        for i in range(0, self.amountAgents):
            self.coordinates["coordinates" + str(i)] = random.randint(10, 590), random.randint(10, 590)

        for i in range(0, 4):
            self.foodCoordinates.extend([random.randint(10, 590), random.randint(10, 590)])
            self.waterCoordinates.extend([random.randint(10, 590), random.randint(10, 590)])

        # print(self.foodCoordinates, self.waterCoordinates)
