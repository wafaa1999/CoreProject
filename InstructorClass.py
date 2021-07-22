class Instructor:
    def __init__(self, idInstructor, name, wantBreaks):
        self._id = idInstructor
        self._name = name
        self._idForCourses = []
        self._wantBreaks = wantBreaks

    def get_id(self): return self._id

    def get_id_for_courses(self): return self._idForCourses

    def add_id_to_courses(self, value): self._idForCourses.append(value)

    def get_name(self): return self._name

    def get_want_breaks(self): return self._wantBreaks

    def __str__(self): return self._name
