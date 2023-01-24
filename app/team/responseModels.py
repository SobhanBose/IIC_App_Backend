from app.team.schemas import Team

class ShowTeam(Team):
    class Config():
        orm_mode = True