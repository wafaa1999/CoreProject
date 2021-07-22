import prettytable as prettytable


def print_generation(population):
    table1 = prettytable.PrettyTable(
        ['schedule #', 'fitness', '# of conflicts'])
    schedules = population.get_schedules()
    for i in range(0, len(schedules)):
        x = schedules[i].get_fitness()
        y = schedules[i].get_numb_of_conflicts()
        # z = schedules[i].__str__()
        table1.add_row([str(i), round(x, 3), y])
    print(table1)


def print_schedule_as_table(schedule):
    classes = schedule.get_classes()
    table = prettytable.PrettyTable(
        ['Class #', 'Course (number, type)', 'Room (type)', 'Instructor (Id)', 'Meeting Time (Id)'])
    for i in range(0, len(classes)):
        if not classes[i].get_course().get_from_other_department():
            table.add_row([str(i), classes[i].get_course().get_name() + " (" +
                           classes[i].get_course().get_number() + ", " +
                           str(classes[i].get_course().get_type()) + ")",
                           classes[i].get_room().get_number() + " (" + str(classes[i].get_room().get_type()) + ")",
                           classes[i].get_instructor().get_name() + " (" + str(
                               classes[i].get_instructor().get_id()) + ")",
                           str(classes[i].get_meeting_time().get_start()) + ":" + str(
                               classes[i].get_meeting_time().get_end()) +
                           str(classes[i].get_meeting_time().get_days()) + " (" +
                           str(classes[i].get_meeting_time().get_id()) + ")"])
    print(table)
    # instructor_ID , days , start time ,end time , is_wanted , weight


class DisplayMgr:
    def __init__(self, data):
        self._data = data

    def print_available_data(self):
        print("> All Available Data")
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_meeting_times()

    def print_course(self):
        availableCoursesTable = prettytable.PrettyTable(['id', 'course #', 'type of room', 'instructors'])
        courses = self._data.get_courses()
        for i in range(0, len(courses)):
            instructors = courses[i].get_instructors()
            tempStr = ""
            tempStr += instructors.__str__()
            availableCoursesTable.add_row(
                [courses[i].get_number(), courses[i].get_name(), str(courses[i].get_type()), tempStr])
        print(availableCoursesTable)

    def print_instructor(self):
        availableInstructorsTable = prettytable.PrettyTable(['id', 'instructor'])
        instructors = self._data.get_instructors()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row([instructors[i].get_id(), instructors[i].get_name()])
        print(availableInstructorsTable)

    def print_room(self):
        availableRoomsTable = prettytable.PrettyTable(['room #', 'room type'])
        rooms = self._data.get_rooms()
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].get_number()), str(rooms[i].get_type())])
        print(availableRoomsTable)

    def print_meeting_times(self):
        availableMeetingTimeTable = prettytable.PrettyTable(['id', 'starting time', 'ending time', 'days'])
        meetingTimes = self._data.get_meeting_times_1()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row(
                [meetingTimes[i].get_id(), meetingTimes[i].get_start(), meetingTimes[i].get_end(),
                 meetingTimes[i].get_days()])
        print(availableMeetingTimeTable)

        availableMeetingTimeTable = prettytable.PrettyTable(['id', 'starting time', 'ending time', 'days'])
        meetingTimes = self._data.get_meeting_times_2()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row(
                [meetingTimes[i].get_id(), meetingTimes[i].get_start(), meetingTimes[i].get_end(),
                 meetingTimes[i].get_days()])
        print(availableMeetingTimeTable)

        availableMeetingTimeTable = prettytable.PrettyTable(['id', 'starting time', 'ending time', 'days'])
        meetingTimes = self._data.get_meeting_times_3()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row(
                [meetingTimes[i].get_id(), meetingTimes[i].get_start(), meetingTimes[i].get_end(),
                 meetingTimes[i].get_days()])
        print(availableMeetingTimeTable)
