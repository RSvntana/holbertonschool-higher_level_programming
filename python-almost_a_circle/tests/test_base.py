import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def setUp(self):
        """Initialize common resources for tests"""
        self.base_instance = Base()

    def tearDown(self):
        """Clean up common resources after tests"""
        del self.base_instance

    def test_base__init(self):
        """Test the id attribute of the Base class"""
        b1 = Base()
        self.assertEqual(b1.id, self.base_instance.id + 1)

        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

        b3 = Base()
        self.assertEqual(b3.id, b2.id + 1)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, b3.id + 1)

    def test_create_rectangle(self):
        """Test the create method of the Rectangle class"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertIsInstance(r2, Rectangle)
        self.assertIsNot(r1, r2)

    def test_save_to_file_rectangle(self):
        """Test the save_to_file method of the Rectangle class"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(len(list_rectangles_input),
                         len(list_rectangles_output))
        self.assertIsInstance(list_rectangles_output[0], Rectangle)
        self.assertIsInstance(list_rectangles_output[1], Rectangle)

    def test_save_to_file_square(self):
        """Test the save_to_file method of the Square class"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

        self.assertEqual(len(list_squares_input), len(list_squares_output))
        self.assertIsInstance(list_squares_output[0], Square)
        self.assertIsInstance(list_squares_output[1], Square)

    def test_load_from_file(self):
        """Test the load_from_file method of the Base class"""
        # Complete the test logic according to your needs.


if __name__ == '__main__':
    unittest.main()
