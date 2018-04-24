import random


class Animal:
    TYPE = None
    StrType = None

    def __init__(self, position=0):
        self.position = position

    @staticmethod
    def choose_side(i, max_lim):
        """
        :param i: index of current position
        :param max_lim: max limit of index
        :return: randomly choose side
        """
        if i == 0:
            return i + random.randint(0, 1)
        elif i == max_lim:
            return i + random.randint(-1, 0)
        else:
            return i + random.randint(-1, 1)

    @staticmethod
    def acting_many(animals):
        def process_animals(processed_animals):
            if len(processed_animals) == 1:
                return {'old': [],
                        'new': processed_animals,
                        '+': []}
            elif len(processed_animals) == 2:
                return {'old': processed_animals,
                        'new': [],
                        '+': [processed_animals[0].new_instance()]}
            elif len(processed_animals) == 3:
                return {'old': processed_animals,
                        'new': [],
                        '+': [processed_animals[0].new_instance()
                              for i in range(3)]}

        dict_animals = {'Bear': [], 'Fish': []}
        for animal in animals:
            dict_animals[animal.__class__.__name__].append(animal)
        if dict_animals['Bear']:
            return process_animals(dict_animals['Bear'])
        else:
            return process_animals(dict_animals['Fish'])

    def __str__(self):
        return self.StrType

    def __repr__(self):
        return self.StrType

    def new_instance(self):
        """
        :return: created new instance of animal with type as parent
        """
        raise NotImplementedError


class Bear(Animal):
    TYPE = 'Bear'
    StrType = 'B'

    def new_instance(self):
        return Bear()


class Fish(Animal):
    TYPE = 'Fish'
    StrType = 'F'

    def new_instance(self):
        return Fish()
