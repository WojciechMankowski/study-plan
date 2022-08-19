from dataclasses import dataclass

@dataclass
class Task:
    name:str
    description: str
    url: str = ""

class ListTasks:

    def __init__(self)-> None:
        self.listtasks: list[Task] = []
    def addTask(self, task: Task)-> None:
        self.listtasks.append(task)
    def getListTask(self)-> list[Task] :
        return self.listtasks