import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(3, 2)
        self.assertTrue(r.display() is None)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        r.update(89, 2)
        r.update(89, 2, 3)
        r.update(89, 2, 3, 4)
        r.update(89, 2, 3, 4, 5)

        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")


if __name__ == '__main__':
    unittest.main()
