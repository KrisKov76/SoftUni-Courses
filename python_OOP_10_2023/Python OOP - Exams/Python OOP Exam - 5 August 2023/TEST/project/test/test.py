from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestTrip(TestCase):

    def setUp(self):
        # Инициализирайте вашата клас или обект преди всяко тестване
        self.test_car = SecondHandCar('Toyota', 'Sedan', 10000, 6000)

    def test_correct_init(self):
        self.assertEqual(self.test_car.model, 'Toyota')
        self.assertEqual(self.test_car.car_type, 'Sedan')
        self.assertEqual(self.test_car.mileage, 10000)
        self.assertEqual(self.test_car.price, 6000)

    def test_price(self):
        with self.assertRaises(ValueError) as ve:
            self.test_car = SecondHandCar('Toyota', 'Sedan', 10000, 1)
        self.assertEqual(str(ve.exception), 'Price should be greater than 1.0!')

    def test_mileage(self):
        with self.assertRaises(ValueError) as ve:
            self.test_car = SecondHandCar('Toyota', 'Sedan', 10, 6000)
        self.assertEqual(str(ve.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_promotional_price_successfully_set(self):
        result = self.test_car.set_promotional_price(2000)
        self.assertEqual(result, 'The promotional price has been successfully set.')

    def test_promotional_price_is_bigger(self):
        with self.assertRaises(ValueError) as ve:
            self.test_car = self.test_car.set_promotional_price(6001.0)
        self.assertEqual(str(ve.exception), 'You are supposed to decrease the price!')

    def test_need_repair_impossible(self):
        result = self.test_car.need_repair(6000, 'смяна на фар')
        self.assertEqual(result, 'Repair is impossible!')

    def test_need_repair_successfully(self):
        result = self.test_car.need_repair(100, 'смяна на фар')
        self.assertEqual(result, 'Price has been increased due to repair charges.')

    def test__str_mismatch(self):
        self.car1 = SecondHandCar('Toyota', 'Sedan', 10000, 6000)
        self.car2 = SecondHandCar('Toyota', 'Van', 10000, 6000)

        self.assertFalse(self.car1 == self.car2, "Cars cannot be compared. Type mismatch!")

    def test__gt__happy_case(self):
        self.car3 = SecondHandCar('Toyota', 'Sedan', 10000, 6000)
        self.car4 = SecondHandCar('Toyota', 'Sedan', 10000, 5000)

        self.assertTrue(self.car3 > self.car4)
        self.assertFalse(self.car4 > self.car3)

    def test__str__(self):
        self.car5 = SecondHandCar('Toyota', 'Sedan', 10000, 6000)
        self.car5.need_repair(200, 'something')
        self.assertEqual(str(self.car5), """Model Toyota | Type Sedan | Milage 10000km
Current price: 6200.00 | Number of Repairs: 1""")


if __name__ == '__main__':
    main()
