import unittest

from racha_app.models.team import Team


class TestTeam(unittest.TestCase):

    def test_add_draw_points(self):
        team = Team(points=0, letter='H', tournament_id='123')

        team.add_draw_points()

        self.assertEqual(team.points, 1)

    def test_add_winner_points(self):
        team = Team(points=0, letter='H', tournament_id='123')

        team.add_winner_points()

        self.assertEqual(team.points, 3)
