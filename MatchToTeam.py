import pandas as pd
import numpy as np
from copy import deepcopy

def integratePersonintoMatch(personStats, matchStats, currentMatch):
    if int(personStats["team"]) == 16:
        matchStats[currentMatch]["Alpha"]["standing"] = personStats["standing"]
        matchStats[currentMatch]["Alpha"]["MatchID"] = currentMatch

        matchStats[currentMatch]["Alpha"]["TeamAvgCR"].append(personStats["combatRating"])
        matchStats[currentMatch]["Alpha"]["TeamAvgAssists"].append(personStats["assists"])
        matchStats[currentMatch]["Alpha"]["TeamAvgScorePerKill"].append(personStats["averageScorePerKill"])
        matchStats[currentMatch]["Alpha"]["TeamAvgScorePerLife"].append(personStats["averageScorePerLife"])
        matchStats[currentMatch]["Alpha"]["TeamAvgDeaths"].append(personStats["deaths"])
        matchStats[currentMatch]["Alpha"]["TeamAvgKills"].append(personStats["kills"])
        matchStats[currentMatch]["Alpha"]["TeamAvgHeavyKills"].append(personStats["weaponKillsHeavy"])
        matchStats[currentMatch]["Alpha"]["TeamAvgSecondaryKills"].append(personStats["weaponKillsSecondary"])
        matchStats[currentMatch]["Alpha"]["TeamAvgPrimaryKills"].append(personStats["weaponKillsPrimary"])
        matchStats[currentMatch]["Alpha"]["TeamAvgOtherKills"].append(personStats["weaponKillsOther"])
        matchStats[currentMatch]["Alpha"]["TeamAvgScore"].append(personStats["score"])
        matchStats[currentMatch]["Alpha"]["TeamAvgKD"].append(personStats["killsDeathsRatio"])
        matchStats[currentMatch]["Alpha"]["TeamAvgKAD"].append(personStats["killsDeathsAssists"])
        matchStats[currentMatch]["Alpha"]["TeamAvgKillDist"].append(personStats["averageKillDistance"])

    elif int(personStats["team"]) == 17:
        matchStats[currentMatch]["Bravo"]["standing"] = personStats["standing"]
        matchStats[currentMatch]["Bravo"]["MatchID"] = currentMatch

        matchStats[currentMatch]["Bravo"]["TeamAvgCR"].append(personStats["combatRating"])
        matchStats[currentMatch]["Bravo"]["TeamAvgAssists"].append(personStats["assists"])
        matchStats[currentMatch]["Bravo"]["TeamAvgScorePerKill"].append(personStats["averageScorePerKill"])
        matchStats[currentMatch]["Bravo"]["TeamAvgScorePerLife"].append(personStats["averageScorePerLife"])
        matchStats[currentMatch]["Bravo"]["TeamAvgDeaths"].append(personStats["deaths"])
        matchStats[currentMatch]["Bravo"]["TeamAvgKills"].append(personStats["kills"])
        matchStats[currentMatch]["Bravo"]["TeamAvgHeavyKills"].append(personStats["weaponKillsHeavy"])
        matchStats[currentMatch]["Bravo"]["TeamAvgSecondaryKills"].append(personStats["weaponKillsSecondary"])
        matchStats[currentMatch]["Bravo"]["TeamAvgPrimaryKills"].append(personStats["weaponKillsPrimary"])
        matchStats[currentMatch]["Bravo"]["TeamAvgOtherKills"].append(personStats["weaponKillsOther"])
        matchStats[currentMatch]["Bravo"]["TeamAvgScore"].append(personStats["score"])
        matchStats[currentMatch]["Bravo"]["TeamAvgKD"].append(personStats["killsDeathsRatio"])
        matchStats[currentMatch]["Bravo"]["TeamAvgKAD"].append(personStats["killsDeathsAssists"])
        matchStats[currentMatch]["Bravo"]["TeamAvgKillDist"].append(personStats["averageKillDistance"])

    else:
        None


def averageTeams(matches):
    for matchId in  matches:
        for each_team in matches[matchId]:
            for each_stat in matches[matchId][each_team]:
                #print(each_team, each_stat, matches[match][each_team][each_stat])
                if np.average(matches[matchId][each_team][each_stat]) == "nan":
                    matches[matchId][each_team][each_stat] = 0
                else:
                    matches[matchId][each_team][each_stat] = np.average(matches[matchId][each_team][each_stat])

def saveToDisk(matches):

    df = pd.DataFrame.from_dict(matches[0], orient='index')

    for i in range(1, len(matches)):
        df = df.append(pd.DataFrame.from_dict(matches[i], orient='index'))


    df.to_csv('Team_batch9Udacity.csv')
    print(df.shape)



df = pd.read_csv("batch9Udacity.csv")

print(df.shape)

matches = []
previousMatch = 0
temp = None
#matchIds = []
match_buckets = {}

for index, row in df.iterrows():

    currentMatch = int(row["matchId"])
    if not currentMatch == previousMatch:
        #matchIds.append(currentMatch)


        match_buckets[currentMatch] = {}
        match_buckets[currentMatch]["Alpha"] = {}
        match_buckets[currentMatch]["Bravo"] = {}

        match_buckets[currentMatch]["Alpha"]["TeamAvgCR"] = []
        match_buckets[currentMatch]["Alpha"]["TeamAvgAssists"] = []
        match_buckets[currentMatch]["Alpha"]["TeamAvgScorePerKill"] = []
        match_buckets[currentMatch]["Alpha"]["TeamAvgScorePerLife"] = []
        match_buckets[currentMatch]["Alpha"]["TeamAvgDeaths"] = []
        match_buckets[currentMatch]["Alpha"]["TeamAvgKills"] = []
        match_buckets[currentMatch]["Alpha"]["TeamAvgHeavyKills"] = []
        match_buckets[currentMatch]["Alpha"]["TeamAvgSecondaryKills"] = []
        match_buckets[currentMatch]["Alpha"]["TeamAvgPrimaryKills"] = []
        match_buckets[currentMatch]["Alpha"]["TeamAvgOtherKills"] = []
        match_buckets[currentMatch]["Alpha"]["TeamAvgScore"] = []
        #match_buckets[currentMatch]["Alpha"]["Standing"]  = []
        match_buckets[currentMatch]["Alpha"]["TeamAvgKD"] = []
        match_buckets[currentMatch]["Alpha"]["TeamAvgKAD"] = []
        match_buckets[currentMatch]["Alpha"]["TeamAvgKillDist"] = []

        match_buckets[currentMatch]["Bravo"]["TeamAvgCR"] = []
        match_buckets[currentMatch]["Bravo"]["TeamAvgAssists"] = []
        match_buckets[currentMatch]["Bravo"]["TeamAvgScorePerKill"] = []
        match_buckets[currentMatch]["Bravo"]["TeamAvgScorePerLife"] = []
        match_buckets[currentMatch]["Bravo"]["TeamAvgDeaths"] = []
        match_buckets[currentMatch]["Bravo"]["TeamAvgKills"] = []
        match_buckets[currentMatch]["Bravo"]["TeamAvgHeavyKills"] = []
        match_buckets[currentMatch]["Bravo"]["TeamAvgSecondaryKills"] = []
        match_buckets[currentMatch]["Bravo"]["TeamAvgPrimaryKills"] = []
        match_buckets[currentMatch]["Bravo"]["TeamAvgOtherKills"] = []
        match_buckets[currentMatch]["Bravo"]["TeamAvgScore"] = []
        #match_buckets[currentMatch]["Bravo"]["Standing"]  = []
        match_buckets[currentMatch]["Bravo"]["TeamAvgKD"] = []
        match_buckets[currentMatch]["Bravo"]["TeamAvgKAD"] = []
        match_buckets[currentMatch]["Bravo"]["TeamAvgKillDist"] = []

    previousMatch = currentMatch

for index, row in df.iterrows():
    currentMatch = int(row["matchId"])
    integratePersonintoMatch(row, match_buckets, currentMatch)




#print(match_buckets)
#print(len(matchIds))
averageTeams(match_buckets)

for matchIDS in match_buckets:
    temp = deepcopy(match_buckets[matchIDS])
    matches.append(temp)


saveToDisk(matches)