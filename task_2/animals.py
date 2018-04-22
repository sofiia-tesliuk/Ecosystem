import random


class Animal:
    """Represents animals"""
    def __init__(self):
        self.sex = random.choice([True, False])
        self.power = random.randint(1, 10) / 10
        self.direction = None
        self.index = 0

    def check_sex(self, other):
        """Return True if two animals have one class"""
        if self.__class__.__name__ == other.__class__.__name__:
            return True
        else:
            return False

    def fight_or_reproduction(self, other):
        """Verifies whether the objects are of the same sex"""
        return True if self.sex is other.sex else False

    def fight(self, other):
        return True if self.power > other.power else False


class Fish(Animal):
    """Represents fishes"""
    pass


class Bear(Animal):
    """Represents """
    pass
