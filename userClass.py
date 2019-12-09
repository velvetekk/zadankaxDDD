class User:

    def __init__(self):
        self.totalTimeSpend_ = {}
        self.timeSpend_ = {}
        self.totalTimeSpendList_ = []
        self.userName_ = ""
        self.occurance_ = 0
        self.visitedSiteList_ = {}


    def setUserName(self, name):
        self.userName_ = name

    def getVisitedSitesNumber(self):
        return self.visitedSiteList_

    def getOccurance(self):
        return self.occurance_

    def setVisitedSitesNumber(self, siteList):
        while siteList.__len__() > 0:
            siteId = siteList[0]
            timesVisit = siteList.count(siteId)

            if siteId in self.visitedSiteList_ :
                self.visitedSiteList_[siteId] += timesVisit

            else :
                self.visitedSiteList_[siteId] = timesVisit

            while siteId in siteList:
                siteList.remove(siteId)

    def splitDate(self, date):
        counter = 0
        secCounter = 0
        wBeg = 0
        tmp = 0
        dateDic = []

        while counter < date.__len__():

                if date[counter] == '.' or date[counter] ==  ':' or date[counter] ==  ' ':
                    dateDic.append(date[wBeg:counter])
                    wBeg = counter + 1

                if counter == (date.__len__() - 1):
                    dateDic.append(date[-2:])
                counter += 1

        return dateDic

    def totalTimeSpend(self):
        self.totalTimeSpendList_.append(self.timeSpend_)
        index = 0
        totYears = 0
        totMonths = 0
        totDays = 0
        totHours = 0
        totMins = 0
        totSecs = 0

        while index < self.totalTimeSpendList_.__len__():
            totSecs += self.totalTimeSpendList_[index]["seconds"]

            if totSecs >= 60:
                mins = totSecs / 60
                totMins += int(mins)
                totSecs = totSecs % 60

            totMins += self.totalTimeSpendList_[index]["minutes"]

            if totMins >= 60:
                hours = totMins / 60
                totHours += int(hours)
                totMins = totMins % 60

            totHours += self.totalTimeSpendList_[index]["hours"]

            if totHours >= 24:
                days = totHours / 24
                totDays += int(days)
                totHours = totHours % 24

            totDays += self.totalTimeSpendList_[index]["days"]

            if totDays >= 30:
                months = totDays / 30
                totMonths += int(months)
                totDays = totDays % 30

            totMonths += self.totalTimeSpendList_[index]["months"]

            if totMonths >= 12:
                years = totMonths / 12
                totYears = int(years)
                totMonths = totMonths % 12

            totYears += self.totalTimeSpendList_[index]["years"]

            self.totalTimeSpend_ = {
                "years" : totYears,
                "months" : totMonths,
                "days" : totDays,
                "hours" : totHours,
                "minutes" : totMins,
                "seconds" : totSecs
            }

            index += 1


    def calculateTimeSpend(self, inDate, outDate):
        inD = self.splitDate(inDate)
        outD = self.splitDate(outDate)

        secs = int(outD[5]) - int(inD[5])
        mins = int(outD[4]) - int(inD[4])
        hours = int(outD[3]) - int(inD[3])
        days = int(outD[0]) - int(inD[0])
        months = int(outD[1]) - int(inD[1])
        years = int(outD[2]) - int(inD[2])


        if secs < 0:
            mins -= 1
            secs = secs + 60

        if mins < 0:
            hours -= 1
            mins = mins + 60

        if hours < 0:
            days -= 1
            hours = hours + 24

        if days < 0:
            months -= 1
            days = 30 + days

        if months < 0:
            years -= 1
            days = 12 + months

        if years < 0:
            print("wrong dates")


        self.timeSpend_ = {
            "days" : days,
            "months" : months,
            "years" : years,
            "hours" : hours,
            "minutes" : mins,
            "seconds" : secs
        }

        self.totalTimeSpend()

















