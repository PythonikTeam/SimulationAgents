import pygame
import sys

BLACK = (2, 1, 18)
WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
BLUE = (0, 191, 255)


class GUI:
    def __init__(self, foodCoordinates, waterCoordinates, foodAndWaterAmount, animalsAmount):
        self.rectAnimal = {}
        self.rectWater = {}
        self.rectFood = {}
        self.animalObject = None
        self.food = None
        self.water = None
        self.sc = None
        self.foodCoordinates = foodCoordinates
        self.waterCoordinates = waterCoordinates
        self.foodAndWaterAmount = foodAndWaterAmount
        self.animalsAmount = animalsAmount

    def createGUI(self):
        self.sc = pygame.display.set_mode((600, 600))

        pygame.font.init()

        self.animalObject = pygame.Surface((10, 10))
        self.animalObject.fill(BLACK)
        self.food = pygame.Surface((15, 15))
        self.food.fill(GREEN)
        self.water = pygame.Surface((15, 15))
        self.water.fill(BLUE)

        for r in range(0, self.animalsAmount):
            self.rectAnimal["rectAnimal" + str(r)] = self.animalObject.get_rect()

        for j in range(0, self.foodAndWaterAmount):
            if j == 0:
                i = 0
            else: i = 2

            self.rectFood["rectFood" + str(j)] = self.food.get_rect()
            self.rectWater["rectWater" + str(j)] = self.water.get_rect()
            self.rectFood["rectFood" + str(j)].x = self.foodCoordinates[j + i]
            self.rectWater["rectWater" + str(j)].x = self.waterCoordinates[j + i]
            self.rectFood["rectFood" + str(j)].y = self.foodCoordinates[j + i + 1]
            self.rectWater["rectWater" + str(j)].y = self.waterCoordinates[j + i + 1]

    def printGUI(self, animalCoordinates):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

        self.sc.fill(WHITE)

        # f1 = pygame.font.Font(None, 24)
        # text1 = f1.render(text1, 1, (180, 0, 0))
        # text2 = f1.render(text2, 1, (180, 0, 0))
        # text3 = f1.render(text3, 1, (180, 0, 0))

        for j in range(0, self.foodAndWaterAmount):
            self.sc.blit(self.food, self.rectFood["rectFood" + str(j)])
            self.sc.blit(self.water, self.rectWater["rectWater" + str(j)])

        for r in range(0, self.animalsAmount):
            self.sc.blit(self.animalObject, self.rectAnimal["rectAnimal" + str(r)])

        # self.sc.blit(text1, (10, 50))
        # self.sc.blit(text2, (10, 70))
        # self.sc.blit(text3, (10, 90))
        # print(animalCoordinates)

        for r in range(0, len(animalCoordinates) - 2):
            self.rectAnimal["rectAnimal" + str(r)].x = animalCoordinates[r][0]
            self.rectAnimal["rectAnimal" + str(r)].y = animalCoordinates[r][1]

        pygame.display.update()
