import logging
import math
from decimal import Decimal

from metrics import metric


logging.basicConfig(filename='logs/tasks.log', level=logging.INFO)


class Task:
    instances = {}
    def __init__(self):
        Task.instances[self] = metric.counter
        metric.counter += 1
        logging.info(f"{Task.instances[self]} task created")

    def start(self):
        logging.info(f"{Task.instances[self]} task started")


    @staticmethod
    def distance(cords, targetCoords):
        return math.sqrt(Decimal(f"{cords[0] - targetCoords[0]}") ** 2 + (Decimal(f"{cords[1] - targetCoords[1]}") ** 2))
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

