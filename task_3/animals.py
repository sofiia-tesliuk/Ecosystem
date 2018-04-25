import random


class Animal:
    TYPE = None
    StrType = None
    MaxLimAge = None
    BabiesCount = None

    def __init__(self, position=0, max_lim_age=0, age=None):
        self.position = position
        if age is None:
            self.age = random.randint(0, max_lim_age)
        else:
            self.age = age
        self.gender = random.choice(['M', 'F'])
        self.power = round(random.uniform(1, 5), 2)

    def add_year_to_age(self):
        """
        :return: add 1 year to age
        """
        self.age += 1

    def time_to_kill(self):
        """
        :return: if it's a high time to become dead
        """
        return self.age > self.MaxLimAge

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
            dict_gender = {'F': [], 'M': []}
            for animal in processed_animals:
                dict_gender[animal.gender].append(animal)

            try:
                female = [max(dict_gender['F'])]
            except ValueError:
                female = []

            try:
                male = [max(dict_gender['M'])]
            except ValueError:
                male = []

            f_and_m = len(female) + len(male)
            processed_animals = male + female

            if f_and_m == 1:
                return {'old': [],
                        'new': processed_animals,
                        '+': []}
            else:
                return {'old': processed_animals,
                        'new': [],
                        '+': [processed_animals[0].new_instance()
                              for i in range(female[0].BabiesCount)]}

        dict_animals = {'Bear': [], 'Fish': [], 'Otter': []}
        for animal in animals:
            dict_animals[animal.__class__.__name__].append(animal)

        if dict_animals['Bear']:
            return process_animals(dict_animals['Bear'])
        elif dict_animals['Otter']:
            return process_animals(dict_animals['Otter'])
        else:
            return process_animals(dict_animals['Fish'])

    def __str__(self):
        return self.StrType + str(int(self.power)) + self.gender + str(self.age)

    def __repr__(self):
        return self.__str__()

    def __gt__(self, other):
        """
        :param other: another animal
        :return: if self > other
        """
        if self.power > other.power:
            return True
        elif self.power == other.power:
            if self.age < other.age:
                return True
        return False

    def __ge__(self, other):
        """
        :param other: another animal
        :return: if self >= other
        """
        if self.power > other.power:
            return True
        elif self.power == other.power:
            if self.age <= other.age:
                return True
        return False

    def new_instance(self):
        raise NotImplementedError


class Bear(Animal):
    TYPE = 'Bear'
    StrType = 'B'
    MaxLimAge = 10
    BabiesCount = 2

    def __init__(self, position=0, age=None):
        super().__init__(position, Bear.MaxLimAge, age)

    def new_instance(self):
        return Bear(age=0)


class Fish(Animal):
    TYPE = 'Fish'
    StrType = 'F'
    MaxLimAge = 5
    BabiesCount = 7

    def __init__(self, position=0, age=None):
        super().__init__(position, Fish.MaxLimAge, age)

    def new_instance(self):
        return Fish(age=0)


class Otter(Animal):
    TYPE = 'Otter'
    StrType = 'O'
    MaxLimAge = 12
    BabiesCount = 3

    def __init__(self, position=0, age=None):
        super().__init__(position, Otter.MaxLimAge, age)

    def new_instance(self):
        return Otter(age=0)
