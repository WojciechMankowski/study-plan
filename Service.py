import os
from datetime import datetime
from json import load
from fpdf import FPDF
import fpdf
from DayTask import DayTask
from Document import DOC
from Schedule import Schedule


class Service:

    def __init__(self, date: datetime):
        self.schedule = Schedule(date)

    def readingJSON(self):
        file = open('data.json', encoding="utf-8")
        data = load(file)
        schedule = data['shedule']
        for key, value in schedule.items():
            date = (datetime.strptime(key, "%Y-%m-%d")).date()
            print(value)
            print(type*value)
            for item in value:
                self.schedule.addTask(
                    DayTask(name=item['name'],
                            description=item['description'],
                            url=item["url"],
                            data=date)
                )
        self.schedule.learningPlanning()
        # self.schedule.showSchudule()

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
    serv.show()
    # serv.creatDOC()

