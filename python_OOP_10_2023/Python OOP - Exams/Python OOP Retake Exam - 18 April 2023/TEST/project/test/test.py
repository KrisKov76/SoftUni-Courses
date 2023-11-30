from unittest import TestCase, main

from project.robot import Robot


class TestRobotClass(TestCase):
    def test_correct_init(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.assertEqual(self.robot.robot_id, "R1")
        self.assertEqual(self.robot.category, 'Education')
        self.assertEqual(self.robot.available_capacity, 200)
        self.assertEqual(self.robot.price, 100)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_wrong_category__should_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot = Robot('R1', 'Wrong', 200, 100)
        self.assertEqual(str(ve.exception),
                         "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_negative_price__should_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot = Robot('R1', 'Education', 200, -1)
        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_upgrade(self):
        self.robot = Robot('R1', 'Education', 200, 100)

        result = self.robot.upgrade('SSD1TB', 100)
        self.assertEqual(self.robot.hardware_upgrades, ['SSD1TB'])  # в self.robot.hardware_upgrades се появява 'SSD1TB'
        self.assertEqual(self.robot.price, 250)  # self.robot.price = 250
        self.assertEqual(result, 'Robot R1 was upgraded with SSD1TB.')

        result = self.robot.upgrade('RAM64', 100)
        self.assertEqual(result, 'Robot R1 was upgraded with RAM64.')
        self.assertEqual(self.robot.hardware_upgrades, ['SSD1TB', 'RAM64'])
        self.assertEqual(self.robot.price, 400)

        result = self.robot.upgrade('SSD1TB', 100)
        self.assertEqual(result, 'Robot R1 was not upgraded.')
        self.assertEqual(self.robot.hardware_upgrades, ['SSD1TB', 'RAM64'])
        self.assertEqual(self.robot.price, 400)

    def test_update(self):
        self.robot = Robot('R1', 'Education', 200, 100)

        result = self.robot.update(2.22, 50)
        self.assertEqual(self.robot.software_updates, [2.22])  # би следвало да се добави 2.22
        self.assertEqual(self.robot.available_capacity, 150)  # и капацитетът да падне до 200-50 = 150
        self.assertEqual(result, 'Robot R1 was updated to version 2.22.')

        result = self.robot.update(2.22, 50)
        self.assertEqual(self.robot.software_updates, [2.22])
        self.assertEqual(self.robot.available_capacity, 150)
        self.assertEqual(result, 'Robot R1 was not updated.')

    def test_gt1(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.other_robot = Robot('R2', 'Education', 200, 99.99)

        result = self.robot > self.other_robot
        self.assertEqual(result, 'Robot with ID R1 is more expensive than Robot with ID R2.')

    def test_gt2(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.other_robot = Robot('R2', 'Entertainment', 300, 100.9)

        result = self.robot > self.other_robot
        self.assertEqual(result, 'Robot with ID R1 is cheaper than Robot with ID R2.')

    def test_gt3(self):
        self.robot = Robot('R1', 'Education', 200, 100)
        self.other_robot = Robot('R2', 'Entertainment', 300, 100)

        result = self.robot > self.other_robot
        self.assertEqual(result, 'Robot with ID R1 costs equal to Robot with ID R2.')


if __name__ == '__main__':
    main()
