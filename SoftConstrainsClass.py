class SoftConstrains:

    def __init__(self, data, listOfAllGenerations, softConstrain):
        self._data = data
        self._softConstrains = softConstrain
        self._listOfGenerations = listOfAllGenerations

    def check_for_soft_con(self):
        schedulerWithMaxWeight = self._listOfGenerations[0]
        k = 0
        for i in range(0, len(self._listOfGenerations)):
            self.calculate_wight(self._listOfGenerations[i])
            if self._listOfGenerations[i].get_superiority_weight() > schedulerWithMaxWeight.get_superiority_weight():
                schedulerWithMaxWeight = self._listOfGenerations[i]
            elif self._listOfGenerations[
                i].get_superiority_weight() == schedulerWithMaxWeight.get_superiority_weight() and \
                    self._listOfGenerations[i].get_middleware_wight() > schedulerWithMaxWeight.get_middleware_wight():
                schedulerWithMaxWeight = self._listOfGenerations[i]
            elif self._listOfGenerations[
                i].get_superiority_weight() == schedulerWithMaxWeight.get_superiority_weight() and \
                    self._listOfGenerations[
                        i].get_middleware_wight() == schedulerWithMaxWeight.get_middleware_wight() and \
                    self._listOfGenerations[i].get_leastwise_weight() > schedulerWithMaxWeight.get_leastwise_weight():
                schedulerWithMaxWeight = self._listOfGenerations[i]

        return schedulerWithMaxWeight

    def calculate_wight(self, generation):
        classes = generation.get_classes()
        weight = 0
        for i in range(len(self._softConstrains)):
                flagNotFound = True
                for j in range(len(classes)):  # "I1", ["Sunday", "Tuesday"], 8, 9, False, 0.5
                    if classes[j].get_course().get_from_other_department() == False:
                        condition2 = True
                        condition1 = self._softConstrains[i][0] == str(classes[j].get_instructor().get_id())
                        if condition1:
                            min = len(classes[j].get_meeting_time().get_days())
                            if len(self._softConstrains[i][1]) < min:
                                min = len(self._softConstrains[i][1])
                            for k in range(min):
                                if self._softConstrains[i][1][k] != classes[j].get_meeting_time().get_days()[k]:
                                    condition2 = False
                            condition3 = self._softConstrains[i][2] == classes[j].get_meeting_time().get_start()
                            condition4 = self._softConstrains[i][3] == classes[j].get_meeting_time().get_end()

                        if self._softConstrains[i][4] == 'true':
                            if condition1 and condition2 and condition3 and condition4:
                                if self._softConstrains[i][5] == '0.9':
                                    generation.inc_superiority_weight()
                                elif self._softConstrains[i][5] == '0.6':
                                    generation.inc_middleware_weight()
                                elif self._softConstrains[i][5] == '0.3':
                                    generation.inc_leastwise_weight()
                                break

                        else:
                            if condition1 and condition2 and condition3 and condition4:
                                flagNotFound = False

                    if flagNotFound:
                        if self._softConstrains[i][5] == '0.9':
                            generation.inc_superiority_weight()
                        elif self._softConstrains[i][5] == '0.6':
                            generation.inc_middleware_weight()
                        elif self._softConstrains[i][5] == '0.3':
                            generation.inc_leastwise_weight()


