import pandas as pd

#PARTS OF FILE NAMES
FileNameP1 = "indexByMatch_batch"
FileNameP2 = "Udacity_103"
FileNameP3 = "Udacity_205"
SUFFIX = ".csv"
FileNameP4 = "batch"
FileNameP5 = "Udacity"

df1 = pd.read_csv(FileNameP1 + "1" + FileNameP2 + SUFFIX, index_col="Unnamed: 0")
#df2 = pd.read_csv(FileNameP1 + FileNameP3 + "_TOTAL" + SUFFIX, index_col="Unnamed: 0")

#For all of the files that I have separated.
for i in range(2, 15):
    #Read in the next file and save it to the first one.

    df103 = pd.read_csv(FileNameP1 + str(i) + FileNameP2 + SUFFIX, index_col="Unnamed: 0")
    #df205 = pd.read_csv(FileNameP1 + str(i) + FileNameP3 + SUFFIX, index_col="Unnamed: 0")


    df1 = df1.append(df103)
    #df2 = df2.append(df205)


#Save the one large Dataframe to a CSV
df1.to_csv(FileNameP4 + FileNameP5 + "_TOTAL" + SUFFIX)
#df2.to_csv(FileNameP1 + FileNameP3 + "_TOTAL" + SUFFIX)

#Print the number of matches now saved in the one file.
print(df1.shape)