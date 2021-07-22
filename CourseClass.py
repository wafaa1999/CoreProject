
class Course:
    def __init__(self, number, numberType, name, instructors, type, year, sectionNumber, totalNumberOfSections, semester,
                 fromOtherDepartment, sharedTimeslot, forOtherDepartment, departmentName):
        self._number = number
        self._numberType = numberType
        self._name = name
        self._type = type
        self._instructors = instructors
        self._year = year
        self._sectionNumber = sectionNumber
        self._totalNumberOfSections = totalNumberOfSections
        self._semester = semester
        self._fromOtherDepartment = fromOtherDepartment
        self._sharedTimeslot = sharedTimeslot
        self._forOtherDepartment = forOtherDepartment
        self._departmentName = departmentName

    def get_from_other_department(self):
        return self._fromOtherDepartment

    def get_department_name(self):
        return self._departmentName

    def get_for_other_department(self):
        return self._forOtherDepartment

    def get_shared_time_slot(self):
        return self._sharedTimeslot

    def get_number(self): return self._number

    def check_if_optional(self):
        if self._semester == -1:
            return True
        else:
            return False

    def get_semester(self): return self._semester

    def get_number_type(self): return self._numberType

    def get_name(self): return self._name

    def get_instructors(self): return self._instructors

    def get_year(self): return self._year

    def get_type(self): return self._type

    def get_section_number(self): return self._sectionNumber

    def get_total_number_of_sections(self): return self._totalNumberOfSections

    def __str__(self): return self._name
