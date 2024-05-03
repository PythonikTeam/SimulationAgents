import random
import numpy as np

import environment
import base_agent


def sigmoid(x: float) -> float:
    return 1 / (1 + np.exp(-x))


class AI:
    def __init__(self):
        # Веса
        self.agents = {}
        self.animals = {}
        self.trainEnvironment = 0
        self.inputs = {}

        self.weights = {}
        for i in range(1, 25):
            self.weights["weight" + str(i)] = np.random.normal()

        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()
        self.b4 = np.random.normal()
        self.b5 = np.random.normal()
        self.b6 = np.random.normal()

    def feedforward(self, x):
        h1 = sigmoid(self.weights["weight1"] * x[0] + self.weights["weight2"] * x[1]
                     + self.weights["weight3"] * x[2] + self.weights["weight4"] * x[3] + self.b1)
        h2 = sigmoid(self.weights["weight5"] * x[0] + self.weights["weight6"] * x[1]
                     + self.weights["weight7"] * x[2] + self.weights["weight8"] * x[3] + self.b2)
        h3 = sigmoid(self.weights["weight9"] * x[0] + self.weights["weight10"] * x[1]
                     + self.weights["weight11"] * x[2] + self.weights["weight12"] * x[3] + self.b3)
        h4 = sigmoid(self.weights["weight13"] * x[0] + self.weights["weight14"] * x[1]
                     + self.weights["weight15"] * x[2] + self.weights["weight16"] * x[3] + self.b4)
        o1 = sigmoid(self.weights["weight17"] * h1 + self.weights["weight18"] * h2
                     + self.weights["weight19"] * h3 + self.weights["weight20"] * h4 + self.b5)
        o2 = sigmoid(self.weights["weight21"] * h1 + self.weights["weight22"] * h2
                     + self.weights["weight23"] * h3 + self.weights["weight24"] * h4 + self.b6)

        output = 0
        if o1 < o2:
            output = 1

        return output

    def train(self):
        i = 0
        j = 0

        self.agents = {}
        for k in range(1, 11):
            self.agents["agent" + str(k)] = AI

        # while j < 10000:
        self.trainEnvironment = environment.Environment(self.agents)
        self.trainEnvironment.createEnvironment()

        for r in range(1, 11):
            self.animals["animal" + str(r)] = base_agent.Animal([random.randint(100, 500),
                                                                random.randint(100, 500)],
                                                                self.trainEnvironment.foodCoordinates,
                                                                self.trainEnvironment.waterCoordinates, 5)

        self.inputs = {}
        for y in range(1, 11):
            self.inputs["inputs" + str(y)] = [self.animals["animal" + str(y)].hungry,
                                              self.animals["animal" + str(y)].thirst,
                                              base_agent.calcDistance(self.animals["animal" + str(y)].coordinates,
                                                                      self.trainEnvironment.foodCoordinates),
                                              base_agent.calcDistance(self.animals["animal" + str(y)].coordinates,
                                                                      self.trainEnvironment.foodCoordinates)]

        while i < 10:
            for r in range(1, 11):
                if self.agents["agent" + str(r)].feedforward(self.inputs["inputs" + str(r)]) == 0:
                    self.animals["animal" + str(r)].goFood()
                else:
                    self.animals["animal" + str(r)].goDrink()

                self.trainEnvironment.coordinates["coordinates" + str(r)] = self.animals["animal" + str(r)].coordinates


