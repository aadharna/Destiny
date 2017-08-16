# Destiny

A copy of the data set I used for this project can be obtained here: https://www.dropbox.com/s/wfrhyy7veba8gw0/indexByMatch_batchUdacity_205_CLEANED_NORM.zip?dl=0

### Step Zero
To rebuild my dataset from scratch, you will need an API key, and matchIDS. 

In order for this to work, you need to first request an API-Key from Bungie.net
You can do so here: http://destinyapiguide.azurewebsites.net/getKey

MatchIds were given to me by https://destinytrialsreport.com/

With these two things, you will call PostGameCarnageReports (PGCRs) from Destiny

### First Step -- dependencies and imports
Libraries used in the totality of this process:

0) Python 3.5

1) Pandas (to make use of the DataFrame)

2) requests (to call Bungie's API)

3) deepcopy (from copy)

4) MatchClass (a custom class to hold the data from each match we call)

5) Numpy 

6) Tensorflow

7) Keras (I used a Tensorflow backend). 

8) SciKit-Learn

9) matplotlib.pyplot

10) Seaborn

11) display from IPython.display (Allows the use of display() for DataFrames)

12) PdfPages from matplotlib.backends.backend_pdf

----

Project pipeline: 

1) Cluster analysis to determine play-style clusters given individualized match data from Destiny (at the moment, the contenders are Expectation Maximation (GMMs) and K-means for the first round of testing).
2) Since matches are between teams, each team can be looked at a sequence of players. Therefore, using the play-style as a feature of each person, one should be able to learn sequences of different playstyles constitute a good team. (Current thoughts are use an LSTM).
3) Given an entire match of two teams, predict which team will win. 

Therefore, the scale starts at the individual, progresses to the team level, and then to the match level.

----
This repo is part 3 of that pipeline. 
Parts 1 and 2 are being worked on currently. 
