from DataClass import Data
from DisplayClass import DisplayMgr, print_schedule_as_table, print_generation
from GeneticClass import GeneticAlgorithm
from PopulationClass import Population
from SoftConstrainsClass import SoftConstrains

POPULATION_SIZE = 15


def checkIfEq(schedule1, schedule2):
    classes1 = schedule1.get_classes()
    classes2 = schedule2.get_classes()
    for j in range(0, len(classes1)):
        if (classes1[j].get_instructor().get_id() != classes2[j].get_instructor().get_id()) or (
                classes1[j].get_meeting_time().get_id() != classes2[j].get_meeting_time().get_id()) \
                or (classes1[j].get_room().get_number() != classes2[j].get_room().get_number()):
            return False
    return True


class Solve:

    def __init__(self, ROOMS, MEETING_TIMES_1, MEETING_TIMES_LABS, MEETING_TIMES_3, INSTRUCTORS, MEETING_TIMES_2,
                 SOFT_CONSTRAINTS, idDep, tableName, softFlag):
        self._listOfGeneration = []
        self._data = Data(ROOMS, MEETING_TIMES_1, MEETING_TIMES_LABS, MEETING_TIMES_3, INSTRUCTORS, MEETING_TIMES_2, idDep, tableName)
        self.soft = SoftConstrains

    def solve(self):
        counter1 = 0
        counter2 = 0
        counter = 0
        currentState = 0
        for i in range(0, 1):
            flag = False
            displayMgr = DisplayMgr(self._data)
            generationNumber = 0
            population = Population(POPULATION_SIZE, self._data)
            d = population.get_schedules()[0].get_fitness()

            population.get_schedules().sort(key=lambda x1: x1.get_fitness(), reverse=True)
            geneticAlgorithm = GeneticAlgorithm(self._data)
            print_schedule_as_table(population.get_schedules()[0])
            while population.get_schedules()[0].get_fitness() != 1.0:
                generationNumber += 1
                if currentState == population.get_schedules()[0].get_fitness():
                    counter += 1
                else:
                    currentState = population.get_schedules()[0].get_fitness()
                    counter = 0
                # if counter == 400:
                # displayMgr.print_schedule_as_table(population.get_schedules()[0])
                # flag = True

                print("\n> Generation # " + str(generationNumber))
                print("number of results =" + str(counter1))

                population = geneticAlgorithm.evolve(population)
                population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
                print_generation(population)

                if (generationNumber % 20) == 0 and population.get_schedules()[0].get_fitness() != 1.0:
                    sec = population.get_schedules()[0]
                    self.cal(sec)
                    print_schedule_as_table(population.get_schedules()[0])
                # if population.get_schedules()[0].get_fitness() == 1.0 or flag :
                #     counter1 += 1
                #
                #     print("\n> Generation # " + str(generationNumber) + "   i #" + str(i))
                #     if len(self._listOfGenaration) == 0:
                #         self._listOfGenaration.append((population.get_schedules()[0]))
                #     for w in range(0, len(self._listOfGenaration)):
                #         FlagForEq = self.checkIfEq(self._listOfGenaration[w], population.get_schedules()[0])
                #         if FlagForEq:
                #             break
                #     if not FlagForEq:
                #         self._listOfGenaration.append(population.get_schedules()[0])
                # print("number of diff results =" + str(len(self._listOfGenaration)))
        print_generation(population)
        for f in range(len(self._listOfGeneration)):
            print_schedule_as_table(self._listOfGeneration[f])
        SoftCon = SoftConstrains(self._data, self._listOfGeneration, self.soft)
        print_schedule_as_table(SoftCon)

    def cal(self, sch):
        counter = 0
        classes = sch.get_classes()
        for i in range(0, len(classes)):
            # classes[i]._isTaken = False
            # classes[i]._conflict = True
            classes[i].set_conflict(True)

            if not classes[i].get_course().get_from_other_department():
                if classes[i].get_room().get_type() != classes[i].get_course().get_type():
                    print("room type")
                    print("calss i  = ")
                    print(classes[i])
                    print("calss j  = ")
                    print(classes[j])
                    counter += 1
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
                        if not classes[i].get_course().get_from_other_department() or classes[
                            j].get_course().get_from_other_department():
                            if classes[i].get_room() == classes[j].get_room():
                                print("room conflict")
                                print("calss i  = ")
                                print(classes[i])
                                print("calss j  = ")
                                print(classes[j])
                                counter += 1
                                classes[i].set_conflict(False)

                            if classes[i].get_instructor() == classes[j].get_instructor():
                                print("instroctor conflict")
                                print("calss i  = ")
                                print(classes[i])
                                print("calss j  = ")
                                print(classes[j])
                                counter += 1
                                classes[i].set_conflict(False)

                            if classes[i].get_course().check_if_optional() and classes[
                                j].get_course().check_if_optional():
                                print("optinal. conflict")
                                print("calss i  = ")
                                print(classes[i])
                                print("calss j  = ")
                                print(classes[j])
                                counter += 1
                                classes[i].set_conflict(False)

                        if not (classes[i].get_course().check_if_optional()) and not \
                                (classes[j].get_course().check_if_optional()) and not \
                                classes[i].get_course().get_for_other_department() and not \
                                classes[j].get_course().get_for_other_department():
                            if ((classes[i].get_course().get_year() == classes[j].get_course().get_year()) and \
                                (classes[i].get_course().get_total_number_of_sections() == 1 or classes[ \
                                        j].get_course().get_total_number_of_sections() == 1)) and \
                                    classes[i].get_course().get_semester() == classes[j].get_course().get_semester():
                                print("one comp. conflict")
                                print("calss i  = ")
                                print(classes[i])
                                print("calss j  = ")
                                print(classes[j])
                                counter += 1
                                classes[i].set_conflict(False)
            for k in range(0, len(self._data.get_instructors())):
                for jj in range(0, len(self._data.get_instructors()[k].get_id_for_courses())):
                    var = 0
                    classOne = sch.search_for_course(classes, self._data.get_instructors()[k].get_id_for_courses()[jj])
        for a in range(0, len(self._data.get_instructors()[k].get_id_for_courses())):
            classTwo = sch.search_for_course(classes, self._data.get_instructors()[k].get_id_for_courses()[a])
            durationOne = classOne.get_meeting_time().get_end() - classOne.get_meeting_time().get_start()
            durationTwo = classTwo.get_meeting_time().get_end() - classTwo.get_meeting_time().get_start()
            if durationOne == 1.5 and durationTwo == 1.5:
                if classOne.get_meeting_time().get_end() == classTwo.get_meeting_time().get_start():
                    print("duration 1.5")
                    print("calss i  = ")
                    print(classOne)
                    print("calss j  = ")
                    print(classTwo)
                    counter += 1
            if durationOne == 1 and durationTwo == 1:
                if classOne.get_meeting_time().get_end() == classTwo.get_meeting_time().get_start() or \
                        classOne.get_meeting_time().get_end() + 1 == classTwo.get_meeting_time().get_start():
                    var += 1
                    if var == 2:
                        print("duration 1")
                        print("calss i  = ")
                        print(classOne)
                        print("calss j  = ")
                        print(classTwo)
                        counter += 1
                        var = 0

                # بدي اجيب بدل classes  اعبي فيها الاجباري بس لحاله
            m: int = 0
            for y in range(0, len(self._data.get_courses_of_years())):  # number of years

                for p in range(0, len(self._data.get_courses_of_years()[y])):  # number of courses in each year
                    SectionOfClass = self._data.get_courses_of_years()[y][p]  # whole course
                    if_there_is_section = False
                    if 1 < len(SectionOfClass) < 4:  # كمان لازم اتأكد اانو نفس الفصل
                        for t in range(0, len(SectionOfClass)):
                            newclass = sch.search_for_class(SectionOfClass[t], classes)
                            if not (
                                    newclass.get_course().check_if_optional()) and newclass.get_course().get_semester() == self._data._semester \
                                    and not newclass.get_course().get_for_other_department():
                                if not newclass.get_is_taken():
                                    checked_flag = sch.check_for_conflict(SectionOfClass[t], classes,
                                                                          len(SectionOfClass), p, t)
                                    if not checked_flag:
                                        print("grouping")
                                        print("calss i  = ")
                                        print(classes[i])
                                        print("calss j  = ")
                                        print(classes[j])
                                        counter += 1
                                        newclass.set_conflict(False)

            for m in range(len(classes)):
                classes[m].set_is_taken(False)
        print("conflict is = " + str(counter))
