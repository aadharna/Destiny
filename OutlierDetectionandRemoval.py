import pandas as pd
import numpy as np

def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result


#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________
#DETERMINE OUTLIERS


df1 = pd.read_csv("batchUdacity_TOTAL.csv", index_col="Unnamed: 0")
df1.fillna(-1, inplace=True)
print(df1.head(), df1.shape)

# Display the outliers
outliers = []

for feature in df1.columns:
    #Calculate Q1 (10th percentile of the data) for the given feature
    Q1 = np.percentile(df1[feature], 10)

    #Calculate Q3 (90th percentile of the data) for the given feature
    Q3 = np.percentile(df1[feature], 90)

    #Use the interquartile range to calculate an outlier step (1.5 times the interquartile range)
    step = (Q3 - Q1) * (1.5)

    print(Q1, Q3, step, " for features --", feature)

    #print("Data points considered outliers for the feature, ", feature)
    #display(df[~((df[feature] >= Q1 - step) & (df[feature] <= Q3 + step))])
    outliers.append(df1[~((df1[feature] >= Q1 - step) & (df1[feature] <= Q3 + step))].index.values)

# print(outliers)
for arrays, names in zip(outliers, df1.columns):
    print(names, len(arrays))

outlierdict = {}
outlierdict.clear()
highoutlierlist = []

for arrays in outliers:
    for people in arrays:
        if people in outlierdict.keys():
            outlierdict[people] += 1
        else:
            outlierdict[people] = 1

for key in outlierdict.keys():
    if outlierdict[key] > 2:
        #print(key, outlierdict[key])
        highoutlierlist.append(key)


print(len(highoutlierlist))
print(float(len(highoutlierlist)/df1.shape[0]))


outlierMatches = []
removal = []
previousMatch = 0
counter = 0
match = {}
#matches = []
temp = None
attributes = df1.columns.values.tolist()
print(len(attributes))
#attributes.remove("percentContribution")

for index, row in df1.iterrows():
    currentMatch = int(row["matchId"])

    if index in highoutlierlist:
        if currentMatch not in outlierMatches:
            outlierMatches.append(currentMatch)
        continue

    if not currentMatch == previousMatch:
        counter += 1
        match[currentMatch] = []
    previousMatch = currentMatch

for index, row in df1.iterrows():
    currentMatch = int(row["matchId"])

    if currentMatch in outlierMatches:
        removal.append(index)

good_data = df1.drop(df1.index[removal]).reset_index(drop=True)

good_data.to_csv("batchUdacity_CLEANED.csv")
