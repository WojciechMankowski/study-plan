from datetime import datetime, timedelta
from DayTask import DayTask

class Schedule:
    def __init__(self, start_time):
        self.dates: list[datetime.date] = [start_time]
        self._getDate(start_time)
        self.schedule = {}
    def _getDate(self, startweek):
        number_day = 1
        while number_day != 7:
            dateandtime = timedelta(days=number_day) + startweek
            self.dates.append(dateandtime.date())
            number_day+=1
        print(self.dates)
#     TODO funkcja dodawania zadań
#     TODO funkcja rozplanowania nauki
#     TODO funkcja wyświetlenie harmonogramu

if __name__ == '__main__':
    day = "2022-08-16"
    date = datetime.strptime(day, "%Y-%m-%d")
    schedule = Schedule(date)
