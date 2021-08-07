from DataBaseConnection import dataBaseC
from DataClass import Data
from Solve import Solve


class MainSolving:
    def solveMain(self, idDep, tableName, softFlag, semester, date):
        ROOMS = []
        INSTRUCTORS = []
        SOFT_CONSTRAINTS = []
        MEETING_TIMES_2 = []
        MEETING_TIMES_LABS = []
        MEETING_TIMES_1 = []
        self._db = dataBaseC()
        # Rooms
        result = self._db.get_rooms()
        for i in range(len(result)):
            if result[i]['idDepartment'] == idDep:
               ROOMS.append([result[i]['number'], result[i]['name']])

        #INSTRUCTORS
        result1 = self._db.get_istn()
        for i in range(len(result1)):
            if result1[i]['idDepartment'] == idDep:
               INSTRUCTORS.append([str(result1[i]['_id']), result1[i]['name'], False])

        #SOFTCONSTRAINS
        result3 = self._db.get_soft_cons()
        for i in range(len(result3)):
            if result3[i]['idDep'] == idDep:
                wholeTime = result3[i]['time'].split('/')
                time11 = wholeTime[0].split(':')
                if time11[1] == '00':
                    startTime = int(time11[0])
                else:
                    startTime = int(time11[0]) + 0.5
                time112 = wholeTime[1].split(':')
                if time112[1] == '00':
                    endTime = int(time112[0])
                else:
                    endTime = int(time112[0]) + 0.5

                days = wholeTime[2].split(',')
                SOFT_CONSTRAINTS.append(
                [result3[i]['instId'], days, startTime, endTime, result3[i]['need'], result3[i]['wieght']])

        #MEETING_TIMES
        index = 0
        result4 = self._db.get_times(semester, date)
        allLabsTimes = result4[0]['labsTimes'].split('*')
        # 1 يعني شغال يعني في بريك وفي دوام
        dayMap =['سبت','احد','اثنين','ثلاثاء','اربعاء','خميس']

        for i in range(len(allLabsTimes)):
            lab = allLabsTimes[i].split(',')
            if lab[1] == '1':
                timeLab = lab[0].split('/')
                time11 = timeLab[0].split(':')
                if time11[1] == '00':
                    startTimelab = int(time11[0])
                else:
                    startTimelab = int(time11[0]) + 0.5
                time112 = timeLab[1].split(':')
                if time112[1] == '00':
                    endTimelab = int(time112[0])
                else:
                    endTimelab = int(time112[0]) + 0.5
            counter = int((endTimelab - startTimelab) / 3)
            endLabs = startTimelab + 3
            for j in range(0,counter):
                if startTimelab >= 14:
                    MEETING_TIMES_LABS.append(["MT" + str(index), startTimelab, endLabs, dayMap[i]])
                else:
                    MEETING_TIMES_2.append(["MT" + str(index), startTimelab, endLabs, dayMap[i]])
                index += 1
                startTimelab += 3
                endLabs += 3

        allCoursesTimes = result4[0]['courseTimes'].split('*')
        groupsOfCorses = [[],[],[],[],[]]
        for i in range(len(allCoursesTimes)):
            firstCourse = allCoursesTimes[i].split(',')
            if firstCourse[5] == '1':
                groupsOfCorses[int(firstCourse[4])].append([dayMap[i],allCoursesTimes[i]])

        for j in range(len(groupsOfCorses)):
            if len(groupsOfCorses[j]) != 0:
                course = groupsOfCorses[j][0][1].split(',')
                courseTime = course[0].split('/')
                time11 = courseTime[0].split(':')
                if time11[1] == '00':
                    startTimeCourse = int(time11[0])
                else:
                    startTimeCourse = int(time11[0]) + 0.5
                time112 = courseTime[1].split(':')
                if time112[1] == '00':
                    endTimeCourse= int(time112[0])
                else:
                    endTimeCourse = int(time112[0]) + 0.5

                # breaks
                if course[1] == '1':
                    breakTime = course[2].split('/')
                    time11 = breakTime[0].split(':')
                    if time11[1] == '00':
                        startTimeBreak = int(time11[0])
                    else:
                        startTimeBreak = int(time11[0]) + 0.5
                    time112 = breakTime[1].split(':')
                    if time112[1] == '00':
                        endTimeBreak = int(time112[0])
                    else:
                        endTimeBreak = int(time112[0]) + 0.5

                # counter1 = int((endTimeCourse - startTimeCourse) / float(course[3]))
                endTimeCourse1 = startTimeCourse + float(course[3])
                daysOfGroup = []
                daysOfGroup.clear()
                for l in range(len(groupsOfCorses[j])):
                    daysOfGroup.append(groupsOfCorses[j][l][0])

                while endTimeCourse1 <= endTimeCourse:
                    if startTimeCourse != startTimeBreak:
                        MEETING_TIMES_1.append(["MT" + str(index), startTimeCourse, endTimeCourse1, daysOfGroup])
                        index += 1
                        startTimeCourse += float(course[3])
                        endTimeCourse1 += float(course[3])
                    else:
                        startTimeCourse += endTimeBreak - startTimeBreak
                        endTimeCourse1 += endTimeBreak - startTimeBreak


        MEETING_TIMES_3 = [["MT27", 8, 9, ["احد", "ثلاثاء"]],
                           ["MT28", 9, 10, ["احد", "ثلاثاء"]]]
        # instructor_ID , days , start time ,end time , is_wanted , weight
        toSolve = Solve(ROOMS, MEETING_TIMES_1, MEETING_TIMES_LABS, MEETING_TIMES_3, INSTRUCTORS, MEETING_TIMES_2,
                        SOFT_CONSTRAINTS,idDep, tableName, softFlag)
        toSolve.solve()






# s = MainSolving()
# s.solveMain('60ddc9735b4d43f8eaaabf83', 'الفصل الاول', 'true','1','2020/2021')

