class Team:

    id = None
    points = None
    letter = None
    tournament_id = None
    players = []

    def __init__(self, letter, tournament_id):
        self.points = 0
        self.letter = letter
        self.tournament_id = tournament_id

    def __str__(self):
        return f'Team {self.letter}: ' + ', '.join([p.name for p in self.players])

    def add_winner_points(self):
        self.points += 3

    def add_draw_points(self):
        self.points += 1
    