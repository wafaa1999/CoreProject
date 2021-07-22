class SoftConstrains:
    def __init__(self, listOfAllGenerations, data, softConstrain):
        self._listOfGenerations = []
        self._data = data
        self._softConstrains = softConstrain
        for i in range(len(listOfAllGenerations)):
            self._listOfGenerations.append(listOfAllGenerations[i])

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
            flagNotWanted = True
            for j in range(len(classes)):  # "I1", ["Sunday", "Tuesday"], 8, 9, False, 0.5
                condition2 = True
                condition1 = self._softConstrains[i][0] == classes[j].get_instructor().get_id()
                for k in range(len(self._softConstrains[i][1])):
                    if self._softConstrains[i][1][k] != classes[j].get_metting_time().get_days()[k]:
                        condition2 = False
                condition3 = self._softConstrains[i][2] == classes[j].get_metting_time().get_start()
                condition4 = self._softConstrains[i][3] == classes[j].get_metting_time().get_end()
                if self._data.get_soft_constraints()[i][4]:
                    if condition1 and condition2 and condition3 and condition4:
                        if self._softConstrains[i][5] == 1:
                            generation.inc_superiority_weight()
                        elif self._softConstrains[i][5] == 0.5:
                            generation.inc_middleware_weight()
                        elif self._softConstrains[i][5] == 0.3:
                            generation.inc_leastwise_weight()
                        break

                else:
                    if condition1 and condition2 and condition3 and condition4:
                        flagNotWanted = False

            if flagNotWanted:
                if self._softConstrains[i][5] == 1:
                    generation.inc_superiority_weight()
                elif self._softConstrains[i][5] == 0.5:
                    generation.inc_middleware_weight()
                elif self._softConstrains[i][5] == 0.3:
                    generation.inc_leastwise_weight()
