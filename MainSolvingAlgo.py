from ClassFinal import Classing
from DataBaseConnection import dataBaseC
from DataClass import Data
from Solve import Solve


class MainSolving:
    # courseNumber, courseName, days, startHour, endHour,
    #                  roomNumber, instName, roomType, classConflict,
    #                  flagConflict
    def cal_fitness(self, idDep, tableName):
        classesOfData = []
        response = dataBaseC().get_final_table(tableName, idDep)
        for k in range(len(response)):
           classesOfData.append(Classing(response[k]['courseNumber'], response[k]['courseName'], response[k]['days']
                                         , response[k]['startHour'], response[k]['endHour'], response[k]['roomNumber']
                                         , response[k]['instName'], response[k]['roomType'], response[k]['classConflict']
                                         , response[k]['flagConflict'], response[k]['year'],response[k]['totalNumberOfSection'],
                                         response[k]['semester']))
        counter = 0
        index = 0
        for i in range(0, len(classesOfData)):

            if not classesOfData[i].get_room_number() == 'من قسم اخر':
                if classesOfData[i].get_room_type() != classesOfData[i].get_room_type() :
                    print("room type")
                    print("calss i  = ")
                    print(classesOfData[i].get_inst_name())
                    print(classesOfData[i].get_room_number())
                    print(classesOfData[i].get_course_name())

                    print("calss j  = ")
                    print(classesOfData[j].get_inst_name())
                    print(classesOfData[j].get_room_number())
                    print(classesOfData[j].get_course_name())
                    classesOfData[i].set_flag_conflict(True)
                    classesOfData[i].set_class_conflict(index)
                    classesOfData[j].set_flag_conflict(True)
                    classesOfData[j].set_class_conflict(index)
                    index += 1
                    counter += 1
            for j in range(0, len(classesOfData)):
                if j >= i:
                    flag = False
                    q1 = classesOfData[i].get_days()
                    q2 = classesOfData[j].get_days()
                    for kk in range(0, len(q1)):
                        for kkk in range(0, len(q2)):
                            w1 = classesOfData[i].get_days()[kk]
                            w2 = classesOfData[j].get_days()[kkk]
                            if w1 == w2:
                                flag = True
                    DuringStart = False
                    DuringEnd = False
                    SameStart = False
                    SameEnd = False

                    if classesOfData[i].get_start_hour() == classesOfData[j].get_start_hour():
                        SameStart = True
                    if classesOfData[i].get_end_hour() == classesOfData[j].get_end_hour():
                        SameEnd = True
                    if ((classesOfData[j].get_start_hour()  < classesOfData[i].get_start_hour() ) and
                            (classesOfData[j].get_end_hour() > classesOfData[i].get_start_hour() )):
                        DuringStart = True
                    if ((classesOfData[j].get_start_hour() < classesOfData[i].get_end_hour()) and
                            (classesOfData[j].get_end_hour() > classesOfData[i].get_end_hour())):
                        DuringEnd = True
                    if (DuringStart or DuringEnd or SameStart or SameEnd) and flag and (
                            classesOfData[i].get_course_number() != classesOfData[j].get_course_number()):
                        if not classesOfData[i].get_room_number() == 'من قسم اخر' or classesOfData[j].get_room_number() == 'من قسم اخر' :
                            if classesOfData[i].get_room_number() == classesOfData[j].get_room_number():
                                print("room conflict")
                                print("calss i  = ")
                                print(classesOfData[i].get_inst_name())
                                print(classesOfData[i].get_room_number())
                                print(classesOfData[i].get_course_name())

                                print("calss j  = ")
                                print(classesOfData[j].get_inst_name())
                                print(classesOfData[j].get_room_number())
                                print(classesOfData[j].get_course_name())
                                classesOfData[i].set_flag_conflict(True)
                                classesOfData[i].set_class_conflict(index)
                                classesOfData[j].set_flag_conflict(True)
                                classesOfData[j].set_class_conflict(index)
                                index += 1
                                counter += 1

                            if classesOfData[i].get_inst_name() == classesOfData[j].get_inst_name():
                                print("instroctor conflict")
                                print("calss i  = ")
                                print(classesOfData[i].get_inst_name())
                                print(classesOfData[i].get_room_number())
                                print(classesOfData[i].get_course_name())

                                print("calss j  = ")
                                print(classesOfData[j].get_inst_name())
                                print(classesOfData[j].get_room_number())
                                print(classesOfData[j].get_course_name())
                                classesOfData[i].set_flag_conflict(True)
                                classesOfData[i].set_class_conflict(index)
                                classesOfData[j].set_flag_conflict(True)
                                classesOfData[j].set_class_conflict(index)
                                index += 1
                                counter += 1
                            # **************
                            if classesOfData[i].get_year() == '-1' and classesOfData[j].get_year() == '-1':
                                print("optinal. conflict")
                                print("calss i  = ")
                                print(classesOfData[i].get_inst_name())
                                print(classesOfData[i].get_room_number())
                                print(classesOfData[i].get_course_name())

                                print("calss j  = ")
                                print(classesOfData[j].get_inst_name())
                                print(classesOfData[j].get_room_number())
                                print(classesOfData[j].get_course_name())
                                classesOfData[i].set_flag_conflict(True)
                                classesOfData[i].set_class_conflict(index)
                                classesOfData[j].set_flag_conflict(True)
                                classesOfData[j].set_class_conflict(index)
                                index += 1
                                counter += 1

                        if not (classesOfData[i].get_year() == '-1') and not \
                                (classesOfData[j].get_year() == '-1') and not \
                                classesOfData[i].get_year() =='لقسم اخر' and not \
                                classesOfData[j].get_year() =='لقسم اخر' :

                            if ((classesOfData[i].get_year() == classesOfData[j].get_year()) and \
                                (classesOfData[i].get_total_number_of_sections()== 1 or classesOfData[ \
                                        j].get_total_number_of_sections() == 1)) and \
                                    classesOfData[i].get_semester() == classesOfData[j].get_semester():

                                print("one comp. conflict")
                                print("calss i  = ")
                                print(classesOfData[i].get_inst_name())
                                print(classesOfData[i].get_room_number())
                                print(classesOfData[i].get_course_name())

                                print("calss j  = ")
                                print(classesOfData[j].get_inst_name())
                                print(classesOfData[j].get_room_number())
                                print(classesOfData[j].get_course_name())
                                classesOfData[i].set_flag_conflict(True)
                                classesOfData[i].set_class_conflict(index)
                                classesOfData[j].set_flag_conflict(True)
                                classesOfData[j].set_class_conflict(index)
                                index += 1
                                counter += 1
        #تخزين بالداتا بيس
        print("conflict is = " + str(counter))

    # idDep, tableName, softFalg, semster, date
    def solveMain(self, idDep, tableName, softFlag, semester, date):
        ROOMS = []
        INSTRUCTORS = []
        SOFT_CONSTRAINTS = []
        MEETING_TIMES_2 = []
        MEETING_TIMES_LABS = []
        MEETING_TIMES_1 = []
        self._db = dataBaseC()
        self._db.change_status('proc', tableName, idDep)

        # Rooms
        result = self._db.get_rooms()
        for i in range(len(result)):
            if result[i]['idDepartment'] == idDep:
                ROOMS.append([result[i]['number'], result[i]['name']])

        # INSTRUCTORS
        result1 = self._db.get_istn()
        for i in range(len(result1)):
            if result1[i]['idDepartment'] == idDep:
                softInst = self._db.get_soft_cons_for_inst(result1[i]['name'], idDep)
                Flag0 = False
                if softInst == 'true':
                    Flag0 = True
            INSTRUCTORS.append([str(result1[i]['_id']), result1[i]['name'], Flag0])

        # SOFTCONSTRAINS
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

                for k in range(len(result1)):
                    if result3[i]['insName'] == result1[k]['name']:
                        inst = str(result1[k]['_id'])
                SOFT_CONSTRAINTS.append(
                  [  inst, days, startTime, endTime, result3[i]['need'], result3[i]['wieght']])

        # MEETING_TIMES
        index = 0
        result4 = self._db.get_times(semester, date)
        allLabsTimes = result4[0]['labsTimes'].split('*')
        # 1 يعني شغال يعني في بريك وفي دوام
        dayMap = ['سبت', 'احد', 'اثنين', 'ثلاثاء', 'اربعاء', 'خميس']
        dayMap2 = [['سبت'], ['احد'], ['اثنين'], ['ثلاثاء'], ['اربعاء'], ['خميس']]
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
            for j in range(0, counter):
                if startTimelab >= 14:
                    MEETING_TIMES_LABS.append(["MT" + str(index), startTimelab, endLabs, dayMap2[i]])
                else:
                    MEETING_TIMES_2.append(["MT" + str(index), startTimelab, endLabs, dayMap2[i]])
                index += 1
                startTimelab += 3
                endLabs += 3


        # ********************
        allCoursesTimes = result4[0]['courseTimes'].split('*')
        groupsOfCorses = [[], [], [], [], []]
        for i in range(len(allCoursesTimes)):
            firstCourse = allCoursesTimes[i].split(',')
            if firstCourse[5] == '1':
                groupsOfCorses[int(firstCourse[4])].append([dayMap[i], allCoursesTimes[i]])

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
                    endTimeCourse = int(time112[0])
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
                        SOFT_CONSTRAINTS, idDep, tableName, softFlag)
        toSolve.solve()








# s = MainSolving()
# # s.solveMain('60ddc9735b4d43f8eaaabf83', 'الفصل الاول', 'true', '1', '2020/2021')
# s.cal_fitness('60ddc9735b4d43f8eaaabf83', 'الفصل الاول')
