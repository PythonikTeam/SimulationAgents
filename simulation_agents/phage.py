import bacteria
import math
import random

UP = -2
DOWN = 2
RIGHT = -1
LEFT = 1


class Phage:
    def __init__(self, bacterias, type, coordinates, chanceToImplementation):
        self.type = type
        self.bacterias = bacterias
        self.liveBacterias = []
        self.chanceToImplementation = chanceToImplementation
        self.energy = 100
        self.coordinates = coordinates

    def attachment(self):
        pass
