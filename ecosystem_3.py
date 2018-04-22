import random
import animals


class River:
    """ The river's initialization. """
    length_river = int(input("Enter river length in ecosystem: "))


    def r_river(self):
        river = []
        for i in range(self.length_river):
            item = random.choice([animals.Bear(), animals.Fish(), animals.Otter(), None])
            info = lambda Type: {'gender': Type().gender, 'age': Type().age, 'power': Type().power}
            if isinstance(item, animals.Bear):
                animal = {item: info(animals.Bear)}
            elif isinstance(item, animals.Fish):
                animal = {item: info(animals.Fish)}
            elif isinstance(item, animals.Otter):
                animal = {item: info(animals.Otter)}
            else:
                animal = None
            river.append(animal)
        print(river)
        return river


class Ecosystem(River):
    """ The ecosystem's internalization. """
    def __init__(self):
        number = int(input("Enter number of iterations: "))
        self.river = River().r_river()
        for i in range(number):
            while True:
                index = random.randint(0, self.length_river) - 1
                animal = self.river[index]
                if animal is not None:
                    break

            next_step = random.randint(0, self.length_river) - 1
            opponent = self.river[next_step]
            Ecosystem().move_bear(animal, opponent, index, next_step)
            Ecosystem().move_fish(animal, opponent, index, next_step)
            Ecosystem().move_otter(animal, opponent, index, next_step)

    def birth_baby(self, number, item):
        """ Creating a new animal. """
        for i in range(number):
            item.age = 1
            item.gender = random.choice(['M', 'F'])
            item.power = round(random.uniform(1, 5), 2)

    def battle_same(self, animal, opponent, index, next_step):
        """ The battle of animals of one species. """
        if animal.power > opponent.power:
            self.river[index], self.river[next_step] = None, animal
        elif animal.power < opponent.power:
            self.river[index], self.river[next_step] = None, opponent
        else:
            if animal.age < opponent.age:
                self.river[index], self.river[next_step] = None, animal
            else:
                self.river[index], self.river[next_step] = None, opponent

    def move_bear(self, animal, opponent, index, next_step):
        """ Bear step. """
        if isinstance(animal, animals.Bear):
            if isinstance(opponent, animals.Bear):
                if animal.gender == opponent.gender:
                    animal.battle_same(animal, opponent, index, next_step)
                else:
                    item = animals.Bear()
                    try:
                        animal.birth_baby(2, item)
                        self.river[self.river.index(None)] = item
                    except ValueError:
                        pass
            else:
                self.river[index], self.river[next_step] = None, animal

    def move_otter(self, animal, opponent, index, next_step):
        """ Otter step. """
        if isinstance(animal, animals.Otter):
            if isinstance(opponent, animals.Otter):
                if animal.gender == opponent.gender:
                    animal.battle_same(animal, opponent, index, next_step)
                else:
                    item = animals.Otter()
                    try:
                        animal.birth_baby(3, item)
                        self.river[self.river.index(None)] = item
                    except ValueError:
                        pass
            elif isinstance(opponent, animals.Bear):
                self.river[index] = None
            else:
                self.river[index], self.river[next_step] = None, animal

    def move_fish(self, animal, opponent, index, next_step):
        """ Fish step. """
        if isinstance(opponent, animals.Fish):
            if animal.gender == opponent.gender:
                animal.battle_same()
            else:
                item = animals.Fish()
                try:
                    animal.birth_baby(7, item)
                    self.river[self.river.index(None)] = item
                except ValueError:
                    pass

        elif type(opponent) is None:
            self.river[index], self.river[next_step] = None, animal
        else:
            self.river[index] = None

e = Ecosystem()


