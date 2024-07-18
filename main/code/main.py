import random
import multiprocessing as mp
import pygame

import GUI
import bacteria
import environment

environment = environment.Environment(5)
environment.createEnvironment()

animals = []
animalsCoordinates = []

processes = []
numberAnimals = 5


def firstClass(animals, coordinates, foodCoordinates, waterCoordinates): #Первый класс
    animal = bacteria.Bacteria(animals, coordinates, foodCoordinates, 1, waterCoordinates, 2, 10)
    return animal


def secondClass(animals, coordinates, foodCoordinates, waterCoordinates): #Второй класс
    animal = bacteria.Bacteria(animals, coordinates, foodCoordinates, 0.5, waterCoordinates, 2, 5)
    return animal


def thirstClass(animals, coordinates, foodCoordinates, waterCoordinates): #Третий класс
    animal = bacteria.Bacteria(animals, coordinates, foodCoordinates, 1, waterCoordinates, 1, 5)
    return animal


for i in range(0, numberAnimals): #Создание объектов класса бактерии
    animals.append(thirstClass(animals, [random.randint(10, 590), random.randint(10, 590)],
                                             environment.foodCoordinates,
                                             environment.waterCoordinates))

for i in animals:
    animalsCoordinates.append(i.coordinates)

window = GUI.GUI(environment.foodCoordinates, environment.waterCoordinates, 5, 10)
window.createGUI()
p = mp.Pool(16)

while 1:
    p.map_async(func=bacteria.Bacteria.main,iterable=animals)
    window.printGUI(animalsCoordinates)
    p.close()
    p.join()