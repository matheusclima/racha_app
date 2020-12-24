class Team:

    id = None
    points = None
    letter = None
    tournament_id = None
    players = []

    def __init__(self, points, letter, tournament_id):
        self.points = points
        self.letter = letter
        self.tournament_id = tournament_id

    def __str__(self):
        return f'Team {self.letter}: ' + ', '.join([p.name for p in self.players])

    def add_winner_points(self):
        self.points += 3

    def add_draw_points(self):
        self.point += 1
    