import os
from datetime import datetime, timedelta
from json import load
from fpdf import FPDF
import fpdf
from DayTask import DayTask
from Document import DOC
from Schedule import Schedule


class Service:

    def __init__(self, date: datetime.date)-> None:
        self.schedule = Schedule(date)
        self.dates = [date.date()]
        self._getDate(date)

    def readingJSON(self)-> None:
        file = open('data.json', encoding="utf-8")
        data = load(file)
        schedule = []
        for key, value in data.items():
            for item in value:
                schedule.append(
                    DayTask(name=item['name'],
                            description=item['description'],
                            url=item["url"], type=key
                            )
                )
        self.Scheduling(schedule)
        self.schedule.showSchudule()

    def Scheduling(self, schedule: list[DayTask])-> None:
        numberday = 0
        app = DayTask("Korzystanie z aplikacji", "", "app")
        replay = DayTask("Powtórka słowek", "", "")
        for daytask in schedule:
            if daytask.type == "Zajęcia":
                self.schedule.learningPlanning(daytask, self.dates[0])
            elif daytask.type == "Czytanie":
                self.schedule.learningPlanning(daytask, self.dates[5])
            elif daytask.type == "Powtórka":
                self.schedule.learningPlanning(replay, date=self.dates[2])
                self.schedule.learningPlanning(replay, date=self.dates[4])
                self.schedule.learningPlanning(replay, date=self.dates[6])
            elif daytask.type == "Słuchanie":
                self.schedule.learningPlanning(daytask, self.dates[3])
            elif daytask.type == "Gramatyka":
                self.schedule.learningPlanning(daytask, self.dates[1])
                self.schedule.learningPlanning(daytask, self.dates[5])
            elif daytask.type == "Podsumowanie tygodnia":
                self.schedule.learningPlanning(daytask, self.dates[7])

            self.schedule.learningPlanning(app, self.dates[numberday])
            numberday += 1
    def _getDate(self, startweek) -> None:
        number_day = 1
        self.dates.append(startweek.date())
        while number_day != 7:
            dateandtime = timedelta(days=number_day) + startweek
            self.dates.append(dateandtime.date())
            self.schedule.creatingSschudle(dateandtime.date())
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


if __name__ == '__main__':
    day = "2022-08-30"
    date = datetime.strptime(day, "%Y-%m-%d")
    serv = Service(date)
    serv.readingJSON()
    # serv.show()
    # serv.creatDOC()

