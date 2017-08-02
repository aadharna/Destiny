import pandas as pd
import requests
import time
from copy import deepcopy
import MatchClass as MC

def combineTypeKills(PJR, i, gunType):

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
    # for sm in matches:
    #     print sm.display()
    print("building dataframe")
    df = pd.DataFrame.from_dict(matches[0].getMatch(), orient='index')

    for i in range(1, len(matches)):
        df = df.append(pd.DataFrame.from_dict(matches[i].getMatch(), orient='index'))

    #print df.head(), df.shape

    df.to_csv('batch15Udacity.csv')
    print(df.shape)
    del matches[:]

weaponTypes = {}
weaponTypes["primary"] = ["weaponKillsAutoRifle", "weaponKillsScoutRifle", "weaponKillsHandCannon", "weaponKillsPulseRifle"]
weaponTypes["secondary"] = ["weaponKillsSniperRifle", "weaponKillsFusionRifle", "weaponKillsShotgun", "weaponKillsSidearm"]
weaponTypes["heavy"] = ["weaponKillsRocketLauncher", "weaponKillsMachineGun", "weaponKillsSwords"]
weaponTypes["other"] = ["weaponKillsGrenade", "weaponKillsSuper", "weaponKillsMelee"]


Kernaldf = pd.read_csv("batch6.csv")
#print(df.head())

#print(df['instanceId'])
dflist = Kernaldf['instanceId'].tolist()
matches = []
skipped = 0
temp = None

for j in range(50000):
    if j%2500 == 0:
        print("On match ", j)

    time.sleep(0.05) #in seconds. At 0.05, this results in 200 requests per 10 seconds.

    match = str(dflist[j])

    PGCR_url = "http://www.bungie.net/Platform/Destiny/Stats/PostGameCarnageReport/" + match + "/"

    HEADERS = {"X-API-Key": "9a46d60a11174668977a76a28b729dd7"} #my personal Bungie-API key.

    #print("\n\n\nConnecting to Bungie: " + PGCR_url + "\n")
    #print("Fetching data for: PGCR!")
    res = requests.get(PGCR_url, headers=HEADERS)

    if "Response" not in res.json().keys():
        print(res.json()['Message'])
        skipped += 1
        continue

    totalplayerCount = int(res.json()['Response']['data']['entries'][0]['values']['playerCount']['basic']['value'])

    for i in range(totalplayerCount):
        singleMatch = MC.SingleMatch(match)

        personId = res.json()['Response']['data']['entries'][i]['player']['destinyUserInfo']['membershipId']

        if "team" not in res.json()['Response']['data']['entries'][i]['values'].keys() \
                or "extended" not in res.json()['Response']['data']['entries'][i].keys()\
                or "values" not in res.json()['Response']['data']['entries'][i].keys():
            skipped += 1
            continue
        else:
            team = res.json()['Response']['data']['entries'][i]['values']['team']['basic']['displayValue']

        if team == '-':
            skipped += 1
            continue

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

        singleMatch.addPrimaries(personId, combineTypeKills(res.json(), i, weaponTypes["primary"]))
        singleMatch.addSecondaries(personId, combineTypeKills(res.json(), i, weaponTypes["secondary"]))
        singleMatch.addHeavy(personId, combineTypeKills(res.json(), i, weaponTypes["heavy"]))
        singleMatch.addAbilityKills(personId, combineTypeKills(res.json(), i, weaponTypes["other"]))

        singleMatch.addActiveDuration(personId, int(res.json()['Response']['data']['entries'][i]['values']['activityDurationSeconds']['basic']['value']))
        singleMatch.addCompletion(personId, res.json()['Response']['data']['entries'][i]['values']['completionReason']['basic']['value'])

        if len(res.json()['Response']['data']['teams']) == 2:

            if res.json()['Response']['data']['entries'][i]['values']['team']['basic']['displayValue'] == "Alpha":

                singleMatch.addpercentContrib(personId,
                                              singleMatch.getScore(personId),
                                              res.json()['Response']['data']['teams'][0]['score']['basic']['value'])
            else:
                singleMatch.addpercentContrib(personId,
                                              singleMatch.getScore(personId),
                                              res.json()['Response']['data']['teams'][1]['score']['basic']['value'])

        temp = deepcopy(singleMatch)
        matches.append(temp)

        # if count%5 == 0:
        #     temp.display()



saveToDisk(matches)
print("num skipped =", skipped)