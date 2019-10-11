from ff_espn_api import League

class League_Data():

    @staticmethod
    def get_points_allowed_ranking(league):
        best_defense = sorted(league.teams, key=lambda x: x.points_against, reverse=True)
        return best_defense
