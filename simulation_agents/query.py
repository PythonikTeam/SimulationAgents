import logging

import tasks
import metrics


logging.basicConfig(filename='logs/query.log', level=logging.INFO)


class Query:
    def __init__(self, coordinates):
        logging.info("Query created")
        self.query = []
        self.coordinates = coordinates

    def addMoveTask(self, coordinates, target):
        self.query.append(tasks.Move(coordinates, target))
    def generatorMoveTasks(self, target, speed):
        # TODO - Разделяем весь путь на кусочки по одному тику
        for i in range(0, len(self.query) - 1):
            self.startTask() #Запускаем все таски
        pass

    def startTask(self):
        self.query[-1].start()
        del self.query[-1]

query = Query([10, 10])
query.generatorMoveTasks([600, 600], 100)
print(query.coordinates)
