import unittest
import json
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_area(self):
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

    def test_display(self):
        s1 = Square(4)
        expected_output = "####\n####\n####\n####\n"
        with self.assertLogs() as logs:
            s1.display()
        self.assertEqual(logs.output, [expected_output])

    def test_str(self):
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 2/1 - 4")

    def test_update(self):
        s1 = Square(5, 10, 10)
        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 5")
        s1.update(89, 2)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 2")
        s1.update(89, 2, 3)
        self.assertEqual(str(s1), "[Square] (89) 3/10 - 2")
        s1.update(89, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 2")

    def test_update_kwargs(self):
        s1 = Square(5, 10, 10)
        s1.update(size=1)
        self.assertEqual(str(s1), "[Square] ({}) 10/10 - 1".format(s1.id))
        s1.update(x=2, size=3)
        self.assertEqual(str(s1), "[Square] ({}) 2/10 - 3".format(s1.id))
        s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(s1), "[Square] (89) 3/1 - 2")

    def test_to_dictionary(self):
        s1 = Square(10, 2, 9)
        s1_dict = s1.to_dictionary()
        self.assertEqual(s1_dict, {'id': 1, 'size': 10, 'x': 2, 'y': 9})
