from Tasks import Task
from datetime import datetime
from dataclasses import dataclass

@dataclass
class DayTask:
    name: str
    description: str
    data: datetime.date = ""
    url: str = ""

    def __str__(self):
        return f"{self.name} -> opis zadania: {self.description}"
