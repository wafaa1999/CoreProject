class Class:
    def __init__(self, idClass, course):
        self._id = idClass
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._room = None
        self._isTaken = False
        self._conflict = True
        self._room_conflict = False
        self._class_conflict = -1
        self._flag_conflict = False

    def get_room_conflict(self): return self._room_conflict

    def set_room_conflict(self, value): self._room_conflict = value

    def get_class_conflict(self): return self._class_conflict

    def set_class_conflict(self, value): self._class_conflict = value

    def get_flag_conflict(self): return self._flag_conflict

    def set_flag_conflict(self, value): self._flag_conflict = value

    def get_id(self): return self._id

    def get_conflict(self): return self._conflict

    def set_conflict(self, conflict): self._conflict = conflict

    def get_is_taken(self): return self._isTaken

    def set_is_taken(self, isTaken):  self._isTaken = isTaken

    def get_course(self): return self._course

    def get_instructor(self): return self._instructor

    def get_meeting_time(self): return self._meetingTime

    def get_room(self): return self._room

    def set_instructor(self, instructor): self._instructor = instructor

    def set_meeting_time(self, meetingTime): self._meetingTime = meetingTime

    def set_room(self, room): self._room = room

    def set_is_taken(self, isTaken): self._isTaken = isTaken

    def __str__(self):
        return str(self._course.get_name()) + "," + str(self._room.get_number()) + "," + str(
            self._instructor.get_name()) + "," + str(self._meetingTime.get_id())
