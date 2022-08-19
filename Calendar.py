from DayTask import DayTask
from datetime import datetime

class Calendar:

    def __init__(self, startweek: datetime.date, endweek: datetime.date):
        self.startweek = startweek
        self.endweek = endweek
        self.daytasks: list[DayTask] = []

    def addDayTask(self, daytask: DayTask)-> None:
        self.daytasks.append(daytask)