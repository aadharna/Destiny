import pandas as pd
from copy import deepcopy

def getAttributeList(matchdict):
    """

    :param matchdict: Dictionary of matches
    :return: FLATTENED attribute list for this match
    """

    attributeCounter = {}
    attributeList = []

    #pick the first person in the match and get the matchID
    randomMatch = list(matchdict.keys())[0]

    #For each person in the match break the Tuple which is storing their data
    #and make the first element into an attribute. Number the attributes by which
    #person in the match this is.
    #Person0 gets 0 added to all of their attributes.
    #Person 6 get 5 added to all of their attributes.
    for i in range(len(matchdict[randomMatch])):
        tup = matchdict[randomMatch][i]
        if tup[0] in attributeCounter.keys():
            attributeCounter[tup[0]] += 1
        else:
            attributeCounter[tup[0]] = 0

        attributeList.append(tup[0] + str(attributeCounter[tup[0]]))

    #For each person in the match
    for each_match in matchdict:
        #for each attribute for that person
        for i in range(len(matchdict[each_match])):
            tup = matchdict[each_match][i]

            #replace the ENTIRE tuple with the 2nd element of the tuple.
            matchdict[each_match][i] = tup[1]
        #break

        # for each_value in matchdict[each_match]:
        #     #print(each_value)
        #     attributeList.append(each_value[0])
        #     matchdict[each_match][0] = each_value[1]

    #return the list of attributes
    return attributeList


def getAlphaVic(dataframe):
    """

    :param dataframe: The entire frame of matches after having been flattened
    :return: the dataframe with a new variable
    """
    alphaVic = []

    #for each match in the dataframe
    for index, row in dataframe.iterrows():

        #if the first person indexed in the match is on team Alpha
        if row['team0'] == 16:
            #save their standing variable as alphaVictory
            alphaVic.append(row['standing0'])

        #If the first person is on team Bravo
        else:
            #Save the opposite of their standing variable as alphaVictory
            if row['standing0'] == 1:
                alphaVic.append(0)
            else:
                alphaVic.append(1)

    return dataframe.assign(alphaVictory=alphaVic)

#START HERE.
#

#Which batch file are you reading.
iteration = 1

df = pd.read_csv("batch" + str(iteration) + "Udacity.csv", index_col="Unnamed: 0")

previousMatch = 0
counter = 0
match = {}
#matches = []
temp = None
attributes = df.columns.values.tolist()


#For person in the dataframe
for index, row in df.iterrows():

    #save current match ID
    currentMatch = int(row["matchId"])

    # if int(row["activityDurationSeconds"]) < 150:
    #     None
    # else:

    #If current match ID does NOT equal the previous match
    if not currentMatch == previousMatch:

        #incriment counter
        counter += 1
        #create new match space in the matchDict
        match[currentMatch] = []

    #Set prevoiusly seen match as current match and repeat loop
    previousMatch = currentMatch


#visualize the match_dict and how many matches you have
print(match)
print(counter)

#print(attributes)


#for each match in the dataframe. Using the same MatchId Scheme as above
for index, row in df.iterrows():

    currentMatch = int(row["matchId"])


    # if int(row["activityDurationSeconds"]) < 150:
    #     None
    # else:

    #For each attribute in the dataframe
    for attribute in attributes:
        # if not attribute == "Unnamed: 0":
            #print(attribute, row[attribute])

        #save that person's stats as a tuple (attribute, number).
        match[currentMatch].append((attribute, row[attribute]))


#print(match)

#Create dicts to hold matches of different sizes.

OneTwentyMatches = {}
OneFortyMatches = {}
#OneSixtyMatches = {}
TwoFortyMatches = {}
TwoSixtyMatches = {}
TwoEightyMatches = {}


#For every match in match
for each_match in match:
#     print(len(match[each_match]))
#
    # if len(match[each_match]) < 100:
    #     print(each_match)
    #     break

    #Save the match and determine how many people were in said match.
    #Sort all of the matches according to the number of people in them.
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

    #matches.append(temp)

#print(match[868856111])

Columns120=getAttributeList(OneTwentyMatches)

df120 = pd.DataFrame.from_dict(OneTwentyMatches, orient="index")
df120.columns = Columns120

#-------------------------------------------------------------------------------------------------------
#
# The next small section cut out by dashes above and below repeats but for differening size matches.
# This removes the person who participated in the match and then left part way through.
#

excess140 = ["Unnamed: 06", "activityDurationSeconds6", "assists6", "averageKillDistance6",
          "averageScorePerKill6", "averageScorePerLife6", "combatRating6", "completed6",
          "deaths6", "kills6", "killsDeathsAssists6", "killsDeathsRatio6", "matchId6",
          "score6", "standing6", "team6", "weaponKillsHeavy6", "weaponKillsOther6",
          "weaponKillsPrimary6", "weaponKillsSecondary6"]

#individually index each person in the match
Columns140=getAttributeList(OneFortyMatches)

#Create a DataFrame of the 7-person matches
df140 = pd.DataFrame.from_dict(OneFortyMatches, orient="index")
df140.columns = Columns140

#Remove the extra person
df140.drop(excess140, axis=1, inplace=True)

#Add all 7-person matches to the 6-person dataframe.
df120 = df120.append(df140)



#----------------------------------------------------------------------------------------------------------
#12-PERSON MATCHES.
Columns240=getAttributeList(TwoFortyMatches)

df240 = pd.DataFrame.from_dict(TwoFortyMatches, orient="index")
df240.columns = Columns240


#----------------------------------------------------------------------------------------------------------
#13 PERSON MATCHES.
#Remove extra person and add them to the 12-person matches.
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

#----------------------------------------------------------------------------------------------------------
#14 PERSON MATCHES
# REMOVE extra person and add them to the 12-person Matches.

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

#----------------------------------------------------------------------------------------------------------



#Create AlphaVictory feature for each match in the 6 and 12 person matches.

df120 = getAlphaVic(df120)
df240 = getAlphaVic(df240)


#Remove Standing, matchId (now the index), and characterId from the dataframes.
for i in range(6):
    df120.drop("standing" + str(i), axis = 1, inplace=True)
    df120.drop("matchId" + str(i), axis = 1, inplace=True)
    df120.drop("Unnamed: 0" + str(i), axis=1, inplace=True)

for i in range(12):
    df240.drop("standing" + str(i), axis = 1, inplace=True)
    df240.drop("matchId" + str(i), axis = 1, inplace=True)
    df240.drop("Unnamed: 0" + str(i), axis=1, inplace=True)


#Save the dataframes according to the number of features present.

df120.to_csv("indexByMatch_batch" + str(iteration) + "Udacity_103.csv")

df240.to_csv("indexByMatch_batch" + str(iteration) + "Udacity_205.csv")


#Print to screen the percentage of data saved.
print(float((df120.shape[0] + df240.shape[0]) / counter), " saved")
#Pring the number of matches in both files.
print(df120.shape, df240.shape)