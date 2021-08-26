import random as rnd
from ClassClass import Class


def find_shared_time_slot(course, data):
    answer = []
    time = course.get_shared_time_slot().split("/")
    if course.get_number_type() == 1:
        time11 = time[0].split(':')
        if time11[1] == '00':
            time[0] = int(time11[0])
        else:
            time[0] = int(time11[0]) + 0.5
        time112 = time[1].split(':')
        if time112[1] == '00':
            time[1] = int(time112[0])
        else:
            time[1] = int(time112[0]) + 0.5


        for i in range(len(data.get_meeting_times_1())):
            x = data.get_meeting_times_1()[i]
            if data.get_meeting_times_1()[i].get_start() == time[0] and \
                    data.get_meeting_times_1()[i].get_end() == time[1]:
                days = time[2].split(",")
                # print(days[0])
                # print(data.get_meeting_times_1()[i].get_days()[0])
                if days[0] == data.get_meeting_times_1()[i].get_days()[0]:
                    answer.append(data.get_meeting_times_1()[i])

                    ######
    elif course.get_number_type() == 2:
        for i in range(len(data.get_meeting_times_2())):
            if data.get_meeting_times_2()[i].get_start() == time[0] and \
                    data.get_meeting_times_2()[i].get_end() == time[1]:
                days = time[2].split(",")
                if days[0] == data.get_meeting_times_2()[i].get_days()[0]:
                    answer.append(data.get_meeting_times_21()[i])
    elif course.get_number_type() == 3:
        for i in range(len(data.get_meeting_times_3())):
            if data.get_meeting_times_3()[i].get_start() == time[0] and data.get_meeting_times_3()[i].get_end() == \
                    time[1]:
                days = time[2].split(",")
                if days[0] == data.get_meeting_times_3()[i].get_days()[0]:
                    answer.append(data.get_meeting_times_3()[i])
    return answer


def get_index(rooms, room):
    for i in range(0, len(rooms)):
        if rooms[i].get_number() == room.get_number():
            return i
    return -1


def conflict(FirstClass, SecondClass):
    flag = False

    q1 = FirstClass.get_meeting_time().get_days()
    xw = SecondClass
    q2 = SecondClass.get_meeting_time().get_days()
    for kk in range(0, len(q1)):
        for kkk in range(0, len(q2)):
            w1 = FirstClass.get_meeting_time().get_days()[kk]
            w2 = SecondClass.get_meeting_time().get_days()[kkk]
            if w1 == w2:
                flag = True
    DuringStart = False
    DuringEnd = False
    SameStart = False
    SameEnd = False

    if FirstClass.get_meeting_time().get_start() == SecondClass.get_meeting_time().get_start():
        SameStart = True
    if FirstClass.get_meeting_time().get_end() == SecondClass.get_meeting_time().get_end():
        SameEnd = True
    if ((SecondClass.get_meeting_time().get_start() < FirstClass.get_meeting_time().get_start()) and
            (SecondClass.get_meeting_time().get_end() > FirstClass.get_meeting_time().get_start())):
        DuringStart = True
    if ((SecondClass.get_meeting_time().get_start() < FirstClass.get_meeting_time().get_end()) and
            (SecondClass.get_meeting_time().get_end() > FirstClass.get_meeting_time().get_end())):
        DuringEnd = True
    if (DuringStart or DuringEnd or SameStart or SameEnd) and flag and (SecondClass.get_is_taken() == False) and (
            FirstClass.get_id() != SecondClass.get_id()):
        return False

    else:
        return True


def set_taken_flages(classes):
    for m in range(len(classes)):
        classes[m].set_is_taken(False)


class Schedule:
    def __init__(self, data):
        self._data = data
        self._classes = []
        self._numbOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True
        self._superiorityWeight = 0
        self._middlewareWight = 0
        self._leastwiseWeight = 0

    def get_superiority_weight(self):
        return self._superiorityWeight

    def get_middleware_wight(self):
        return self._middlewareWight

    def get_leastwise_weight(self):
        return self._leastwiseWeight

    def inc_superiority_weight(self):
        self._superiorityWeight += 1

    def inc_middleware_weight(self):
        self._middlewareWight += 1

    def inc_leastwise_weight(self):
        self._leastwiseWeight += 1

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numb_of_conflicts(self):
        return self._numbOfConflicts

    def get_fitness(self):
        if self._isFitnessChanged:
            self._fitness = self.calculate_fitness
            self._isFitnessChanged = False
        return self._fitness

    def search_for_class(self, id_value, classes):
        for i in range(0, len(classes)):
            if classes[i].get_course().get_number() == id_value:
                return classes[i]

    def initialize(self):
        courses = self._data.get_courses()

        for j in range(0, len(courses)):
            if(j == 7):
                print("hi")
            newclass = Class(self._classNumb, courses[j])
            self._classNumb += 1
            newclass.set_instructor(courses[j].get_instructors())
            x = courses[j].get_number_type()
            counterOne = 0
            counterTwo = 0
            flagOne = False
            flagTwo = False
            if courses[j].get_from_other_department():
                answer = find_shared_time_slot(courses[j], self._data)[0]

                newclass.set_meeting_time(answer)
                # newclass.set_room('من قسم اخر')
                # newclass.set_instructor('من قسم اخر')

            else:
                if courses[j].get_for_other_department():
                    answer = find_shared_time_slot(courses[j], self._data)[0]
                    newclass.set_meeting_time(answer)

                while counterOne < 30 and not courses[j].get_for_other_department():
                    counterOne += 1
                    if x == 1 :
                        newclass.set_meeting_time(
                            self._data.get_meeting_times_1()[rnd.randrange(0, len(self._data.get_meeting_times_1()))])
                    if x == 2:
                        value = courses[j].get_number().split("/")
                        for o in range(len(self._data.get_array_of_labs())):
                            if value[1] == self._data.get_array_of_labs()[o]:
                                x = rnd.random()
                                if self._data.get_number_of_labs()[o] > 5 or x < 0.2:
                                    newclass.set_meeting_time(
                                        self._data.get_meeting_times_2()[
                                            rnd.randrange(0, len(self._data.get_meeting_times_2()))])

                                else:
                                    newclass.set_meeting_time(
                                        self._data.get_meeting_times_labs()[
                                            rnd.randrange(0, len(self._data.get_meeting_times_labs()))])

                    if x == 3:
                        newclass.set_meeting_time(
                            self._data.get_meeting_times_3()[rnd.randrange(0, len(self._data.get_meeting_times_3()))])
                    for k in range(0, len(self._classes)):
                        if not self._classes[k].get_course().get_from_other_department():
                            if self._classes[k].get_instructor().get_id() == newclass.get_instructor().get_id():
                                output = conflict(self._classes[k], newclass)
                                if not output:
                                    flagOne = True
                    if not flagOne:
                        break
                if x == 2:
                    self._data.get_number_of_labs()[o] -= 1

                while True:
                    counterTwo += 1
                    newclass.set_room(self._data.get_rooms()[rnd.randrange(0, len(self._data.get_rooms()))])
                    if newclass.get_course().get_type() == newclass.get_room().get_type():
                        if counterTwo > 20:
                            break
                        for k in range(0, len(self._classes)):
                            if not self._classes[k].get_course().get_from_other_department():
                                if self._classes[k].get_room().get_number() == newclass.get_room().get_number():
                                    output = conflict(self._classes[k], newclass)
                                    if output:
                                        flagTwo = True
                        if not flagTwo:
                            break
            self._classes.append(newclass)
        return self

    def search_for_course(self, classes, idCourse):
        for i in range(0, len(classes)):
            if idCourse == classes[i].get_course().get_number():
                return classes[i]

    @property
    def calculate_fitness(self):

        self._numbOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            classes[i].set_conflict(True)

            if not classes[i].get_course().get_from_other_department() and not classes[i].get_course().get_for_other_department():
                if classes[i].get_room().get_type() != classes[i].get_course().get_type():
                    self._numbOfConflicts += 1
                    classes[i].set_conflict(False)
            for j in range(0, len(classes)):
                if j >= i:
                    flag = False
                    q1 = classes[i].get_meeting_time().get_days()
                    q2 = classes[j].get_meeting_time().get_days()
                    for kk in range(0, len(q1)):
                        for kkk in range(0, len(q2)):
                            w1 = classes[i].get_meeting_time().get_days()[kk]
                            w2 = classes[j].get_meeting_time().get_days()[kkk]
                            if w1 == w2:
                                flag = True
                    DuringStart = False
                    DuringEnd = False
                    SameStart = False
                    SameEnd = False

                    if classes[i].get_meeting_time().get_start() == classes[j].get_meeting_time().get_start():
                        SameStart = True
                    if classes[i].get_meeting_time().get_end() == classes[j].get_meeting_time().get_end():
                        SameEnd = True
                    if ((classes[j].get_meeting_time().get_start() < classes[i].get_meeting_time().get_start()) and
                            (classes[j].get_meeting_time().get_end() > classes[i].get_meeting_time().get_start())):
                        DuringStart = True
                    if ((classes[j].get_meeting_time().get_start() < classes[i].get_meeting_time().get_end()) and
                            (classes[j].get_meeting_time().get_end() > classes[i].get_meeting_time().get_end())):
                        DuringEnd = True
                    if (DuringStart or DuringEnd or SameStart or SameEnd) and flag and (
                            classes[i].get_id() != classes[j].get_id()):
                        if not classes[i].get_course().get_from_other_department() or classes[j] \
                                .get_course().get_from_other_department():
                            if classes[i].get_room() == classes[j].get_room():
                                self._numbOfConflicts += 1
                            # out = self.check_another_room(classes, i)
                            # if not out:
                            #     self._numbOfConflicts += 1
                            #     classes[i].set_room_conflict(True)
                            #     classes[i].set_conflict(False)

                            if classes[i].get_instructor() == classes[j].get_instructor():
                                self._numbOfConflicts += 1
                                classes[i].set_conflict(False)

                            if classes[i].get_course().check_if_optional() and classes[
                                j].get_course().check_if_optional():
                                self._numbOfConflicts += 1
                                classes[i].set_conflict(False)

                        if not (classes[i].get_course().check_if_optional()) and not \
                                (classes[j].get_course().check_if_optional()) and not \
                                classes[i].get_course().get_for_other_department() and not \
                                classes[j].get_course().get_for_other_department():
                            if ((classes[i].get_course().get_year() == classes[j].get_course().get_year()) and
                                (classes[i].get_course().get_total_number_of_sections() == 1 and classes[
                                    j].get_course().get_total_number_of_sections() == 1)) and \
                                    classes[i].get_course().get_semester() == classes[j].get_course().get_semester():
                                self._numbOfConflicts += 1
                                classes[i].set_conflict(False)

        # self.findBreakConflict(classes)

        # بدي اجيب بدل classes  اعبي فيها الاجباري بس لحاله

        m: int = 0
        for y in range(0, len(self._data.get_courses_of_years())):  # number of years

            for p in range(0, len(self._data.get_courses_of_years()[y])):  # number of courses in each year
                SectionOfClass = self._data.get_courses_of_years()[y][p]  # whole course
                if_there_is_section = False
                if 1 < len(SectionOfClass) < 4:  # same semester
                    for t in range(0, len(SectionOfClass)):
                        newclass = self.search_for_class(SectionOfClass[t], classes)
                        if not (
                                newclass.get_course().check_if_optional()) and newclass.get_course().get_semester() == \
                                self._data._semester and not newclass.get_course().get_for_other_department():
                            if not newclass.get_is_taken():
                                checked_flag = self.check_for_conflict(SectionOfClass[t], classes, len(SectionOfClass),
                                                                       p, t,
                                                                       newclass.get_course().get_department_name())
                                if not checked_flag:
                                    self._numbOfConflicts += 1
                                    newclass.set_conflict(False)

        set_taken_flages(classes)

        return 1 / (1.0 * self._numbOfConflicts + 1)

    def find_break_conflict(self, classes):
        Weight = 0
        for k in range(0, len(self._data.get_instructors())):
            FlagInst = True
            if self._data.get_instructors()[k].get_want_breaks():
                for jj in range(0, len(self._data.get_instructors()[k].get_id_for_courses())):
                    var = 0
                    classOne = self.search_for_course(classes, self._data.get_instructors()[k].get_id_for_courses()[jj])
                    for a in range(0, len(self._data.get_instructors()[k].get_id_for_courses())):
                        classTwo = self.search_for_course(classes,
                                                          self._data.get_instructors()[k].get_id_for_courses()[a])
                        durationOne = classOne.get_meeting_time().get_end() - classOne.get_meeting_time().get_start()
                        durationTwo = classTwo.get_meeting_time().get_end() - classTwo.get_meeting_time().get_start()
                        if durationOne == 1.5 and durationTwo == 1.5:
                            if classOne.get_meeting_time().get_end() == classTwo.get_meeting_time().get_start():
                                FlagInst = False
                                # self._numbOfConflicts += 1

                        if durationOne == 1 and durationTwo == 1:
                            if classOne.get_meeting_time().get_end() == classTwo.get_meeting_time().get_start() or \
                                    classOne.get_meeting_time().get_end() + 1 == classTwo.get_meeting_time().get_start():
                                var += 1
                                if var == 2:
                                    # self._numbOfConflicts += 1
                                    FlagInst = False
                                    var = 0
            Weight += 1
        return Weight

    def check_another_room(self, classes1, i):
        arr = [True] * len(self._data.get_rooms())
        classes = self.get_classes()
        meeting = classes[i].get_meeting_time().get_id()
        for k in range(0, len(classes)):
            if classes[k].get_meeting_time().get_id() == meeting:
                index = get_index(self._data.get_rooms(), classes[k].get_room())
                arr[index] = False
        for j in range(0, len(arr)):
            if arr[j] and self._data.get_rooms()[j].get_type() == classes[i].get_course().get_type():
                classes[i].set_room(self._data.get_rooms()[j])
                return True
        return False

    def check_for_conflict(self, SectionOfClass, classes, lengthOfClass, index, t, departmetName):

        newClass = self.search_for_class(SectionOfClass, classes)
        ListOfAvailableClasses = []
        ListOfFlags = []
        ListOfAvailableClasses.append(newClass)
        for i in range(0, len(self._data.get_courses_of_years()[(newClass.get_course().get_year() - 1)])):  # courses-1
            if index != i:
                if t < len(self._data.get_courses_of_years()[(newClass.get_course().get_year() - 1)][i]) and \
                        len(self._data.get_courses_of_years()[(newClass.get_course().get_year() - 1)][i]) > 1:
                    result = self.search_for_available_classes(ListOfAvailableClasses, newClass, i, classes, t)
                    if result[0].get_course().get_department_name() == departmetName:
                        ListOfAvailableClasses.append(result[0])
                        ListOfFlags.append(result[1])

        for j in range(len(ListOfFlags)):
            if not ListOfFlags[j]:
                for j in range(len(ListOfAvailableClasses)):
                    ListOfAvailableClasses[j].set_is_taken(False)
                return False
        return True

    def search_for_available_classes(self, ListOfAvailableClasses, classS, indexOfCertainClass, classes, t):
        flag = True
        returnArray = []
        year = classS.get_course().get_year()

        for j in range(0, len(self._data.get_courses_of_years()[year - 1][indexOfCertainClass])):
            for k in range(0, len(ListOfAvailableClasses)):
                classCompare = self.search_for_class(
                    self._data.get_courses_of_years()[year - 1][indexOfCertainClass][j], classes)
                if classCompare.get_course().get_semester() == self._data._semester:
                    if not (conflict(ListOfAvailableClasses[k], classCompare)):
                        flag = False
                        break
            if flag:
                returnArray.append(classCompare)
                classCompare.set_is_taken(True)
                returnArray.append(True)
                return returnArray

        returnArray.append(classCompare)
        returnArray.append(False)
        return returnArray

    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes) - 1):
            returnValue += str(self._classes[i]) + ", "

        returnValue += str(self._classes[len(self._classes) - 1])
        return returnValue
