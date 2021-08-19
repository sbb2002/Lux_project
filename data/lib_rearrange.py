class rearrange:
    global match

    def stats(self, match):
        md_list = []
        for i in range(10):
            match_record = match['info']['participants'][i]

            # details
            assists = match_record['assists']
            baronKills = match_record['baronKills']
            bountyLevel = match_record['bountyLevel']
            champExperience = match_record['champExperience']
            champLevel = match_record['champLevel']
            championId = match_record['championId']
            championName = match_record['championName']
            championTransform = match_record['championTransform']
            consumablesPurchased = match_record['consumablesPurchased']
            damageDealtToBuildings = match_record['damageDealtToBuildings']
            damageDealtToObjectives = match_record['damageDealtToObjectives']
            damageDealtToTurrets = match_record['damageDealtToTurrets']
            damageSelfMitigated = match_record['damageSelfMitigated']
            deaths = match_record['deaths']
            detectorWardsPlaced = match_record['detectorWardsPlaced']
            doubleKills = match_record['doubleKills']
            dragonKills = match_record['dragonKills']
            firstBloodAssist = match_record['firstBloodAssist']
            firstBloodKill = match_record['firstBloodKill']
            firstTowerAssist = match_record['firstTowerAssist']
            firstTowerKill = match_record['firstTowerKill']
            gameEndedInEarlySurrender = match_record['gameEndedInEarlySurrender']
            gameEndedInSurrender = match_record['gameEndedInSurrender']
            goldEarned = match_record['goldEarned']
            goldSpent = match_record['goldSpent']
            individualPosition = match_record['individualPosition']
            inhibitorKills = match_record['inhibitorKills']
            inhibitorsLost = match_record['inhibitorsLost']
            item0 = match_record['item0']
            item1 = match_record['item1']
            item2 = match_record['item2']
            item3 = match_record['item3']
            item4 = match_record['item4']
            item5 = match_record['item5']
            item6 = match_record['item6']
            itemsPurchased = match_record['itemsPurchased']
            killingSprees = match_record['killingSprees']
            kills = match_record['kills']
            lane = match_record['lane']
            largestCriticalStrike = match_record['largestCriticalStrike']
            largestKillingSpree = match_record['largestKillingSpree']
            largestMultiKill = match_record['largestMultiKill']
            longestTimeSpentLiving = match_record['longestTimeSpentLiving']
            magicDamageDealt = match_record['magicDamageDealt']
            magicDamageDealtToChampions = match_record['magicDamageDealtToChampions']
            magicDamageTaken = match_record['magicDamageTaken']
            neutralMinionsKilled = match_record['neutralMinionsKilled']
            nexusKills = match_record['nexusKills']
            nexusLost = match_record['nexusLost']
            objectivesStolen = match_record['objectivesStolen']
            objectivesStolenAssists = match_record['objectivesStolenAssists']
            participantId = match_record['participantId']
            pentaKills = match_record['pentaKills']
            perks = match_record['perks']
            physicalDamageDealt = match_record['physicalDamageDealt']
            physicalDamageDealtToChampions = match_record['physicalDamageDealtToChampions']
            physicalDamageTaken = match_record['physicalDamageTaken']
            profileIcon = match_record['profileIcon']
            puuid = match_record['puuid']
            quadraKills = match_record['quadraKills']
            riotIdName = match_record['riotIdName']
            riotIdTagline = match_record['riotIdTagline']
            role = match_record['role']
            sightWardsBoughtInGame = match_record['sightWardsBoughtInGame']
            spell1Casts = match_record['spell1Casts']
            spell2Casts = match_record['spell2Casts']
            spell3Casts = match_record['spell3Casts']
            spell4Casts = match_record['spell4Casts']
            summoner1Casts = match_record['summoner1Casts']
            summoner1Id = match_record['summoner1Id']
            summoner2Casts = match_record['summoner2Casts']
            summoner2Id = match_record['summoner2Id']
            summonerId = match_record['summonerId']
            summonerLevel = match_record['summonerLevel']
            summonerName = match_record['summonerName']
            teamEarlySurrendered = match_record['teamEarlySurrendered']
            teamId = match_record['teamId']
            teamPosition = match_record['teamPosition']
            timeCCingOthers = match_record['timeCCingOthers']
            timePlayed = match_record['timePlayed']
            totalDamageDealt = match_record['totalDamageDealt']
            totalDamageDealtToChampions = match_record['totalDamageDealtToChampions']
            totalDamageShieldedOnTeammates = match_record['totalDamageShieldedOnTeammates']
            totalDamageTaken = match_record['totalDamageTaken']
            totalHeal = match_record['totalHeal']
            totalHealsOnTeammates = match_record['totalHealsOnTeammates']
            totalMinionsKilled = match_record['totalMinionsKilled']
            totalTimeCCDealt = match_record['totalTimeCCDealt']
            totalTimeSpentDead = match_record['totalTimeSpentDead']
            totalUnitsHealed = match_record['totalUnitsHealed']
            tripleKills = match_record['tripleKills']
            trueDamageDealt = match_record['trueDamageDealt']
            trueDamageDealtToChampions = match_record['trueDamageDealtToChampions']
            trueDamageTaken = match_record['trueDamageTaken']
            turretKills = match_record['turretKills']
            turretsLost = match_record['turretsLost']
            unrealKills = match_record['unrealKills']
            visionScore = match_record['visionScore']
            visionWardsBoughtInGame = match_record['visionWardsBoughtInGame']
            wardsKilled = match_record['wardsKilled']
            wardsPlaced = match_record['wardsPlaced']
            win = match_record['win']

            # stats = [match_record[num] for num in range(10)]
            match_data = [
                    assists, 
                    baronKills, bountyLevel, 
                    champExperience, champLevel, championId, championName, championTransform, consumablesPurchased, 
                    damageDealtToBuildings, damageDealtToObjectives, damageDealtToTurrets, damageSelfMitigated, deaths, detectorWardsPlaced, doubleKills, dragonKills, 
                    firstBloodAssist, firstBloodKill, firstTowerAssist, firstTowerKill,
                    gameEndedInEarlySurrender, gameEndedInSurrender, goldEarned, goldSpent,
                    individualPosition, inhibitorKills, inhibitorsLost, item0, item1, item2, item3, item4, item5, item6, itemsPurchased,
                    killingSprees, kills,
                    lane, largestCriticalStrike, largestKillingSpree, largestMultiKill, longestTimeSpentLiving,
                    magicDamageDealt, magicDamageDealtToChampions, magicDamageTaken,
                    neutralMinionsKilled, nexusKills, nexusLost,
                    objectivesStolen, objectivesStolenAssists, 
                    participantId, pentaKills, perks, physicalDamageDealt, physicalDamageDealtToChampions, physicalDamageTaken, profileIcon, puuid, 
                    quadraKills,
                    riotIdName, riotIdTagline, role,
                    sightWardsBoughtInGame, spell1Casts, spell2Casts, spell3Casts, spell4Casts, summoner1Casts, summoner1Id, summoner2Casts, summoner2Id, summonerId, summonerLevel, summonerName, 
                    teamEarlySurrendered, teamId, teamPosition, timeCCingOthers, timePlayed, totalDamageDealt, totalDamageDealtToChampions, totalDamageShieldedOnTeammates, totalDamageTaken, totalHeal, totalHealsOnTeammates, totalMinionsKilled, totalTimeCCDealt, totalTimeSpentDead, totalUnitsHealed, tripleKills, trueDamageDealt, trueDamageDealtToChampions, trueDamageTaken, turretKills, turretsLost,
                    unrealKills,
                    visionScore, visionWardsBoughtInGame,
                    wardsKilled, wardsPlaced, win
                    ]
            md_list.append(match_data)

        return md_list