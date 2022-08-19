from Tasks import Task
from datetime import datetime
class DayTask(Task):
    data: datetime.date

    def __str__(self):
        return f"{self.name} -> opis zadania: {self.description}"
