### Initial Start
from ff_espn_api import League
from ff_espn_api import Team
from business_logic.league_data import League_Data

def main():
    league_id = 246927
    year = 2018
    username = 'paarth_joshi@hotmail'
    password = 'vemcnair002'
    league = League(league_id, year, username, password)

    best_defense = League_Data.get_points_allowed_ranking(league)
    for t in best_defense:
        print(t.team_name + " " + t.points_against)

if __name__ == "__main__":
    main()
    
