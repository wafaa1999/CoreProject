from PopulationClass import Population
from ScheduleClass import Schedule
import random as rnd

POPULATION_SIZE = 2
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.15


def get_index(rooms, room):
    for i in range(0, len(rooms)):
        if rooms[i].get_number() == room.get_number():
            return i
    return -1


class GeneticAlgorithm:
    def __init__(self, data):
        self._data = data

    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0, self._data)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        first_time = True
        while i < POPULATION_SIZE:
            if first_time:
                crossover_pop.get_schedules().append(pop.get_schedules()[i])
                first_time = False
            else:
                schedule1 = self._select_tournament_population(pop).get_schedules()[0]
                schedule2 = self._select_tournament_population(pop).get_schedules()[0]
                crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
            # self.check_another_room(population.get_schedules()[i])

        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule(self._data).initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if rnd.random() > 0.5:
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        crossoverSchedule.calculate_fitness
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule(self._data).initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            if not mutateSchedule.get_classes()[i].get_conflict():
                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
            if MUTATION_RATE > rnd.random():
                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]

        for i in range(0, len(mutateSchedule.get_classes())):
            for k in range(0, len(mutateSchedule.get_classes())):
                if not mutateSchedule.get_classes()[k].get_course().get_from_other_department() and \
                        not mutateSchedule.get_classes()[i].get_course().get_from_other_department():
                    if mutateSchedule.get_classes()[k].get_room() == mutateSchedule.get_classes()[i].get_room() and \
                            mutateSchedule.get_classes()[k].get_meeting_time() == mutateSchedule.get_classes()[i] \
                            .get_meeting_time() and i != k:
                        arr = [True] * len(self._data.get_rooms())
                        meeting = mutateSchedule.get_classes()[i].get_meeting_time()
                        for p in range(0, len(mutateSchedule.get_classes())):
                            if not mutateSchedule.get_classes()[p].get_course().get_from_other_department():
                                if mutateSchedule.get_classes()[p].get_meeting_time() == meeting:
                                    index = get_index(self._data.get_rooms(),
                                                      mutateSchedule.get_classes()[p].get_room())
                                    arr[index] = False

                        for j in range(0, len(arr)):

                            if arr[j] and self._data.get_rooms()[j].get_type() == mutateSchedule.get_classes()[i] \
                                    .get_course().get_type():
                                schedule.get_classes()[i].set_room(self._data.get_rooms()[j])
                                schedule.get_classes()[i].set_instructor(
                                    mutateSchedule.get_classes()[i].get_instructor())
                                schedule.get_classes()[i].set_meeting_time(
                                    mutateSchedule.get_classes()[i].get_meeting_time())
                                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
                                break

        mutateSchedule.calculate_fitness
        return mutateSchedule

    def _select_tournament_population(self, pop):
        tournament_pop = Population(0, self._data)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop
