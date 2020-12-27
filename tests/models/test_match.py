import unittest

from racha_app.models.match import Match
from racha_app.models.team import Team


class TestMatch(unittest.TestCase):

    def test_winner(self):
        home_team = Team(letter='H', tournament_id='123')
        away_team = Team(letter='J', tournament_id='123')
        match = Match(
            home_id='123',
            away_id='123',
            home_goals=4,
            away_goals=2,
            tournament_id='123'
        )
        match.home = home_team
        match.away = away_team

        winner = match.winner

        self.assertEqual(winner, home_team)

    def test_winner_when_draw(self):
        home_team = Team(letter='H', tournament_id='123')
        away_team = Team(letter='J', tournament_id='123')
        match = Match(
            home_id='123',
            away_id='123',
            home_goals=2,
            away_goals=2,
            tournament_id='123'
        )
        match.home = home_team
        match.away = away_team

        winner = match.winner

        self.assertEqual(winner, None)

    def test_assign_points_when_winner_exists(self):
        home_team = Team(letter='H', tournament_id='123')
        away_team = Team(letter='J', tournament_id='123')
        match = Match(
            home_id='123',
            away_id='123',
            home_goals=4,
            away_goals=2,
            tournament_id='123'
        )
        match.home = home_team
        match.away = away_team

        match.assign_points()

        self.assertEqual(home_team.points, 3)
        self.assertEqual(away_team.points, 0)

    def test_assign_points_when_draw(self):
        home_team = Team(letter='H', tournament_id='123')
        away_team = Team(letter='J', tournament_id='123')
        match = Match(
            home_id='123',
            away_id='123',
            home_goals=2,
            away_goals=2,
            tournament_id='123'
        )
        match.home = home_team
        match.away = away_team

        match.assign_points()

        self.assertEqual(home_team.points, 1)
        self.assertEqual(away_team.points, 1)
