from main.bacteria import Bacteria
import unittest
import main.GUI


class TestBacteria(unittest.TestCase):
    def setUp(self):
        self.testAgent = Bacteria([10, 10], [20, 20], [20, 20], 5)
        self.testCoordinates = [20, 20]

    def test_vision(self):
        distance = self.testAgent.calcDistance(self.testCoordinates)
        self.assertEqual(distance, 14)

    def test_move(self):
        self.testAgent.move(self.testCoordinates)
        self.assertEqual(self.testAgent.coordinates, self.testCoordinates)

    def test_vision_result(self):
        distance, a, closeTargets = self.testAgent.vision(self.testCoordinates)
        self.assertEqual(distance, [14])
        self.assertEqual(a, [20, 20])
        self.assertEqual(closeTargets, [20, 20])

    def test_go_food(self):
        self.testAgent.goFood()
        self.assertEqual(self.testAgent.coordinates, [20, 20])

    def test_go_water(self):
        self.testAgent.goDrink()
        self.assertEqual(self.testAgent.coordinates, [20, 20])

if __name__ == '__main__':
    unittest.main()
