import unittest
import json
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

    def test_area(self):
        r1 = Rectangle(3, 5)
        self.assertEqual(r1.area(), 15)

    def test_display(self):
        r1 = Rectangle(4, 6)
        expected_output = "####\n####\n####\n####\n####\n####\n"
        with self.assertLogs() as logs:
            r1.display()
        self.assertEqual(logs.output, [expected_output])

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] ({}) 10/10 - 10/1".format(r1.id))
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] ({}) 2/10 - 1/1".format(r1.id))
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict, {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})
