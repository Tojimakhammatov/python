

import unittest
from circle import getArea, getPerimeter

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(4), 50.26544,3)
        self.assertEqual(getArea(3), 28.27431)
        self.assertEqual(getArea(2), 12.56636)
    
    def test_area(self):
        self.assertAlmostEqual(getPerimeter(4), 25.13272, 2)
        self.assertEqual(getPerimeter(2), 12.56636)


unittest.main()
