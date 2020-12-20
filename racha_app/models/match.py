class Match:

    id = None
    team_1 = None
    team_2 = None
    goal_1 = None
    goal_2 = None
    day = None

    def __init__(self, team_1, team_2, goal_1, goal_2, day):
        self.team_1 = team_1
        self.team_2 = team_2
        self.goal_1 = goal_1
        self.goal_2 = goal_2
        self.day = day