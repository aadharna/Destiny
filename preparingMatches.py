import pandas as pd
from copy import deepcopy

def getAttributeList(matchdict):

    attributeCounter = {}
    attributeList = []

    randomMatch = list(matchdict.keys())[0]

    for i in range(len(matchdict[randomMatch])):
        tup = matchdict[randomMatch][i]
        if tup[0] in attributeCounter.keys():
            attributeCounter[tup[0]] += 1
        else:
            attributeCounter[tup[0]] = 0

        attributeList.append(tup[0] + str(attributeCounter[tup[0]]))

    for each_match in matchdict:
        for i in range(len(matchdict[each_match])):
            tup = matchdict[each_match][i]
            #attributeList.append(tup[0])
            matchdict[each_match][i] = tup[1]
        #break



        # for each_value in matchdict[each_match]:
        #     #print(each_value)
        #     attributeList.append(each_value[0])
        #     matchdict[each_match][0] = each_value[1]

    return attributeList

df = pd.read_csv("batch5Udacity.csv")

previousMatch = 0
counter = 0
match = {}
matches = []
temp = None
attributes = df.columns.values.tolist()
attributes.remove("percentContribution")

for index, row in df.iterrows():
    currentMatch = int(row["matchId"])

    # if int(row["activityDurationSeconds"]) < 150:
    #     None
    # else:

    if not currentMatch == previousMatch:
        counter += 1
        match[currentMatch] = []
    previousMatch = currentMatch

print(match)
print(counter)

#print(attributes)

for index, row in df.iterrows():

    currentMatch = int(row["matchId"])


    # if int(row["activityDurationSeconds"]) < 150:
    #     None
    # else:

    for attribute in attributes:
        # if not attribute == "Unnamed: 0":
            #print(attribute, row[attribute])
        match[currentMatch].append((attribute, row[attribute]))


#print(match)

OneTwentyMatches = {}
OneFortyMatches = {}
#OneSixtyMatches = {}
TwoFortyMatches = {}
TwoSixtyMatches = {}
TwoEightyMatches = {}



for each_match in match:
#     print(len(match[each_match]))
#
    # if len(match[each_match]) < 100:
    #     print(each_match)
    #     break

    temp = deepcopy(match[each_match])
    if len(match[each_match]) == 120:
        OneTwentyMatches[each_match] = temp
    elif len(match[each_match]) == 140:
        OneFortyMatches[each_match] = temp
    # elif len(match[each_match]) == 160:
    #     OneSixtyMatches[each_match] = temp
    elif len(match[each_match]) == 240:
        TwoFortyMatches[each_match] = temp
    elif len(match[each_match]) == 260:
        TwoSixtyMatches[each_match] = temp
    elif len(match[each_match]) == 280:
        TwoEightyMatches[each_match] = temp
    else:
        None

    matches.append(temp)

#print(match[868856111])

Columns120=getAttributeList(OneTwentyMatches)

df120 = pd.DataFrame.from_dict(OneTwentyMatches, orient="index")
df120.columns = Columns120

#print(df120.shape)

excess140 = ["Unnamed: 06", "activityDurationSeconds6", "assists6", "averageKillDistance6",
          "averageScorePerKill6", "averageScorePerLife6", "combatRating6", "completed6",
          "deaths6", "kills6", "killsDeathsAssists6", "killsDeathsRatio6", "matchId6",
          "score6", "standing6", "team6", "weaponKillsHeavy6", "weaponKillsOther6",
          "weaponKillsPrimary6", "weaponKillsSecondary6"]

Columns140=getAttributeList(OneFortyMatches)

df140 = pd.DataFrame.from_dict(OneFortyMatches, orient="index")
df140.columns = Columns140

df140.drop(excess140, axis=1, inplace=True)

df120 = df120.append(df140)

#print(df120.shape)


Columns240=getAttributeList(TwoFortyMatches)

df240 = pd.DataFrame.from_dict(TwoFortyMatches, orient="index")
df240.columns = Columns240

#print(df240.shape)

Columns260=getAttributeList(TwoSixtyMatches)

df260 = pd.DataFrame.from_dict(TwoSixtyMatches, orient="index")
df260.columns = Columns260

# for things in df260.columns.values.tolist():
#     print(things)

excess260 = ["Unnamed: 012", "activityDurationSeconds12", "assists12", "averageKillDistance12",
          "averageScorePerKill12", "averageScorePerLife12", "combatRating12", "completed12",
          "deaths12", "kills12", "killsDeathsAssists12", "killsDeathsRatio12", "matchId12",
          "score12", "standing12", "team12", "weaponKillsHeavy12", "weaponKillsOther12",
          "weaponKillsPrimary12", "weaponKillsSecondary12"]

df260.drop(excess260, axis=1, inplace=True)

df240 = df240.append(df260)

#print(df240.shape)

excess280 = ["Unnamed: 012", "activityDurationSeconds12", "assists12", "averageKillDistance12",
          "averageScorePerKill12", "averageScorePerLife12", "combatRating12", "completed12",
          "deaths12", "kills12", "killsDeathsAssists12", "killsDeathsRatio12", "matchId12",
          "score12", "standing12", "team12", "weaponKillsHeavy12", "weaponKillsOther12",
          "weaponKillsPrimary12", "weaponKillsSecondary12", "Unnamed: 013", "activityDurationSeconds13", "assists13", "averageKillDistance13",
          "averageScorePerKill13", "averageScorePerLife13", "combatRating13", "completed13",
          "deaths13", "kills13", "killsDeathsAssists13", "killsDeathsRatio13", "matchId13",
          "score13", "standing13", "team13", "weaponKillsHeavy13", "weaponKillsOther13",
          "weaponKillsPrimary13", "weaponKillsSecondary13"]

Columns280=getAttributeList(TwoEightyMatches)

df280 = pd.DataFrame.from_dict(TwoEightyMatches, orient="index")
df280.columns = Columns280

df280.drop(excess280, axis=1, inplace=True)

df240 = df240.append(df280)

#print(df240.shape)

df120.to_csv("indexByMatch_batch5Udacity_120.csv")
df240.to_csv("indexByMatch_batch5Udacity_240.csv")
print(float((df120.shape[0] + df240.shape[0]) / counter), " saved")