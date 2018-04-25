from task_2.animals import *


class Ecosystem:
    """Represents ecosystem and river """
    def __init__(self):
        self.river = []

    def add_animals(self, n):
        """Create primary river"""
        for i in range(n):
            animal = random.choice(["fish", "bear", "none"])
            if animal == "fish":
                self.river.append(Fish())
            elif animal == "bear":
                self.river.append(Bear())
            else:
                self.river.append(None)
        return self.river

    def move(self):
        """This function does a cycle of ecosystem"""
        children = []
        new_list = [None] * (len(self.river))
        for ind, animal in enumerate(self.river):
            if animal is not None:
                animal.direction = random.choice([None, "left", "right"])
                if animal.direction == "left":
                    if ind == 0:
                        animal.index = 0
                    else:
                        animal.index = ind - 1
                if animal.direction == "right":
                    if ind == len(self.river) - 1:
                        animal.index = len(self.river) - 1
                    else:
                        animal.index = ind + 1
                else:
                    animal.index = ind
        for animal1 in self.river:
            if animal1 is not None:

                if new_list[animal1.index] is None:
                    new_list[animal1.index] = animal1
                else:
                    if animal1.check_sex(self.river[animal1.index]) is True:
                        if animal1.fight_or_reproduction(self.river
                                                         [animal1.index]):
                            if animal1.fight(self.river[animal1.index]):
                                self.river[animal1.index] = animal1
                        else:
                            new_list[animal1.index + 1] = animal1
                            if animal1.__class__.__name__ == "Bear":
                                children.append(Bear())
                            else:
                                children.append(Fish())
                    else:
                        if animal1.__class__.__name__ == "Bear":
                            self.river[animal1.index] = animal1
        for child in children:
            if None in new_list:
                num = new_list.index(None)
                new_list[num] = child
        self.river = new_list
        return self.river
