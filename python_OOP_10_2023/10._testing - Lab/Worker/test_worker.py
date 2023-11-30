from unittest import TestCase, main

from Worker.worker import Worker


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("TestGuy", 25000, 100)

    def test_correct_initialization(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(25000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_function(self):
        expected_money = self.worker.salary
        expected_energy = self.worker.energy - 1
        self.worker.work()

        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_work_raises_exception(self):
        self.worker.energy = 0  # arrange

        with self.assertRaises(Exception) as ex:
            self.worker.work()  # act

        self.assertEqual('Not enough energy.', str(ex.exception))  # assert

    def test_rest(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info(self):
        self.assertEqual(
            f'{self.worker.name} has saved {self.worker.money} money.',
            self.worker.get_info())


if __name__ == '__main__':
    main()
