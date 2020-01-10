import unittest

from src import crayon


class TestTrue(unittest.TestCase):
    def test_import(self):
        self.assertTrue(crayon)

    def test_true(self):
        self.assertTrue(True)
