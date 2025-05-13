from dataclasses import dataclass, field
from match_status import MatchStatus

@dataclass
class Match:
    id: int
    title: str
    venue: str
    start_time: datetime
    teams: list
    status: MatchStatus = field(default=MatchStatus.SCHEDULED)

    def set_status(self, status: MatchStatus):
        self.status = status
