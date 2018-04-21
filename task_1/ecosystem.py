from task_1 import animals
import random


class Ecosystem:
    def __init__(self, river_length):
        self.river = River(river_length)

    def simulation(self, limit_iterations):
        try:
            for i in range(limit_iterations):
                print('{}: {}'.format(i + 1, self.river.state))
                self.river.next_state()
        except Overpopulation:
            print('Overpopulation, stop simulation.')

    def fish_count(self):
        return self.river.fish_count()

    def bear_count(self):
        return self.river.bear_count()


class River:
    def __init__(self, length):
        self._length = length
        self._num_fish = 0
        self._num_bears = 0

        self.state = []
        for i in range(length):
            animal = random.choice([animals.Fish, animals.Bear, None, None])
            if animal:
                animal = animal(i)
                if animal.TYPE == 'Fish':
                    self._num_fish += 1
                else:
                    self._num_bears += 1
            self.state.append(animal)

    def fish_count(self):
        return self._num_fish

    def bear_count(self):
        return self._num_bears

    def next_state(self):
        new_state = [[] for i in range(self._length)]
        new_animals = []
        for i, cell in enumerate(self.state):
            if cell:
                new_state[cell.choose_side(i, self._length - 1)].append(cell)

        unresolved_conflicts = True
        while unresolved_conflicts:
            unresolved_conflicts = False
            for i, cell in enumerate(new_state):
                if len(cell) == 2:
                    unresolved_conflicts = True
                    # Two animals in current cell acting
                    state_of_cell = cell[0].act(cell[1])
                    new_state[i] = []
                    if len(state_of_cell['new']) == 3:
                        new_animals.append(state_of_cell['new'][2])
                    for animal in state_of_cell['old']:
                        new_state[animal.position].append(animal)

        new_state = [cell[0] if cell else None for cell in new_state]
        i = 0
        while new_animals:
            try:
                if not new_state[i]:
                    new_state[i] = new_animals[-1]
                    new_animals.pop()
            except IndexError:
                raise Overpopulation
            i += 1

        for i, animal in enumerate(new_state):
            if animal:
                animal.position = i

        self.state = new_state


class Overpopulation(Exception):
    pass
