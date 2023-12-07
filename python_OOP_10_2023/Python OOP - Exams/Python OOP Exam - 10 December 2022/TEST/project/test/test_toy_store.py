import unittest

from project.toy_store import ToyStore


class TestToyStore(unittest.TestCase):
    def test_init(self):
        toy_store = ToyStore()

        # Проверка дали toy_shelf е инициализиран правилно
        expected_toy_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(toy_store.toy_shelf, expected_toy_shelf)

    def test_add_toy(self):
        toy_store = ToyStore()
        result = toy_store.add_toy('А', 'Мече')
        self.assertEqual(result, "Toy:Мече placed successfully!")

    def test_add_toy_invalid_shelf(self):
        toy_store = ToyStore()
        with self.assertRaises(Exception) as context:
            toy_store.add_toy("X", "Кукла")
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_add_toy_toy_already_in_shelf(self):
        toy_store = ToyStore()

        # Проверка за грешка при опит за добавяне на играчка, която вече е на полицата
        toy_store.add_toy("B", "Корабче")
        with self.assertRaises(Exception) as context:
            toy_store.add_toy("B", "Корабче")
        self.assertEqual(str(context.exception), "Toy is already in shelf!")

    def test_add_toy_shelf_already_taken(self):
        toy_store = ToyStore()

        # Проверка за грешка при опит за добавяне на играчка на вече заета полица
        toy_store.add_toy("C", "Машинка")
        with self.assertRaises(Exception) as context:
            toy_store.add_toy("C", "Машинка2")
        self.assertEqual(str(context.exception), "Shelf is already taken!")

    def test_remove_toy_success(self):
        toy_store = ToyStore()

        # Добавяне на играчка и след това успешно премахване
        toy_store.add_toy("D", "Dinosaur")
        result = toy_store.remove_toy("D", "Dinosaur")
        self.assertEqual(result, "Remove toy:Dinosaur successfully!")
        self.assertIsNone(toy_store.toy_shelf["D"])

    def test_remove_toy_invalid_shelf(self):
        toy_store = ToyStore()

        # Проверка за грешка при опит за премахване на играчка от невалидна полица
        with self.assertRaises(Exception) as context:
            toy_store.remove_toy("X", "Car")
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_remove_toy_toy_not_in_shelf(self):
        toy_store = ToyStore()

        # Проверка за грешка при опит за премахване на играчка, която не е на полицата
        toy_store.add_toy("F", "FairyTale")
        with self.assertRaises(Exception) as context:
            toy_store.remove_toy("F", "AdventureBook")
        self.assertEqual(str(context.exception), "Toy in that shelf doesn't exists!")


if __name__ == '__main__':
    unittest.main()
