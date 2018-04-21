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

    def act(self, other):
        if self.TYPE != other.TYPE:
            return {'old': [self, other], 'new': [[self, other][self.TYPE == 'Fish']]}
        else:
            return {'old': [self, other], 'new': [self, other, self.new_instance()]}

    def __str__(self):
        return self.StrType

    def __repr__(self):
        return self.StrType

    def new_instance(self):
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
