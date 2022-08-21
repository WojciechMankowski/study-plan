from datetime import datetime, timedelta
from DayTask import DayTask

class Schedule:
    def __init__(self, start_time):
        self.dates: list[datetime.date] = [start_time]
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
        self.daytasks.append(dayTask)
#     TODO funkcja rozplanowania nauki
    def learningPlanning(self):
        colection = self.__divisionintocategories()
        read =  colection[0]
        listening =  colection[1]
        writin =  colection[2]
        grama =  colection[3]
        app =  colection[4]
        lession = DayTask("Spotkanie z lektorem", "Wtorek o 8:15")
        learning_vocabulary = DayTask("Nauka słówek", "W tm dniu uczem się nowych słówek")
        repeat = DayTask("Powtórka", "Powtórzenie gramatyki i słownictwa")
        numberday = 0
        while numberday != 7:
            if numberday == 0:
                self.schedule[self.dates[numberday]] = [lession, app]
            elif numberday == 2 or numberday == 4 or numberday == 6:
                self.schedule[self.dates[numberday]] = [learning_vocabulary, app]
            elif numberday == 1: self.schedule[self.dates[numberday]] = [grama, app, writin]
            elif numberday == 3: self.schedule[self.dates[numberday]] = [read, app]
            elif numberday == 5: self.schedule[self.dates[numberday]] = [listening, app]
            elif numberday == 6: self.schedule[self.dates[numberday]] = [repeat, app]
            numberday+=1
        print("")
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
        for daytask in self.daytasks:
            if daytask.name in key_read:
                read.append(daytask)
            elif daytask.name in key_listening: listening.append(daytask)
            elif daytask.name in key_writin: writin.append(daytask)
            elif daytask.name in key_grama: grama.append(daytask)
            else: app.append(daytask)
        return read, listening, writin, grama,app

    def showSchudule(self):
        print(self.schedule)
        # for  key, item in self.schedule.items():
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
