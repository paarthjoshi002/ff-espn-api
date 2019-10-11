### Initial Start
from ff_espn_api import League
from ff_espn_api import Team

def main():
    league_id = 246927
    year = 2018
    username = 'paarth_joshi@hotmail'
    password = 'vemcnair002'
    league = League(league_id, year, username, password)

    for team in league.teams:
        print(team.team_name)

if __name__ == "__main__":
    main()
    
