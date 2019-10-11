### Initial Start
from ff_espn_api import League
from ff_espn_api import Team

def main():
    league_id = 1180821
    year = 2018
    username = 'paarth_joshi@hotmail.com'
    password = 'Stevemcnair002'
    league = League(league_id, year, username, password)

    for team in league.teams:
        print(team.team_name)

if __name__ == "__main__":
    main()
    
