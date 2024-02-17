import unittest
import json
from models.base import Base

class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        Base._Base__nb_objects = 0
        r1 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        self.assertEqual(Base.to_json_string([r1]), json.dumps([r1]))

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        Base._Base__nb_objects = 0
        r1 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        self.assertEqual(Base.from_json_string(json.dumps([r1])), [r1])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_create(self):
        Base._Base__nb_objects = 0
        r1 = Base.create(id=1)
        self.assertIsInstance(r1, Base)
        self.assertEqual(r1.id, 1)

    def test_load_from_file(self):
        Base._Base__nb_objects = 0
        r1 = Base(1)
        r2 = Base(2)
        lst = [r1, r2]
        Base.save_to_file(lst)
        loaded = Base.load_from_file()
        self.assertIsInstance(loaded, list)
        self.assertEqual(len(loaded), 2)
        self.assertIsInstance(loaded[0], Base)
        self.assertEqual(loaded[0].id, 1)
        self.assertIsInstance(loaded[1], Base)
        self.assertEqual(loaded[1].id, 2)
