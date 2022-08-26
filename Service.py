import os
from datetime import datetime, timedelta
from json import load
from fpdf import FPDF
import fpdf
from DayTask import DayTask
from Document import DOC
from Schedule import Schedule


class Service:

    def __init__(self, date: datetime):
        self.schedule = Schedule(date)
        self.dates = []
        self._getDate(date)

    def readingJSON(self):
        file = open('data.json', encoding="utf-8")
        data = load(file)
        schedule = []
        for key, value in data.items():
            # date = (datetime.strptime(key, "%Y-%m-%d")).date()
            print(key)
            for item in value:
                print(item)
                schedule.append(
                    DayTask(name=item['name'],
                            description=item['description'],
                            url=item["url"],
                            )
                )
        numberday = 0
        for daytask in schedule:
            self.schedule.learningPlanning(daytask, self.dates[numberday])
            numberday += 1
        # self.schedule.showSchudule()
    def _getDate(self, startweek):
        number_day = 1
        while number_day != 7:
            dateandtime = timedelta(days=number_day) + startweek
            self.dates.append(dateandtime.date())
            number_day+=1

    def creatDOC(self):
        data = list(self.schedule.getShedule().keys())
        doc = DOC(data[0], data[-1])
        schudle = self.schedule.getShedule()
        for key, item in schudle.items():
            for value in item:
                if type(value) == list :
                    if len(value) != 0:
                        doc.AddTabet(value, str(key))
                elif type(value) ==DayTask:
                    doc.AddTabet(value, str(key))
        doc.Save()
    def show(self):
        schudle = self.schedule.getShedule()
        for key, item in schudle.items():
            print(key)
            print("---"*5)
            for value in item:
                if type(value) == list :
                    if len(value) != 0:
                       for i in value:
                           print(i)
                elif type(value) ==DayTask:
                    print(value)

if __name__ == '__main__':
    day = "2022-08-16"
    date = datetime.strptime(day, "%Y-%m-%d")
    serv = Service(date)
    serv.readingJSON()
    # serv.show()
    # serv.creatDOC()

