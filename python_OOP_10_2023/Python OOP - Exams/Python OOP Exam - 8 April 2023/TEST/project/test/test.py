from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class Test_Object(TestCase):

    def test_correct_init(self):
        self.tennis_player = TennisPlayer('Kris', 47, 100)
        self.assertEqual(self.tennis_player.name, 'Kris')
        self.assertEqual(self.tennis_player.age, 47)
        self.assertEqual(self.tennis_player.points, 100)
        self.assertEqual(self.tennis_player.wins, [])

    def test_name(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = TennisPlayer('K', 47, 100)
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_age(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = TennisPlayer('Kris', 17, 100)
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_already_added(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.tennis_player.add_new_win('Australian Open 2023')
        self.assertEqual(self.tennis_player.wins, ['Australian Open 2023'])

        result = self.tennis_player.add_new_win('Australian Open 2023')
        self.assertEqual(result, 'Australian Open 2023 has been already added to the list of wins!')

    def test_add_new_win_added_successfully(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.tennis_player.add_new_win('Australian Open 2023')
        self.assertEqual(self.tennis_player.wins, ['Australian Open 2023'])

        self.tennis_player.add_new_win('French Open 2022')
        self.assertEqual(self.tennis_player.wins, ['Australian Open 2023', 'French Open 2022'])

    def test__it__first_test(self):
        player1 = TennisPlayer('Kris', 47, 100.0)
        player2 = TennisPlayer('Misho', 47, 200.0)

        result = player1 > player2
        self.assertEqual(result, 'Misho is a better player than Kris')

        result2 = player1 < player2
        self.assertEqual(result2, 'Misho is a top seeded player and he/she is better than Kris')

    def test__str__(self):
        self.tennis_player = TennisPlayer('Kris', 47, 100)
        self.tennis_player.add_new_win('Australian Open 2023')
        result = str(self.tennis_player)
        self.assertEqual(result, 'Tennis Player: Kris\nAge: 47\nPoints: 100.0\nTournaments won: Australian Open 2023')


if __name__ == '__main__':
    main()
