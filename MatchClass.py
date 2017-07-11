class SingleMatch:
    def __init__(self, PersonId):
        self.id = PersonId
        self.match = {}
        self.match[str(PersonId)] = {}


    def display(self):

        print("\n\n NEW MATCH \n\nmatchId, ", self.id, "\n\n")

        for people in self.match:
            #print people, "", self.match[self.id][people]
            for data in self.match[people]:
                print(data, "", self.match[people][data])
            print(" ")

    def getId(self):
        return self.id

    def getMatch(self):
        return self.match

    def addMatchIDtoPlayers(self, playerId):
        self.match[playerId]["matchId"] = self.id

    def addPlayer(self, playerId):
        #print team, playerId
        self.match[str(playerId)] = {}


    def addKills(self, playerId, kills):

        self.match[playerId]["kills"] = kills

    def addAssists(self, playerId, assists):

        self.match[playerId]["assists"] = assists

    def addScore(self, playerId, score):

        self.match[playerId]["score"] = score

    def getScore(self, playerId):

        return self.match[playerId]["score"]

    def addAVGLIFE(self, playerId, lifespane):

        self.match[playerId]["averageLifespan"] = lifespane

    def addAVG_K_DIST(self, playerId, AVGKDIST):

        self.match[playerId]["averageKillDistance"] = AVGKDIST

    def addSecondsPlayed(self, playerId, SecPlay):

        self.match[playerId]["secondsPlayed"] = SecPlay

    def addDeaths(self, playerId, deaths):

        self.match[playerId]["deaths"] = deaths

    def addAVGScorePerKill(self, playerId, AVGSCRPKILL):

        self.match[playerId]["averageScorePerKill"] = AVGSCRPKILL

    def addAVGScorePerLife(self, playerId, AVGSCRPLIFE):

        self.match[playerId]["averageScorePerLife"] = AVGSCRPLIFE

    def addStanding(self, playerId, standing):

        self.match[playerId]["standing"] = standing

    def addmeleeKills(self, playerId, mKills):

        self.match[playerId]["weaponKillsMelee"] = mKills

    def addsuperKills(self, playerId, sKills):

        self.match[playerId]["weaponKillsSuper"] = sKills

    def addBestWeapon(self, playerId, best):

        self.match[playerId]["weaponBestType"] = best

    def addCompletion(self, playerId, comp):

        self.match[playerId]["completed"] = comp

    def addKD(self, playerId, KD):

        self.match[playerId]["killsDeathsRatio"] = KD

    def addKAD(self, playerId, KAD):

        self.match[playerId]["killsDeathsAssists"] = KAD

    def addActiveDuration(self, playerId, duration):

        self.match[playerId]["activityDurationSeconds"] = duration

    def addTeamScore(self, TS):

        self.match["teamScore"] = TS

    def addPlayerClass(self, playerId, pClass):

        self.match[playerId]["class"] = pClass

    def addLL(self, playerId, LL):

        self.match[playerId]["lightLevel"] = LL

    def addCR(self, playerId, CR):

        self.match[playerId]["combatRating"] = CR

    def addPrimaries(self, playerId, numPrimKills):

        self.match[playerId]["weaponKillsPrimary"] = numPrimKills

    def addSecondaries(self, playerId, numSecKills):

        self.match[playerId]["weaponKillsSecondary"] = numSecKills

    def addHeavy(self, playerId, numHeavyKills):

        self.match[playerId]["weaponKillsHeavy"] = numHeavyKills

    def addAbilityKills(self, playerId, abilityKills):

        self.match[playerId]["weaponKillsOther"] = abilityKills

    def addpercentContrib(self, playerId, yourScore, teamScore):

        if teamScore == 0.0 or teamScore == 0:
            teamScore = 0.1

            self.match[playerId]["percentContribution"] = float(yourScore/teamScore)

    def addTeam(self, playerId, team):

        if team == "Alpha":
            team = 16
        else:
            team = 17

        self.match[playerId]["team"] = team