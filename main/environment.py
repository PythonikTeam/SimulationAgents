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

        self.foodCoordinates.extend([247, 91, 171, 551, 239, 202, 465, 373, 316, 128])

        self.waterCoordinates.extend([211, 351, 295, 81, 430, 407, 404, 374, 120, 481])

        # print(self.foodCoordinates, self.waterCoordinates)
