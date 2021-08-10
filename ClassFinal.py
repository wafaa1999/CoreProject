

class Classing:

    def __init__(self, courseNumber, courseName, days, startHour, endHour,
                 roomNumber, instName, roomType, classConflict,
                 flagConflict ,year , numberOfSections, semester):
        self._courseNumber = courseNumber
        self._courseName = courseName
        self._startHour = startHour
        self._endHour = endHour
        self._roomNumber = roomNumber
        self._roomType = roomType
        self._instName = instName
        self._classConflict = classConflict
        self._flagConflict = flagConflict
        self._days = []
        arr = days.split(',')
        for i in range(len(arr)):
            self._days.append(arr[i])
        self._year = year
        self._totalNumberOfSections = numberOfSections
        self._semester = semester

    def get_course_number(self): return self._courseNumber

    def get_semester(self): return self._semester

    def get_total_number_of_sections(self): return self._totalNumberOfSections

    def get_year(self): return self._year

    def get_course_name(self): return self._courseName

    def get_start_hour(self): return self._startHour

    def get_end_hour(self): return self._endHour

    def get_room_number(self): return self._roomNumber

    def get_room_type(self): return self._roomType

    def get_inst_name(self): return self._instName

    def get_class_conflict(self): return self._classConflict

    def get_flag_conflict(self): return self._flagConflict

    def get_days(self): return self._days

    def set_class_conflict(self, value):  self._classConflict = value

    def set_flag_conflict(self, value): self._flagConflict = value










