#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        self.assertEqual(str(self.model),
                         "[BaseModel] ({}) {}".format(
                             self.model.id, self.model.__dict__))

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        self.assertEqual(self.model.to_dict()["__class__"], "BaseModel")
        self.assertIsInstance(self.model.to_dict()["created_at"], str)
        self.assertIsInstance(self.model.to_dict()["updated_at"], str)


if __name__ == '__main__':
    unittest.main()
