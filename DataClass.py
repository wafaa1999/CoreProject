import pandas as pd
from CourseClass import *
from DataBaseConnection import dataBaseC
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
                 meetingTimesTwo, idDep, tableName, semester):
        self._db = dataBaseC()
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
        self._courses = []
        #**************************  تعديل
        self._semester = semester
        # self._department = 1

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
        # get courses
        result = self._db.get_course_from_draft(idDep, tableName)
        courses1 = []
        for i in range(len(result)):
            flag = True
            for j in range(len(courses1)):
                if result[i]['courseName'] == courses1[j]['courseName']:
                    flag = False
            if flag:
                courses1.append(result[i])

        for k in range(len(courses1)):
            current_course = courses1[k]['courseName']
            sameCourses = self.get_similar_courses(current_course, result)
            count = len(sameCourses)
            # count += 1
            for w in range(0, count):

                num = str((w+1)) + "/"+sameCourses[w]['courseNumber']
                numberOfSections = count
                if sameCourses[w]['duration'] == '3':
                    type = 1
                elif sameCourses[w]['duration'] == '1':
                    type = 2
                elif sameCourses[w]['duration'] == '2':
                    type = 3
                name = sameCourses[w]['courseName']
                dr = sameCourses[w]['courseIns']
                room = sameCourses[w]['roomType']
                year = int(sameCourses[w]['year'])
                section = w+1
                sem = sameCourses[w]['semester']
                if sameCourses[w]['fromOtherDep'] == 'false':
                    fromotherDepartement = False
                else:
                    fromotherDepartement = True

                if sameCourses[w]['toOtherDep'] == 'false':
                    toOtherDepartment = False
                else:
                    toOtherDepartment = True
                timeSlot = sameCourses[w]['timeSolt']
                departmentName = sameCourses[w]['specialty']



                flag = True

                if type == 2:
                    for m in range(len(self._arrayOfLabs)):
                        if sameCourses[w]['courseNumber'] == self._arrayOfLabs[m]:
                            flag = False
                            break
                    if flag:
                        self._arrayOfLabs.append(sameCourses[w]['courseNumber'])
                        self._numberOfLabs.append(numberOfSections)

                for j in range(0, len(self._instructors)):
                    if self._instructors[j].get_name() == dr:
                        instr = self._instructors[j]
                        break
                # self, number, numberType, name, instructors, type, year, sectionNumber, totalNumberOfSections, semester,
                #                  fromOtherDepartment, sharedTimeslot, forOtherDepartment, departmentName)
                if fromotherDepartement and not toOtherDepartment:
                    course7 = Course(num, type, name, 0, 0, year, section, numberOfSections, sem, True, timeSlot, False,
                                     departmentName)
                elif not fromotherDepartement and not toOtherDepartment:
                    course7 = Course(num, type, name, instr, room, year, section, numberOfSections, sem, False, 0,
                                     False, departmentName)
                else:
                    course7 = Course(num, type, name, instr, room, year, section, numberOfSections, sem, False, timeSlot, True,
                                     departmentName)  # بدنا تايم سلوت

                self._courses.append(course7)

                if year == 1:
                    self._coursesOfFirstYears.append(course7)
                elif year == 2:
                    self._coursesOfSecondYears.append(course7)
                elif year == 3:
                    self._coursesOfThirdYears.append(course7)
                elif year == 4:
                    self._coursesOfFourthYears.append(course7)
                elif year == 5:
                    self._coursesOfFifthYears.append(course7)
                    var1 = []

        # data1 = pd.read_excel("b1.xlsx")
        # self._courses = []
        # num1 = data1['num']
        # numberOfSections1 = data1['sum']
        # type1 = data1['type']
        # name1 = data1['name']
        # dr1 = data1['dr']
        # room1 = data1['room']
        # year1 = data1['year']
        # sem1 = data1['sem']
        # flagDepartment1 = data1['dep']
        # timeSlot1 = data1['timeslot']
        # toOtherDepartment1 = data1['todep']
        # departmentName1 = data1['depN']

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

        self._numberOfClasses = len(result)
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

    def get_similar_courses(self, current_course, courses):
        course = []
        for i in range(len(courses)):
            if current_course == courses[i]['courseName']:
                course.append(courses[i])

        return course
