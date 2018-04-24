from task_1 import animals
import random


class Ecosystem:
    def __init__(self, river_length):
        self.river = River(river_length)

    def simulation(self, limit_iterations):
        """
        Simulation of ecosystem
        :param limit_iterations: max number of iterations
        :return: None (prints state of river in each iteration)
        """
        try:
            for i in range(limit_iterations):
                print('\n{}: {}'.format(i + 1, self.river))
                print('Fishes: {}, Bears: {}'.format(self.fish_count(), self.bear_count()))
                self.river.next_state()
        except Overpopulation:
            print('Overpopulation, stop simulation.')

    def fish_count(self):
        """
        :return: number of fishes in river
        """
        return self.river.fish_count()

    def bear_count(self):
        """
        :return: number of bears in river
        """
        return self.river.bear_count()


class River:
    def __init__(self, length):
        self._length = length
        self.state = self.generate_state()

    def __str__(self):
        string = [animal.StrType if animal else ' ' for animal in self.state]
        return ''.join(string)

    def generate_state(self):
        """
        :return: randomly generated state (consists of fishes, bears and None)
        """
        state = []
        for i in range(self._length):
            animal = random.choice([animals.Fish, animals.Bear, None, None])
            if animal:
                animal = animal(i)
            state.append(animal)
        return state

    def fish_count(self):
        """
        :return: number of fishes in river
        """
        num_fish = (list(map(lambda animal: animal.TYPE if animal else None,
                             self.state))).count('Fish')
        return num_fish

    def bear_count(self):
        """
        :return: number of bears in river
        """
        num_bear = (list(map(lambda animal: animal.TYPE if animal else None,
                             self.state))).count('Bear')
        return num_bear

    def add_new_animal(self, new_animal):
        """
        Add in river state new animal in randomly choose position
        :param new_animal: animal
        :return: None
        """
        index_l = random.randint(1, self._length)
        index_r = index_l
        while (index_l >= 0) or (index_r < self._length):
            index_l -= 1
            index_r += 1
            try:
                if not self.state[index_l]:
                    self.state[index_l] = new_animal
                    return None
                elif not self.state[index_r]:
                    self.state[index_r] = new_animal
                    return None
            except IndexError:
                continue
        raise Overpopulation

    def next_state(self):
        """
        changes configuration in river
        :return: None
        """
        new_state = [[] for i in range(self._length)]
        new_animals = []
        for i, cell in enumerate(self.state):
            if cell:
                new_state[cell.choose_side(i, self._length - 1)].append(cell)

        unresolved_conflicts = True
        while unresolved_conflicts:
            unresolved_conflicts = False
            for i, cell in enumerate(new_state):
                if len(cell) >= 2:
                    unresolved_conflicts = True
                    # Animals in current cell acting
                    state_of_cell = cell[0].acting_many(cell)
                    new_state[i] = []
                    for animal in state_of_cell['old']:
                        new_state[animal.position].append(animal)
                    for animal in state_of_cell['new']:
                        new_state[i] = [animal]
                    new_animals.extend(state_of_cell['+'])

        self.state = [cell[0] if cell else None for cell in new_state]
        for animal in new_animals:
            self.add_new_animal(animal)

        for i, animal in enumerate(self.state):
            if animal:
                animal.position = i


class Overpopulation(Exception):
    pass
