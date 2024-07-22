from loguru import logger
import os

from genes import Gene, GeneCluster


os.remove("logs/bacterias.log")
logger.add("logs/bacterias.log", format="{level}: {message}")


class Bacteria:
    def __init__(self, coordinates: list[int],
                 foodCoordinates: list[int], foodCost: Gene,
                 waterCoordinates: list[int], waterCost: Gene,
                 visionDistance: Gene, speed: Gene):
        self.coordinates = coordinates
        self.foodCoordinates = foodCoordinates
        self.waterCoordinates = waterCoordinates
        self.foodCost = foodCost
        self.waterCost = waterCost
        self.visionDistance = visionDistance
        self.speed = speed
        self.geneCluster = GeneCluster([foodCost, waterCost, visionDistance, speed])

    def __str__(self):
        return ("Simulation Agents 1.9.0\n"
                "Type: Agent, bacteria")

