import bacteria
import math
import random

UP = -2
DOWN = 2
RIGHT = -1
LEFT = 1


class Phage:
    def __init__(self, bacterias, type, coordinates, chanceToImplementation):
        self.speed = 2.5
        self.direction = 2
        self.type = type
        self.bacterias = bacterias
        self.liveBacterias = []
        self.chanceToImplementation = chanceToImplementation
        self.energy = 100
        self.coordinates = coordinates

    def move(self, targetCoordinates: list[int]) -> None:
        """Function for agent move"""
        coordinates = []
        distance = self.calcDistance(targetCoordinates)

        if distance < 1:
            return

        speedX = abs(self.coordinates[0] - targetCoordinates[0]) / (distance / self.speed.value)
        speedY = abs(self.coordinates[1] - targetCoordinates[1]) / (distance / self.speed.value)

        # print(f"{self.foodCoordinates, self.waterCoordinates} - Agent data")

        if distance > 1:
            while True:
                if self.doMove(targetCoordinates, speedX, speedY) == 1:
                    break

    def doMove(self, targetCoordinates, speedX, speedY):
        """Function, what moves the bacteria"""
        distanceWhile = self.calcDistance(targetCoordinates)

        if round(distanceWhile) < self.speed.value:
            stop = 1
            return stop

        if self.coordinates[0] < targetCoordinates[0]:
            self.coordinates[0] = self.coordinates[0] + speedX
        else:
            self.coordinates[0] = self.coordinates[0] - speedX

        if self.coordinates[1] < targetCoordinates[1]:
            self.coordinates[1] = self.coordinates[1] + speedY
        else:
            self.coordinates[1] = self.coordinates[1] - speedY

    def findDirection(self):
        """Function for finding a direction"""
        if self.coordinates[0] + 10 > 600:
            self.move([self.coordinates[0] - self.speed.value, self.coordinates[1]])
            self.direction = random.choice([LEFT, UP, DOWN])
        if self.coordinates[0] - 10 < 0:
            self.move([self.coordinates[0] + self.speed.value, self.coordinates[1]])
            self.direction = random.choice([RIGHT, UP, DOWN])

        if self.coordinates[1] + 10 > 600:
            self.move([self.coordinates[0], self.coordinates[1] - self.speed.value])
            self.direction = random.choice([UP, RIGHT, LEFT])
        if self.coordinates[1] - 10 < 0:
            self.move([self.coordinates[0], self.coordinates[1] + self.speed.value])
            self.direction = random.choice([DOWN, RIGHT, LEFT])

        # print(self.randRotation)

        if self.direction == RIGHT:
            self.move([self.coordinates[0] + self.speed.value, self.coordinates[1]])
        elif self.direction == LEFT:
            self.move([self.coordinates[0] - self.speed.value, self.coordinates[1]])
        elif self.direction == DOWN:
            self.move([self.coordinates[0], self.coordinates[1] + self.speed.value])
        elif self.direction == UP:
            self.move([self.coordinates[0], self.coordinates[1] - self.speed.value])

    def calcDistance(self, targetCoordinates: list[int]) -> list[int]:
        distanceToTarget = round(math.sqrt(abs(self.coordinates[0] - targetCoordinates[0]) ** 2 + abs(
            self.coordinates[1] - targetCoordinates[1]) ** 2))
        return distanceToTarget

    def attachment(self):
        bacteriasCoordinates = []
        bacteriasDistances = []

        for i in self.bacterias.keys():
            if self.bacterias[i].status == 1:
                self.liveBacterias.append(self.bacterias[i])

        for j in self.liveBacterias:
            bacteriasCoordinates.append(j.coordinates)

        for k in bacteriasCoordinates:
            bacteriasDistances.append(self.calcDistance(k))

        target = self.bacterias[bacteriasDistances.index(min(bacteriasDistances))]
        if min(bacteriasDistances) * 0.5 < self.energy:
            self.move(target.coordinates)
            self.energy -= min(bacteriasDistances) * 0.5
        else: pass

