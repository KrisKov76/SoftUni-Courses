import unittest

from project.railway_station import RailwayStation


class TestRailwayStation(unittest.TestCase):
    def setUp(self):
        self.station = RailwayStation("TestStation")

    def test_station_name_valid(self):
        self.assertEqual(self.station.name, "TestStation")

    def test_correct_init(self):
        station_name = "TestStation"
        station = RailwayStation(station_name)

        # Проверка на инициализацията
        self.assertEqual(station.name, station_name)
        self.assertListEqual(list(station.arrival_trains), [])
        self.assertListEqual(list(station.departure_trains), [])

    def test_station_name_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.station = RailwayStation('Stа')
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("Train_one")
        self.assertEqual(self.station.arrival_trains[-1], "Train_one")

    def test_new_arrival_on_board_order(self):
        station = RailwayStation("TestStation")

        # Примерни влакове
        train1, train2, train3 = "Express 101", "Local 102", "Regional 103"

        # Добавяне на влакове в дека с пристигащи влакове
        station.new_arrival_on_board(train1)
        station.new_arrival_on_board(train2)
        station.new_arrival_on_board(train3)

        # Проверка на реда на влаковете в списъка с пристигащи влакове
        self.assertListEqual(list(station.arrival_trains), [train1, train2, train3])


    def test_train_has_arrived_successful(self):
        station = RailwayStation("TestStation")
        # модел - has_arrived_successful
        station.new_arrival_on_board("Express 101")
        # резултат
        result = station.train_has_arrived("Express 101")
        self.assertEqual(result, "Express 101 is on the platform and will leave in 5 minutes.")

    def test_train_has_arrived_with_other_train_before(self):
        station = RailwayStation("TestStation")
        # модел - with_other_train_before
        station.new_arrival_on_board("Local 100")
        station.new_arrival_on_board("Express 101")
        # резултат
        result = station.train_has_arrived("Express 101")
        self.assertEqual(result, "There are other trains to arrive before Express 101.")

    def test_train_has_left_successful(self):
        station = RailwayStation("TestStation")
        # модел - влакът has_left_successful
        station.new_arrival_on_board("Express 101")
        station.train_has_arrived("Express 101")  # Преставяме влака в списъка с напускащи влакове
        # резултат
        result = station.train_has_left("Express 101")
        self.assertTrue(result)

    def test_train_has_left_unsuccessful(self):
        station = RailwayStation("TestStation")
        # модел - влакът has_left_unsuccessful
        station.new_arrival_on_board("Express 101")
        result = station.train_has_left("Express 101")
        # резултат
        self.assertFalse(result)

    def test_train_has_left_unscheduled_train(self):
        station = RailwayStation("TestStation")

        # Тест за напускащ влак, който не е пристигнал
        result = station.train_has_left("Express 101")
        self.assertFalse(result)
        self.assertListEqual(list(station.departure_trains), [])

    def test_train_order_in_deques(self):
        station = RailwayStation("TestStation")
        train1, train2, train3 = "Express 101", "Local 102", "Regional 103"

        # Пристигане на влакове в дека
        station.new_arrival_on_board(train1)
        station.new_arrival_on_board(train2)
        station.new_arrival_on_board(train3)

        # Проверка на реда на влаковете в списъка с пристигащи влакове
        self.assertListEqual(list(station.arrival_trains), [train1, train2, train3])

        # Пропускане на влакове
        station.train_has_arrived(train1)
        station.train_has_arrived(train2)
        station.train_has_arrived(train3)

        # Проверка на реда на влаковете в списъка с напускащи влакове
        self.assertListEqual(list(station.departure_trains), [train1, train2, train3])


if __name__ == '__main__':
    unittest.main()
