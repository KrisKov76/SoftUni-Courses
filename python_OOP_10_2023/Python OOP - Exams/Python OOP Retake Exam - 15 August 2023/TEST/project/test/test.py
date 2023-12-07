from unittest import TestCase, main

from project.trip import Trip


class TestTrip(TestCase):
    def test_correct_init(self):
        self.trip = Trip(10000, 2, False)
        self.assertEqual(self.trip.budget, 10000)
        self.assertEqual(self.trip.travelers, 2)
        self.assertEqual(self.trip.is_family, False)
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {})

    def setUp(self):
        # Инициализирайте вашата клас или обект преди всяко тестване
        self.trip = Trip

    def test_at_least_one_traveler_is_required(self):
        with self.assertRaises(ValueError) as ve:
            self.trip = Trip(10000, 0, False)
        self.assertEqual(str(ve.exception), 'At least one traveler is required!')

    def test_is_family_wrong_(self):
        self.trip = Trip(200, 1, True)
        self.assertFalse(self.trip.is_family)

    def test_book_a_trip_invalid_destination(self):
        trip = Trip(10000, 3, True)
        result = trip.book_a_trip('Czech republic')
        self.assertEqual(result, 'This destination is not in our offers, please choose a new one!')

    def test_book_a_trip_valid_destination(self):
        trip2 = Trip(10000, 1, True)
        result = trip2.book_a_trip('New Zealand')
        self.assertEqual(result, 'Successfully booked destination New Zealand! Your budget left is 2500.00')

    def test_book_a_trip_not_enough_budget(self):
        trip3 = Trip(10000, 2, True)
        result = trip3.book_a_trip('New Zealand')
        self.assertEqual(result, 'Your budget is not enough!')

    def test_booking_status_no_bookings_yet(self):
        trip4 = Trip(10000, 2, True)
        trip4.book_a_trip('New Zealand')
        result = trip4.booking_status()
        self.assertEqual(result, 'No bookings yet. Budget: 10000.00')

    def test_booking_status_successfully_booking(self):
        trip4 = Trip(10000, 1, True)
        trip4.book_a_trip('New Zealand')
        result = trip4.booking_status()
        self.assertEqual(result, '''Booked Destination: New Zealand
Paid Amount: 7500.00
Number of Travelers: 1
Budget Left: 2500.00''')


if __name__ == '__main__':
    main()
