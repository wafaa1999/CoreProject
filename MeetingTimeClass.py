class MeetingTime:
    def __init__(self, idTime, start, end, days):
        self._id = idTime
        self._start = start
        self._end = end
        self._days = days

    def get_id(self):
        return self._id

    def get_start(self):
        return self._start

    def set_start(self, start):
        self._start = start

    def get_end(self):
        return self._end

    def get_days(self):
        return self._days
