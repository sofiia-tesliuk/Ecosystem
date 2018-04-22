import random


class Animal:
    Type = None

    def __init__(self):
        pass


class Bear(Animal):
    pass


class Fish(Animal):
    pass

class Otter(Animal):
    pass


class Ecosystem:

    def animals(self):
        num = 15
        river = []
        for i in range(num):
            age_fish = random.randint(0, 5)
            age_otter = random.randint(0, 12)
            age_bear = random.randint(0, 10)
            info = lambda age_animal: {'sex': random.choice([True, False]), 'age': age_animal, 'power': round(random.uniform(1, 5), 2)}
            item = random.choice([Bear(), Fish(), Otter(), None])
            if isinstance(item, Bear):
                animal = {item: info(age_bear)}
            elif isinstance(item, Fish):
                animal = {item: info(age_fish)}
            elif isinstance(item, Otter):
                animal = {item: info(age_otter)}
            else:
                animal = None
            river.append(animal)
        return river

    # def moving_animals(self, river):
    #     while None in river:
    #         num = len(river) - 1
    #         while True : #choos random animal, переобирає якшо None
    #             index = random.randint(0, num)-1
    #             animal = river[index]
    #             if animal is not None:
    #                 break
    #
    #         next_step = random.randint(0, num)-1
    #         opponent = river[next_step]
    #
    #         if opponent is None: #якщо тварина просто міняє позицію на посту
    #             river[index], river[next_step] = None, animal
    #         elif isinstance(animal, Bear): #Якщо тварина це ведідь і будь-яка інша тварина.
    #             if isinstance(opponent, Bear): #якщо два ведмеді
    #                 if animal['sex'] == opponent['sex'] :#якщо два самці
    #                     if animal['power'] > opponent['power']: #viner is animal
    #                         river[index], river[next_step] = None, animal
    #                     elif animal['power'] < opponent['power']:
    #                         river[index], river[next_step] = None, opponent #viner is opponent
    #                     else:
    #                         if animal['age'] < opponent['age']:
    #                             river[index], river[next_step] = None, animal
    #                         else:
    #                             river[index], river[next_step] = None, opponent
    #                 else:
    #
    #
    #
    #
    #
    #             river, river[next_step] = None, animal
    #         elif isinstance(animal, Otter):
    #             pass
    #         elif isinstance(animal, Fish):
    #             pass





