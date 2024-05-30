import random
import time
import threading

import bacteria
import environment

environment = environment.Environment(200)
environment.createEnvironment()

animals = {}

threads = {}
numberAnimals = 10


def firstClass(animals, coordinates, foodCoordinates, waterCoordinates):
    animal = bacteria.Bacteria(animals, coordinates, foodCoordinates, 1, waterCoordinates, 2, 10)
    return animal


def secondClass(animals, coordinates, foodCoordinates, waterCoordinates):
    animal = bacteria.Bacteria(animals, coordinates, foodCoordinates, 0.5, waterCoordinates, 2, 5)
    return animal


def thirstClass(animals, coordinates, foodCoordinates, waterCoordinates):
    animal = bacteria.Bacteria(animals, coordinates, foodCoordinates, 1, waterCoordinates, 1, 5)
    return animal


# time.sleep(3)

for i in range(0, numberAnimals):
    animals["animal" + str(i)] = thirstClass(animals, [random.randint(10, 590), random.randint(10, 590)],
                                             environment.foodCoordinates,
                                             environment.waterCoordinates)

for j in range(0, numberAnimals - 3):
    threads[j] = threading.Thread(target=animals["animal" + str(j)].main)  # , args=(j))

for j in range(0, numberAnimals - 3):
    threads[j].start()

# print(f"{environment.foodCoordinates, environment.waterCoordinates} - Environment data.")

for j in range(0, numberAnimals - 3):
    threads[j].join()
