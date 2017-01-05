import pandas as pd
import numpy as np
import nflgame

def determine_winner(away_score, home_score, away_team, home_team):
    if away_score > home_score:
        return away_team
    elif home_score > away_score:
        return home_team
    else:
        return 'TIE'

s = []
for yr in range(2009,2017):
    print yr
    games = nflgame.games(yr)

    for g in games:
        r = g.schedule
        r.update({'away_score':g.score_away})
        r.update({'home_score':g.score_home})
        s += [r]

all_games = pd.concat([pd.DataFrame.from_dict(x, orient = 'index').T for x in s])
all_games['WINNER'] = all_games.apply(lambda x: determine_winner(x['away_score'],x['home_score'], x['away'], x['home']), axis = 1)
all_games.to_csv('AllGames.csv', sep = ',', header = True, index = False)
