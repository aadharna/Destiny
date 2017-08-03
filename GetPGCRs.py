import pandas as pd
import requests
import time
from copy import deepcopy
import MatchClass as MC

def combineTypeKills(PJR, i, gunType):
    """

    :param PJR: PGCR JSON
    :param i: Player Number
    :param gunType: Array specifying different types of guns
    :return: the number of kills that person got with all of the specified gun types.
    """

    used = []
    killcounter = 0

    all_keys = PJR['Response']['data']['entries'][i]['extended']['values'].keys()

    for guns in gunType:
        if guns in all_keys:
            used.append(guns)
    #print used

    for used_guns in used:
        killcounter += PJR['Response']['data']['entries'][i]['extended']['values'][used_guns]['basic']['value']

    #print counter
    return killcounter


def saveToDisk(matches):
    """

    :param matches: Dictionary containing ALL matches. Is MatchID indexed.
    :return: N/A
    """


    print("building dataframe")
    #first match
    df = pd.DataFrame.from_dict(matches[0].getMatch(), orient='index')

    #append the rest of the matches catalogued
    for i in range(1, len(matches)):
        df = df.append(pd.DataFrame.from_dict(matches[i].getMatch(), orient='index'))

    #print df.head(), df.shape

    #save the matches to a CSV
    df.to_csv('batch15Udacity.csv')
    print(df.shape)
    del matches[:]

weaponTypes = {}
weaponTypes["primary"] = ["weaponKillsAutoRifle", "weaponKillsScoutRifle", "weaponKillsHandCannon", "weaponKillsPulseRifle"]
weaponTypes["secondary"] = ["weaponKillsSniperRifle", "weaponKillsFusionRifle", "weaponKillsShotgun", "weaponKillsSidearm"]
weaponTypes["heavy"] = ["weaponKillsRocketLauncher", "weaponKillsMachineGun", "weaponKillsSwords"]
weaponTypes["other"] = ["weaponKillsGrenade", "weaponKillsSuper", "weaponKillsMelee"]


#STARTING POINT. SPECIFY WHICH BATCH YOU WANT TO START AT FROM DTR'S DATA.
Kernaldf = pd.read_csv("batch6.csv")
#print(df.head())

#Save the matchIDS
dflist = Kernaldf['instanceId'].tolist()
matches = []
skipped = 0
temp = None

#For all matches in the list of match IDS
for j in range(50000):

    #check point marker
    if j%2500 == 0:
        print("On match ", j)

    time.sleep(0.05) #in seconds. At 0.05, this results in 200 requests per 10 seconds.

    match = str(dflist[j])

    #URL to call
    PGCR_url = "http://www.bungie.net/Platform/Destiny/Stats/PostGameCarnageReport/" + match + "/"

    HEADERS = {"X-API-Key": "9a46d60a11174668977a76a28b729dd7"} #my personal Bungie-API key.

    #print("\n\n\nConnecting to Bungie: " + PGCR_url + "\n")
    #print("Fetching data for: PGCR!")
    res = requests.get(PGCR_url, headers=HEADERS)

    #If there was a problem, print out what the problem was and keep going.
    if "Response" not in res.json().keys():
        print(res.json()['Message'])
        skipped += 1
        continue

    #Get the total number of players in that match.
    totalplayerCount = int(res.json()['Response']['data']['entries'][0]['values']['playerCount']['basic']['value'])

    #For each person who participated in the match
    for i in range(totalplayerCount):

        #create a match object.
        singleMatch = MC.SingleMatch(match)

        #Get their CharacterId Number
        personId = res.json()['Response']['data']['entries'][i]['player']['destinyUserInfo']['membershipId']

        #Skip the person if they're missing important sub-dictionaries
        #Trying to work around the missing dicts is FAR TOO MUCH of a headache.
        if "team" not in res.json()['Response']['data']['entries'][i]['values'].keys() \
                or "extended" not in res.json()['Response']['data']['entries'][i].keys()\
                or "values" not in res.json()['Response']['data']['entries'][i].keys():
            skipped += 1
            continue
        else:
            #Specify their team.
            team = res.json()['Response']['data']['entries'][i]['values']['team']['basic']['displayValue']

        #If something went wrong, just skip this person and keep going.
        if team == '-':
            skipped += 1
            continue


        #BEGIN PULLING RELAVENT STATS FOR THIS PERSON.

        singleMatch.addPlayer(personId)
        singleMatch.addTeam(personId, team)
        singleMatch.addMatchIDtoPlayers(personId)

        singleMatch.addScore(personId, res.json()['Response']['data']['entries'][i]['score']['basic']['value'])
        singleMatch.addAVGScorePerLife(personId, res.json()['Response']['data']['entries'][i]['values']['averageScorePerLife']['basic']['value'])
        singleMatch.addKills(personId, res.json()['Response']['data']['entries'][i]['values']['kills']['basic']['value'])
        singleMatch.addAssists(personId, res.json()['Response']['data']['entries'][i]['values']['assists']['basic']['value'])
        singleMatch.addDeaths(personId, res.json()['Response']['data']['entries'][i]['values']['deaths']['basic']['value'])
        singleMatch.addStanding(personId, res.json()['Response']['data']['entries'][i]['values']['standing']['basic']['value'])
        singleMatch.addKD(personId,res.json()['Response']['data']['entries'][i]['values']['killsDeathsRatio']['basic']['value'])
        singleMatch.addKAD(personId, res.json()['Response']['data']['entries'][i]['values']['killsDeathsAssists']['basic']['value'])

        #For these three next stats, if they are not there, just skip it and make that spot NaN

        if ("averageKillDistance" not in res.json()['Response']['data']['entries'][i]['extended']['values'].keys()):
            None
        else:
            singleMatch.addAVG_K_DIST(personId, res.json()['Response']['data']['entries'][i]['extended']['values']['averageKillDistance']['basic']['value'])

        if ("averageScorePerKill" not in res.json()['Response']['data']['entries'][i]['extended']['values'].keys()):
            None
        else:
            singleMatch.addAVGScorePerKill(personId, res.json()['Response']['data']['entries'][i]['extended']['values']['averageScorePerKill']['basic']['value'])

        if ("combatRating" not in res.json()['Response']['data']['entries'][i]['extended']['values'].keys()):
            None
        else:
            singleMatch.addCR(personId, int(res.json()['Response']['data']['entries'][i]['extended']['values']['combatRating']['basic']['value']))

        #Get all weapon type kills.
        singleMatch.addPrimaries(personId, combineTypeKills(res.json(), i, weaponTypes["primary"]))
        singleMatch.addSecondaries(personId, combineTypeKills(res.json(), i, weaponTypes["secondary"]))
        singleMatch.addHeavy(personId, combineTypeKills(res.json(), i, weaponTypes["heavy"]))
        singleMatch.addAbilityKills(personId, combineTypeKills(res.json(), i, weaponTypes["other"]))

        #Get how long the match was and whether or not the person completed it.
        singleMatch.addActiveDuration(personId, int(res.json()['Response']['data']['entries'][i]['values']['activityDurationSeconds']['basic']['value']))
        singleMatch.addCompletion(personId, res.json()['Response']['data']['entries'][i]['values']['completionReason']['basic']['value'])

        #Make a copy that will last once the loop is done.
        temp = deepcopy(singleMatch)
        #Save the copy
        matches.append(temp)

        # if count%5 == 0:
        #     temp.display()


#Save the matches to disk.
saveToDisk(matches)
#Print out the amount of matches lost out of the 50,000.
print("num skipped =", skipped)