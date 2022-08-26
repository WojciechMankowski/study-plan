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
        return f"(Data: {self.data}) {self.name} -> opis zadania: {self.description}"
    def setData(self, data: datetime.date):
        self.data = data
    def getInformation(self) -> str:
        return f"Tytuł: {self.name}. Opis: {self.description}, link: {self.url}"
