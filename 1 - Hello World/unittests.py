"""
Check if your script is correct using this file.

Run in the command line by typing:
    python unittests.py

If you are in the PyCharm IDE, run this file by clicking the green arrow next to the main method:
    if __name__ == "__main__":
"""
import unittest
from helloworld import hello


class TestHello(unittest.TestCase):
    def test_steve(self):
        self.assertEqual("Hello Steve", hello("Steve"))

    def test_janette(self):
        self.assertEqual("Hello Janette", hello("Janette"))

    def test_lowercase_steve(self):
        self.assertEqual("Hello Steve", hello("steve"))

    def test_lowercase_janette(self):
        self.assertEqual("Hello Janette", hello("janette"))


if __name__ == "__main__":
    unittest.main()