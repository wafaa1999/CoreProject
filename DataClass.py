import pandas as pd
from CourseClass import *
from InstructorClass import *
from MeetingTimeClass import *
from RoomClass import *


def createArrayOfCourses(courseId, courses):
    ListOfSectionsOfCourse = []
    for i in range(len(courses)):
        ID = str(courses[i].get_number()).split("/")
        if courseId == ID[1]:
            ListOfSectionsOfCourse.append(courses[i])
    return ListOfSectionsOfCourse


def course_choose(arrayOfCourses):
    result = []
    finalResult = []
    flags = []
    for o in range(len(arrayOfCourses)):
        flags.append(True)

    for i in range(len(arrayOfCourses)):
        if flags[i]:
            value = arrayOfCourses[i].get_number()
            num = value.split("/")
            for j in range(i, len(arrayOfCourses)):
                num2 = arrayOfCourses[j].get_number().split("/")
                if num[1] == num2[1]:
                    result.append(arrayOfCourses[j].get_number())
                    flags[j] = False
            w = result.copy()
            finalResult.append(w)
            result.clear()
    return finalResult


def add_courses(courses):
    for i in range(len(courses)):
        if not courses[i].get_from_other_department():
            instructor = courses[i].get_instructors()
            instructor.add_id_to_courses(courses[i].get_number())


class Data:

    def __init__(self, allRooms, meetingTimesOne, meetingTimesLab, meetingTimesThree, instructorsOfCourses,
                 meetingTimesTwo):
        self._meetingTimesLabs = []
        self._rooms = []
        self._meetingTimes1 = []
        self._meetingTimes2 = []
        self._meetingTimes3 = []
        self._instructors = []
        self._arrayOfLabs = []
        self._numberOfLabs = []
        self._coursesOfYears = [[], [], [], [], []]
        self._coursesOfFirstYears = []
        self._coursesOfSecondYears = []
        self._coursesOfThirdYears = []
        self._coursesOfFourthYears = []
        self._coursesOfFifthYears = []
        self._semester = 1
        self._department = 1

        self._softConstraints = [["I1", ["Sunday", "Tuesday"], 8, 9, False, 0.5],
                                 ["I1", ["Sunday", "Tuesday", "Thursday"], 10, 11, False, 1],
                                 ["I3", ["Sunday", "Tuesday"], 8, 9, False, 0.5]]

        for j in range(0, len(allRooms)):
            self._rooms.append(Room(allRooms[j][0], allRooms[j][1]))
        for j in range(0, len(meetingTimesOne)):
            self._meetingTimes1.append(
                MeetingTime(meetingTimesOne[j][0], meetingTimesOne[j][1], meetingTimesOne[j][2],
                            meetingTimesOne[j][3]))

        for j in range(0, len(meetingTimesLab)):
            self._meetingTimesLabs.append(
                MeetingTime(meetingTimesLab[j][0], meetingTimesLab[j][1], meetingTimesLab[j][2],
                            meetingTimesLab[j][3]))

        for j in range(0, len(meetingTimesTwo)):
            self._meetingTimes2.append(
                MeetingTime(meetingTimesTwo[j][0], meetingTimesTwo[j][1], meetingTimesTwo[j][2],
                            meetingTimesTwo[j][3]))
        for j in range(0, len(meetingTimesThree)):
            self._meetingTimes3.append(
                MeetingTime(meetingTimesThree[j][0], meetingTimesThree[j][1], meetingTimesThree[j][2],
                            meetingTimesThree[j][3]))
        for j in range(0, len(instructorsOfCourses)):
            self._instructors.append(Instructor(instructorsOfCourses[j][0], instructorsOfCourses[j][1], instructorsOfCourses[j][2]))

        data1 = pd.read_excel("b1.xlsx")
        self._courses = []
        num1 = data1['num']
        numberOfSections1 = data1['sum']
        type1 = data1['type']
        name1 = data1['name']
        dr1 = data1['dr']
        room1 = data1['room']
        year1 = data1['year']
        sem1 = data1['sem']
        flagDepartment1 = data1['dep']
        timeSlot1 = data1['timeslot']
        toOtherDepartment1 = data1['todep']
        departmentName1 = data1['depN']

        for w in range(0, len(data1)):
            num = num1[w]
            numberOfSections = numberOfSections1[w]
            type = type1[w]
            name = name1[w]
            dr = dr1[w]
            room = room1[w]
            year = year1[w]
            num2 = num.split("/")
            sem = sem1[w]
            fromotherDepartement = flagDepartment1[w] # من ديبارتمنت تاني
            timeSlot = timeSlot1[w]
            toOtherDepartment = toOtherDepartment1[w] # مساق من عندي لحدا تاني
            departmentName = departmentName1[w]
            flag = True

            if type == 2:
                for m in range(len(self._arrayOfLabs)):
                    if num2[1] == self._arrayOfLabs[m]:
                        flag = False
                        break
                if flag:
                    self._arrayOfLabs.append(num2[1])
                    self._numberOfLabs.append(numberOfSections)

            for j in range(0, len(self._instructors)):
                if self._instructors[j].get_name() == dr:
                    instr = self._instructors[j]
                    break
            # self, number, numberType, name, instructors, type, year, sectionNumber, totalNumberOfSections, semester,
            #                  fromOtherDepartment, sharedTimeslot, forOtherDepartment, departmentName)
            if fromotherDepartement and not toOtherDepartment:
                course1 = Course(num, type, name, 0, 0, year, num2[0], numberOfSections, sem,True, timeSlot, False,departmentName)
            elif not fromotherDepartement and not toOtherDepartment:
                course1 = Course(num, type, name, instr, room, year, num2[0], numberOfSections, sem, False, 0, False, departmentName)
            else:
                course1 = Course(num, type, name, instr, room, year, num2[0], numberOfSections, sem, False, 0, True, departmentName) #بدنا تايم سلوت

            self._courses.append(course1)
            if year == 1:
                self._coursesOfFirstYears.append(course1)
            elif year == 2:
                self._coursesOfSecondYears.append(course1)
            elif year == 3:
                self._coursesOfThirdYears.append(course1)
            elif year == 4:
                self._coursesOfFourthYears.append(course1)
            else:
                self._coursesOfFifthYears.append(course1)
                var1 = []

        var1 = course_choose(self._coursesOfFirstYears)
        for i in range(len(var1)):
            self._coursesOfYears[0].append(var1[i])

        var2 = course_choose(self._coursesOfSecondYears)
        for i in range(len(var2)):
            self._coursesOfYears[1].append(var2[i])

        var3 = course_choose(self._coursesOfThirdYears)
        for i in range(len(var3)):
            self._coursesOfYears[2].append(var3[i])

        var4 = course_choose(self._coursesOfFourthYears)
        for i in range(len(var4)):
            self._coursesOfYears[3].append(var4[i])

        var5 = course_choose(self._coursesOfFifthYears)
        for i in range(len(var5)):
            self._coursesOfYears[4].append(var5[i])

        self._numberOfClasses = len(data1)
        add_courses(self._courses)

    def get_rooms(self):
        return self._rooms

    def get_instructors(self):
        return self._instructors

    def get_courses(self):
        return self._courses

    def get_courses_of_years(self):
        return self._coursesOfYears

    def get_meeting_times_1(self):
        return self._meetingTimes1

    def get_meeting_times_labs(self):
        return self._meetingTimesLabs

    def get_array_of_labs(self):
        return self._arrayOfLabs

    def get_number_of_labs(self):
        return self._numberOfLabs

    def get_meeting_times_2(self):
        return self._meetingTimes2

    def get_meeting_times_3(self):
        return self._meetingTimes3

    def get_number_of_classes(self):
        return self._numberOfClasses

    def get_soft_constraints(self):
        return self._softConstraints
