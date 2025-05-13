from dataclasses import dataclass,field
class Innings:
    def __init__(self, id, batting_team_id, bowling_team_id):
        id: int
        batting_team_id: int
        bowling_team_id: int
        overs: list = field(default_factory=list)

    def add_over(self, over):
        self.overs.append(over)
