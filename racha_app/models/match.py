class Match:

    id = None
    home_id = None
    away_id = None
    home_goals = None
    away_goals = None
    tournament_id = None
    home = None
    away = None

    def __init__(self, home_id, away_id, home_goals, away_goals, tournament_id):
        self.home_id = home_id
        self.away_id = away_id
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.tournament_id = tournament_id

    @property
    def winner(self):
        if self.home_goals > self.away_goals:
            return self.home

        if self.away_goals > self.home_goals:
            return self.away

        return None

    def assign_points(self):
        if self.winner:
            self.winner.add_winner_points()
        else:
            self.home.add_draw_points()
            self.away.add_draw_points()
