from datetime import datetime, timedelta
from DayTask import DayTask

class Schedule:
    def __init__(self, start_time)-> None:
        self.dates: list[datetime.date] = [start_time.date()]
        self._getDate(start_time)
        self.daytasks: list[DayTask] = []
        self.schedule = {}
    def _getDate(self, startweek)-> None:
        number_day = 1
        while number_day != 7:
            dateandtime = timedelta(days=number_day) + startweek
            self.dates.append(dateandtime.date())
            number_day+=1

    def addTask(self, dayTask: DayTask)-> None:
        self.daytasks.append(dayTask)
    def learningPlanning(self,dayTask:DayTask,date:datetime.date)-> None:
        if date in self.schedule:
            item = self.schedule[date]
            item.append(dayTask)
        else:
            self.schedule[date] = []
            item = self.schedule[date]
            item.append(dayTask)
    def creatingSschudle(self, date: datetime.date)-> None:
        self.schedule[date] = []

    def showSchudule(self)-> None:
        for date in self.dates:
            print(date)
            print(self.schedule[date])
    def getShedule(self):
        return self.schedule

if __name__ == '__main__':
    day = "2022-08-16"
    date = datetime.strptime(day, "%Y-%m-%d")
    schedule = Schedule(date)

