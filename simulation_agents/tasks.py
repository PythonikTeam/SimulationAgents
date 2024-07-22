from loguru import logger
import math
import os
import sys

from metrics import metric


os.remove("logs/tasks.log")
logger.add("logs/tasks.log", format="{level}: {message}")


class Task:
    instances = {}
    def __init__(self):
        Task.instances[self] = metric.counter
        metric.counter += 1
        logger.info(f"{Task.instances[self]} task created")

    def start(self):
        logger.info(f"{Task.instances[self]} task started")


    @staticmethod
    def distance(cords, targetCoords):
        return math.sqrt(cords[0] - targetCoords[0] ** 2 + cords[1] - targetCoords[1] ** 2)
    @staticmethod
    def vision(coordinates, targetCoords, visionArea):
        if Task.distance(coordinates, targetCoords) <= visionArea: return True
        else: return False

class Move(Task):
    def __init__(self, coordinates, target):
        super().__init__()

        self.coordinates = coordinates
        self.target = target
        self.distance = super().distance

    def start(self):
        super().start()

        self.coordinates[0] = self.target[0]
        self.coordinates[1] = self.target[1]

class Eat(Task):
    def __init__(self, coordinates):
        super().__init__()

        self.coordinates = coordinates
