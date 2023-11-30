import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "Test type", "test sound")

    def test_init(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("Test type", self.mammal.type)
        self.assertEqual("test sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", result)

if __name__ == '__main__':
    unittest.main()
