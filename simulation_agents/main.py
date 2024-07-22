import random
import multiprocessing as mp
import logging

import GUI
import bacteria
import environment
import metrics

environment = environment.Environment(5, 5)
environment.createEnvironment()

animals = []
animalsCoordinates = []

numberAnimals = 10

def methodWrapper(object: bacteria.Bacteria):
    object.main()


def firstClass(coordinates, foodCoordinates, waterCoordinates):  #Первый класс
    animal = bacteria.Bacteria(coordinates, foodCoordinates, 1, waterCoordinates, 2, 10)
    return animal


def secondClass(coordinates, foodCoordinates, waterCoordinates):  #Второй класс
    animal = bacteria.Bacteria(coordinates, foodCoordinates, 0.5, waterCoordinates, 2, 5)
    return animal


def thirstClass(coordinates, foodCoordinates, waterCoordinates):  #Третий класс
    animal = bacteria.Bacteria(coordinates, foodCoordinates, 1, waterCoordinates, 1, 5)
    return animal


for i in range(0, numberAnimals):  #Создание объектов класса бактерии
    animals.append(thirstClass([random.randint(10, 590), random.randint(10, 590)],
                               environment.foodCoordinates,
                               environment.waterCoordinates))


def main():
    window = GUI.GUI(environment.foodCoordinates, environment.waterCoordinates, 5, 5)
    window.createGUI()
    # p = mp.Pool(10)

    while True:
        methodWrapper([])
        window.printGUI([animals[0].coordinates])


main()
