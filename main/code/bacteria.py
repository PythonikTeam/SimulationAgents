import math
import random
import sys
import time
import threading
import logging
from typing import Optional

from genes import Gene, GeneCluster

mutex = threading.Lock()

UP = -2
DOWN = 2
RIGHT = -1
LEFT = 1


logging.basicConfig(level=logging.DEBUG)


class Bacteria:
    def __init__(self, animals: Optional[list], coordinates, foodCoordinates,
                 foodCosts, waterCoordinates, waterCosts, speed, gui=True):
        """Init function"""
        self.status = 1
        self.hungry = 0
        self.thirst = 0
        self.need = 0
        self.speed = Gene(speed, 0.1)  # 5 координат в тик
        self.direction = self.direction = random.choice([-2, -1, 1, 2])
        self.animals = animals
        self.animalsCoordinates = []
        self.coordinates = coordinates
        self.foodCoordinates = foodCoordinates
        self.waterCoordinates = waterCoordinates
        self.tickWaterCost = Gene(waterCosts, 0.1)
        self.tickFoodCost = Gene(foodCosts, 0.1)
        self.nowTick = 0
        self.diedTime = 1000
        self.genes = GeneCluster([self.speed, self.tickWaterCost, self.tickFoodCost])
        self.gui = gui

        if self.gui:
            import GUI

            self.GUI = GUI.GUI(self.foodCoordinates, self.waterCoordinates, 4, 10)
            self.GUI.createGUI()

            for j in range(0, len(animals.keys())):
                # print(self.animalsCoordinates)
                self.animalsCoordinates.append(self.animals["animal" + str(j)].coordinates)

    def __str__(self):
        """Dunder(magic) method"""
        return ("Simulation Agents 1.11.8V""\n"
                f"Hungry - {self.hungry}""\n"
                f"Thirst - {self.thirst}""\n"
                f"Need - {self.need}""\n"
                f"Now tick - {self.nowTick}""\n"
                f"Coordinates - {self.coordinates}""\n"
                f"Food coordinates - {self.foodCoordinates}""\n"
                f"Water coordinates - {self.waterCoordinates}""\n"
                "___________________________")

    def calcDistance(self, targetCoordinates):
        """Function for calculating the distance between 2 points"""
        distanceToTarget = round(math.sqrt(abs(self.coordinates[0] - targetCoordinates[0]) ** 2 + abs(
            self.coordinates[1] - targetCoordinates[1]) ** 2))
        return distanceToTarget

    def everyTick(self):
        """Function, what works through every tick"""
        if self.hungry >= 200 or self.thirst >= 200:
            self.diedTime = self.nowTick
            self.status = 0
            sys.exit()
        self.nowTick += 1
        self.hungry += self.tickFoodCost.value
        self.thirst += self.tickWaterCost.value

    def detectNeed(self):
        """Function for detecting bacteria`s need."""
        if self.hungry == self.thirst or self.thirst == 0 and self.hungry == 0:
            randint = random.randint(0, 1)
            if randint == 0:
                self.need = 0
            elif randint == 1:
                self.need = 1
            return

        if self.thirst > self.hungry:
            self.need = 0
        else:
            self.need = 1

    def main(self):
        """Main function for starting the simulation"""
        while True:
            self.everyTick()
            self.detectNeed()
            if self.need == 0:
                self.goDrink()
            elif self.need == 1:
                self.goFood()
            elif self.need == 2:
                pass

    def move(self, targetCoordinates):
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

                if self.gui:
                    mutex.acquire()
                    self.GUI.printGUI([*self.animalsCoordinates, *self.coordinates])
                    mutex.release()
                    time.sleep(0.1)

                else:
                    pass

        else:
            if self.gui:
                mutex.acquire()
                self.GUI.printGUI([*self.animalsCoordinates, *self.coordinates])
                mutex.release()
            else:
                pass

    def doMove(self, targetCoordinates, speedX, speedY):
        """Function, what moves the bacteria"""
        distanceWhile = self.calcDistance(targetCoordinates)

        if round(distanceWhile) < self.speed.value:
            stop = 1
            return stop

        self.everyTick()

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

    def vision(self, Coordinates):
        """Function to check whether a point is in the field of view"""
        returnValue = {}

        for x, y in zip(Coordinates[::2], Coordinates[1::2]):
            distanceToTarget = self.calcDistance([x, y])
            if distanceToTarget < 100:
                returnValue[distanceToTarget] = [x, y]
        return returnValue

    def goFood(self) -> None:
        """Function for bacteria going to food"""
        distanceToCoordinatesList = self.vision(self.foodCoordinates)

        if distanceToCoordinatesList:
            key = min(distanceToCoordinatesList)

            closeFoodSource = distanceToCoordinatesList[key]
            self.move(closeFoodSource)
            if self.hungry - 30 <= 0:
                self.hungry = 0
            else:
                self.hungry -= 30

        else:
            self.direction = random.choice([-2, -1, 1, 2])

            while True:
                distanceToCoordinatesList = self.vision(self.foodCoordinates)
                if distanceToCoordinatesList: break
                self.findDirection()
            key = min(distanceToCoordinatesList)

            closeFoodSource = distanceToCoordinatesList[key]
            self.move(closeFoodSource)
            if self.hungry - 30 <= 0:
                self.hungry = 0
            else:
                self.hungry -= 30

    def goDrink(self) -> None:
        """Function for bacteria going to water"""
        distanceToCoordinatesList = self.vision(self.waterCoordinates)

        if distanceToCoordinatesList:
            key = min(distanceToCoordinatesList)

            closeWaterSource = distanceToCoordinatesList[key]
            self.move(closeWaterSource)

            if self.thirst - 30 <= 0:
                self.thirst = 0
            else:
                self.thirst -= 30

        else:
            self.direction = random.choice([-2, -1, 1, 2])

            while True:
                distanceToCoordinatesList = self.vision(self.waterCoordinates)
                if distanceToCoordinatesList: break
                self.findDirection()
            key = min(distanceToCoordinatesList)

            closeWaterSource = distanceToCoordinatesList[key]
            self.move(closeWaterSource)
            if self.thirst - 30 <= 0:
                self.thirst = 0
            else:
                self.thirst -= 30

    def goBreed(self) -> None:
        pass
