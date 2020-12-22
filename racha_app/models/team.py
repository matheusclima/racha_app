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
    

