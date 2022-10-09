#!/usr/bin/python3
"""Tests for Base class."""


import re
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests of Base class."""
    def test_base_type(self):
        """Tests Base's type."""
        obj = Base()
        self.assertTrue(isinstance(obj, Base))

    def test_base_docs(self):
        """Tests Base's documentations."""
        mod_docs = "models.base".__doc__
        self.assertTrue(len(mod_docs) > 1)

        class_docs = Base.__doc__
        self.assertTrue(len(class_docs) > 1)

    @classmethod
    def setUpClass(cls):
        """Sets up tests' environment."""
        Base._Base__nb_objects = 0
        cls.base1 = Base()
        cls.base2 = Base()
        cls.base3 = Base(id=25)

    def test_obj_id(self):
        """Tests Base's id."""
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 2)
        self.assertEqual(self.base3.id, 25)

    def test_base_to_json_string(self):
        """Tests to JSON string methods."""
        test_dict = {"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}
        result = Base.to_json_string(test_dict)
        self.assertTrue(isinstance(result, str))
        result = Base.to_json_string(None)
        self.assertEqual(result, '[]')
        result = Base.to_json_string([])
        self.assertEqual(result, '[]')

    def test_base_from_json_string(self):
        """Tests from JSON string method."""
        result = Base.from_json_string(None)
        self.assertEqual(result, [])
        self.assertTrue(isinstance(result, list))
        result = Base.from_json_string('[]')
        self.assertEqual(result, [])
        self.assertTrue(isinstance(result, list))
        result = Base.from_json_string('[{"id": 1, "width": 10}]')
        self.assertTrue(isinstance(result, list))
        self.assertEqual(result, [{"id": 1, "width": 10}])


if __name__ == "__main__":
    unittest.main()
