from unittest import TestCase, main

from project.truck_driver import TruckDriver


class Test(TestCase):

    def setUp(self):
        self.test_driver = TruckDriver("Kris", 20)

    def test_correct_init(self):
        self.test_driver = TruckDriver('Kris', 20)
        self.assertEqual(self.test_driver.name, 'Kris')
        self.assertEqual(self.test_driver.money_per_mile, 20)
        self.assertEqual(self.test_driver.available_cargos, {})
        self.assertEqual(self.test_driver.earned_money, 0)
        self.assertEqual(self.test_driver.miles, 0)

    def test_earned_money_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.test_driver.earned_money = -1
        self.assertEqual(str(ve.exception), f"{self.test_driver.name} went bankrupt.")

    def test_bankrupt(self):
        self.test_driver.money_per_mile = 0.01
        self.test_driver.add_cargo_offer("California", 2000)
        with self.assertRaises(ValueError) as ve:
            self.test_driver.drive_best_cargo_offer()
        self.assertEqual(str(ve.exception), f"{self.test_driver.name} went bankrupt.")

    def test_add_cargo_offer(self):
        self.test_driver = TruckDriver('Kris', 20)
        result = self.test_driver.add_cargo_offer("Sofia", 150)
        self.assertEqual(result, 'Cargo for 150 to Sofia was added as an offer.')

        with self.assertRaises(Exception) as ve:
            self.test_driver.add_cargo_offer("Sofia", 150)
        self.assertEqual(str(ve.exception), 'Cargo offer is already added.')

    def test_drive_best_cargo_offer_real_offer(self):
        self.test_driver = TruckDriver('Kris', 20)
        self.test_driver.add_cargo_offer("Plovdiv", 200)
        self.test_driver.add_cargo_offer("Sofia", 150)
        result = self.test_driver.drive_best_cargo_offer()
        self.assertEqual(result, 'Kris is driving 200 to Plovdiv.')

    def test_drive_best_cargo_offer_no_offers(self):
        self.test_driver = TruckDriver('Kris', 20)
        result = self.test_driver.drive_best_cargo_offer()
        self.assertEqual(result, 'There are no offers available.')

    def test_eat(self):
        self.test_driver.earned_money = 100
        self.test_driver.eat(250)
        self.test_driver.eat(500)
        self.assertEqual(self.test_driver.earned_money, 60)

    def test_sleep(self):
        self.test_driver.earned_money = 100
        self.test_driver.sleep(1000)
        self.test_driver.sleep(2000)
        self.assertEqual(self.test_driver.earned_money, 10)

    def test_earned_gas(self):
        self.test_driver.earned_money = 1000
        self.test_driver.pump_gas(1500)
        self.assertEqual(self.test_driver.earned_money, 500)

    def test_repair_truck(self):
        self.test_driver.earned_money = 16000

        self.test_driver.repair_truck(10000)
        self.test_driver.repair_truck(20000)

        self.assertEqual(self.test_driver.earned_money, 1000)

    def test_drive_best_cargo_invalid(self):
        result = self.test_driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test__repr__(self):
        self.test_driver = TruckDriver('Kris', 20)
        self.test_driver.add_cargo_offer("Plovdiv", 200)
        self.test_driver.drive_best_cargo_offer()
        self.assertEqual(str(self.test_driver), "Kris has 200 miles behind his back.")


if __name__ == '__main__':
    main()
