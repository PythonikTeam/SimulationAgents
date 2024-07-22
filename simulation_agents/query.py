from loguru import logger
import numpy
import os

import tasks


os.remove("logs/query.log")
logger.add("logs/query.log", format="{level}: {message}")


class Query:
    def __init__(self, coordinates):
        logger.info("Query created")
        self.query = []
        self.coordinates = coordinates

    def addMoveTask(self, coordinates, target):
        self.query.append(tasks.Move(coordinates, target))
    def generatorMoveTasks(self, target, speed):
        speed = speed / 100

        c = numpy.array(self.coordinates)
        t = numpy.array(target)

        def tr(value, n):
            if value != 0:
                return value / n
            return 1

        def move(coordinate: numpy, targetCoords: numpy):
            gh = list(coordinate)
            x, y = (targetCoords - coordinate) / speed
            x, y = int(x), int(y)
            u, i = abs(x), abs(y)
            j, k = tr(x, u), tr(y, i)
            output = []
            for l in range(max(u, i) - 1):
                if l < u:
                    gh[0] += j * speed
                if l < i:
                    gh[1] += k * speed
                yield gh.copy()

        for x in move(c, t):
            self.addMoveTask(self.coordinates, [float(i) for i in x])
        self.addMoveTask(self.coordinates, target)
        for i in range(0, len(self.query)):
            self.startTask()

    def addEatTask(self):
        pass

    def startTask(self):
        self.query[0].start()
        del self.query[0]

