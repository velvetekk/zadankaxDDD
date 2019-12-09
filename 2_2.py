import os
from userClass import User

def foundMostActiveUser(userList):
    user = userList[0]
    index = 0

    while index < userList.__len__():

        if userList[index].getOccurance() > user.getOccurance():
            user = userList[index]
        index += 1

    return user

def findUserWithMostSiteVisited(userList):
    index = 0
    user = userList[0]

    while index < userList.__len__():

        if userList[index].getVisitedSitesNumber().__len__() > user.getVisitedSitesNumber().__len__():
            user = userList[index]

        index += 1

    return user

def createAndAddUser(userList, name):
    newUser = User()
    newUser.setUserName(name)
    newUser.occurance_ = 1
    userList.append(newUser)

def findUser(name, userList):
    for user in userList:

        if user.userName_ == name:
            return user

    createAndAddUser(userList, name)
    return userList[-1]

def updateOccurance(userList, name):
    userIndex = 0

    if userList.__len__() == 0:
        createAndAddUser(userList, name)

    else:

        while userIndex < userList.__len__():
            actualUser = userList[userIndex]

            if actualUser.userName_ == name:
                userList[userIndex].occurance_ += 1
                return userList

            userIndex += 1
        createAndAddUser(userList, name)
    return userList

def findMostVisitedSite(userList):
    visitList = {}
    index = 0
    topSiteId = 0
    topSiteVisits = 0

    for user in userList:

        for siteId in user.getVisitedSitesNumber().keys():

            if not siteId in visitList:
                visitList[siteId] = user.getVisitedSitesNumber()[siteId]

            else:
                visitList[siteId] += user.getVisitedSitesNumber()[siteId]

    for site in visitList.keys():

        if visitList[site] > topSiteVisits:
            topSiteId = site
            topSiteVisits = visitList[site]

    return [topSiteId, topSiteVisits]






def folder_analyzer(folderPath):

    fileList = os.listdir(folderPath)
    siteList = []
    userList = []
    userTimeSpend = {}
    userPagesSeen = {}

    for fileName in fileList:
        inDate = fileName[:19]
        outDate = fileName[20:40]
        flag = False
        letterIndex = 40
        startName = 0
        endName = 0
        name = ''
        tempString = ''

        while letterIndex < fileName.__len__():

            if fileName[letterIndex] == '\"' and startName != 0:
                endName = letterIndex
                name = fileName[startName:endName]
                userList = updateOccurance(userList, name)

            elif fileName[letterIndex]  == "\"" and startName == 0:
                startName = letterIndex + 1

            while letterIndex < fileName.__len__() and fileName[letterIndex].isdigit():
                tempString += fileName[letterIndex]
                flag = True
                letterIndex += 1

            if flag :
                siteList.append(tempString)
                flag = False
                tempString = ''

            letterIndex += 1

        user = findUser(name, userList)
        user.setVisitedSitesNumber(siteList)
        user.calculateTimeSpend(inDate, outDate)

    most_visit = findMostVisitedSite(userList)
    print(f"most active user in case of occurance: {foundMostActiveUser(userList).userName_}")
    print(f"most active user in case of visited sites: {findUserWithMostSiteVisited(userList).userName_}")
    print(f"most visited site {most_visit}")
    for user in userList:
        print(f"user {user.userName_} spend on this visit :{user.timeSpend_} \n and in total : {user.totalTimeSpend_}")
















folder_analyzer("/home/wylandow/Desktop/costam/dummyFiles")