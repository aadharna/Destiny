# Destiny


Getting PostGameCarnageReports (PGCRs) from Destiny
### Step Zero
In order for this to work, you need to first request an API-Key from Bungie.net
I have included my own key commented out; however, I would prefer if you did not use that and instead got your own.
You can do so here: http://destinyapiguide.azurewebsites.net/getKey
### First Step -- dependencies and imports
1) Pandas (to make use of the DataFrame)

2) requests (to call Bungie's API)

3) deepcopy (from copy)

4) MatchClass (a custom class to hold the data from each match we call)
