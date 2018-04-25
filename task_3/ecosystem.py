from task_3 import animals
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
                print('Fishes: {}, Otters: {}, Bears: {}'
                      .format(self.fish_count(), self.otter_count(), self.bear_count()))
                if not self.animal_count():
                    raise EmptyEcosystem
                self.river.next_state()
        except Overpopulation:
            print('Overpopulation, stop simulation.')
        except EmptyEcosystem:
            print('Seems that there is no one in ecosystem anymore.')

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

    def otter_count(self):
        """
        :return: number of otters in river
        """
        return self.river.otter_count()

    def animal_count(self):
        """
        :return: number of animals in ecosystem
        """
        return self.river.animal_count()


class River:
    def __init__(self, length):
        self._length = length
        self._count_an_type = {'Fish': 0, 'Otter': 0, 'Bear': 0}
        self._count_an = 0
        self._storage_an = {'Fish': [], 'Otter': [], 'Bear': []}
        self.state = self.generate_state()

    def __str__(self):
        string = [str(animal) if animal else '    ' for animal in self.state]
        return '|'.join(string)

    def generate_state(self):
        """
        :return: randomly generated state (consists of fishes, bears and None)
        """
        state = []
        for i in range(self._length):
            animal = random.choice([animals.Fish, animals.Bear, animals.Otter, None, None])
            if animal:
                animal = animal(i)
                self.item_registration(animal)
            state.append(animal)
        return state

    def fish_count(self):
        """
        :return: number of fishes in river
        """
        return self._count_an_type['Fish']

    def bear_count(self):
        """
        :return: number of bears in river
        """
        return self._count_an_type['Bear']

    def otter_count(self):
        """
        :return: number of otters in river
        """
        return self._count_an_type['Otter']

    def animal_count(self):
        """
        :return: number of animals in ecosystem
        """
        return self._count_an

    def add_new_animal(self, new_animal, first_time=True):
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
                    new_animal.position = index_l
                    return None
                elif not self.state[index_r]:
                    self.state[index_r] = new_animal
                    new_animal.position = index_r
                    return None
            except IndexError:
                continue

        # if overpopulation
        if first_time:
            first_time = False
            # Decrease population
            self.check_population()
            self.add_new_animal(new_animal, first_time)
        raise Overpopulation

    def remove_animal(self, animal):
        """
        Remove animal from ecosystem
        :return:
        """
        self.state[animal.position] = None

    def item_registration(self, animal):
        """
        :param animal: animal
        :return: increase number of animals in river of the same class
        """
        if isinstance(animal, animals.Fish):
            self._count_an_type['Fish'] += 1
            self._storage_an['Fish'].append(animal)
        elif isinstance(animal, animals.Otter):
            self._count_an_type['Otter'] += 1
            self._storage_an['Otter'].append(animal)
        else:
            self._count_an_type['Bear'] += 1
            self._storage_an['Bear'].append(animal)
        self._count_an += 1

    def check_age(self):
        """
        Add 1 year of age to each animal in state,
        if age of animal > max_age, animal becomes dead.
        :return: None
        """
        for animal in self.state:
            if animal:
                animal.add_year_to_age()
                if animal.time_to_kill():
                    self.remove_animal(animal)

    def update_info(self):
        """
        Update info about animals in river
        """
        for an_type in self._count_an_type:
            self._count_an_type[an_type] = 0

        for an_type in self._storage_an:
            self._storage_an[an_type] = []

        for animal in self.state:
            if animal:
                self.item_registration(animal)

    def check_population(self):
        """
        Check if type of animals cover river less than 60 percent
        of ecosystem
        """
        self.update_info()
        self._count_an = sum(self._count_an_type.values())
        overpopulation_type = True
        while overpopulation_type:
            overpopulation_type = False
            for an_type, an_count in self._count_an_type.items():
                if an_count > 0.6 * self._count_an:
                    overpopulation_type = True
                    self.decrease_population(an_type, 2 * an_count - self._count_an)

    def decrease_population(self, an_type, number):
        """
        Decrease population of selected type in river
        :param an_type: type of animal
        :param number: number to decrease
        """
        an_type_storage = self._storage_an[an_type]
        an_type_storage.sort(key=(lambda x: x.age))
        index_kill = random.randint(0, 1)
        for i in range(number):
            animal_to_kill = an_type_storage[-index_kill]
            self.remove_animal(animal_to_kill)
            self._count_an -= 1
            self._count_an_type[animal_to_kill.TYPE] -= 1
            an_type_storage.pop(-index_kill)
            index_kill = not index_kill

    def next_state(self):
        """
        changes configuration in river
        :return: None
        """
        self.check_age()

        new_state = [[] for i in range(self._length)]
        new_animals = []
        for i, cell in enumerate(self.state):
            if cell:
                new_state[cell.choose_side(i, self._length - 1)].append(cell)

        # Process cells, in which 2 and more animals
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
                        animal.position = i
                    new_animals.extend(state_of_cell['+'])
                elif len(cell):
                    cell[0].position = i

        self.state = [cell[0] if cell else None for cell in new_state]
        # Add born animals to current state
        for animal in new_animals:
            self.add_new_animal(animal)

        self.check_population()


class Overpopulation(Exception):
    pass


class EmptyEcosystem(Exception):
    pass
