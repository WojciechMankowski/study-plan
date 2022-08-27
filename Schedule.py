from datetime import datetime, timedelta
from DayTask import DayTask

class Schedule:
    def __init__(self, start_time):
        self.dates: list[datetime.date] = [start_time.date()]
        self._getDate(start_time)
        self.daytasks: list[DayTask] = []
        self.schedule = {}
    def _getDate(self, startweek):
        number_day = 1
        while number_day != 7:
            dateandtime = timedelta(days=number_day) + startweek
            self.dates.append(dateandtime.date())
            number_day+=1

    def addTask(self, dayTask: DayTask):
        # print("---"*10)
        # print(dayTask)
        self.daytasks.append(dayTask)
    def learningPlanning(self,dayTask:DayTask,date:datetime.date):
        # print(date)
        # print(self.showSchudule())

        if date in self.schedule:
            item = self.schedule[date]
            item.append(dayTask)
        else:
            self.schedule[date] = []
            item = self.schedule[date]
            item.append(dayTask)
    def creatingSschudle(self, date: datetime.date):
        if date in self.schedule:
            item = self.schedule[date]
        else:
            self.schedule[date] = []



    def __divisionintocategories(self):
        read = []
        key_read = ["Czytanie", "Artykuł", "Czytanie artykułu"]
        listening = []
        key_listening = ["Słuchanie", "Wideo"]
        writin = []
        key_writin = ["Pisanie"]
        grama = []
        key_grama = ["Gramatyka", "Czasy", "Present"]
        app = []
        learning_vocabulary = DayTask("Nauka słówek", "W tm dniu uczem się nowych słówek")
        repeat = DayTask("Powtórka", "Powtórzenie gramatyki i słownictwa")
        learning_vocabulary_list = []
        numberday = 0
        while numberday != 7:
            # print(self.dates[numberday])
            numberday+=1
            for daytask in self.daytasks:
                print(daytask)
                if daytask.name in key_read:
                    read.append(daytask)
                elif daytask.name in key_listening: listening.append(daytask)
                elif daytask.name in key_writin: writin.append(daytask)
                elif daytask.name in key_grama: grama.append(daytask)
                else: app.append(daytask)
        # print(read, listening, grama)
        return read, listening, writin, grama,app

    def showSchudule(self):
        # print(self.schedule)
        for key, item in self.schedule.items():
            print(key)
        #     for task in item:
        #         print(f"{key} są zadania {task}")
        #         print("-"*15)
    def getShedule(self):
        return self.schedule

if __name__ == '__main__':
    day = "2022-08-16"
    date = datetime.strptime(day, "%Y-%m-%d")
    schedule = Schedule(date)
    app = DayTask("Aplikacja", "Korzystanie z Dulingo")
    writer = DayTask("Czytanie artykułu", "Czytanie artukułu na temat emocji",
                     "https://www.talkenglish.com/speaking/regular/feelingsemotions1.aspx")
    schedule.addTask(app)
    schedule.addTask(writer)
    schedule.learningPlanning()
    schedule.showSchudule()
