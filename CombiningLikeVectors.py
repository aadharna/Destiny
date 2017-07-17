import pandas as pd

def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

FileNameP1 = "indexByMatch_batch"
FileNameP2 = "Udacity_103"
FileNameP3 = "Udacity_205"
SUFFIX = ".csv"

df11 = pd.read_csv(FileNameP1 + FileNameP2 + "_TOTAL" + SUFFIX)
df12 = pd.read_csv(FileNameP1 + FileNameP3 + "_TOTAL" + SUFFIX)
df11.drop("Unnamed: 0", axis=1, inplace=True)
df12.drop("Unnamed: 0", axis=1, inplace=True)

#
# for i in range(14, 15):
#
#     df103 = pd.read_csv(FileNameP1 + str(i) + FileNameP2 + SUFFIX)
#     df205 = pd.read_csv(FileNameP1 + str(i) + FileNameP3 + SUFFIX)
#
#     df103.drop("Unnamed: 0", axis=1, inplace=True)
#     df205.drop("Unnamed: 0", axis=1, inplace=True)
#
#     df11 = df11.append(df103)
#     df12 = df12.append(df205)


df11 = normalize(df11)
df12 = normalize(df12)


df11.to_csv(FileNameP1 + FileNameP2 + "_TOTAL_NORM" + SUFFIX)
df12.to_csv(FileNameP1 + FileNameP3 + "_TOTAL_NORM" + SUFFIX)

print(df11.shape, df12.shape)