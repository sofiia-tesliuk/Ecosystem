import random
from task_3 import animals


class Ecosystem:

    def animals(self):
        num = 15
        river = []
        for i in range(num):
            age_fish = random.randint(0, 5)
            age_otter = random.randint(0, 12)
            age_bear = random.randint(0, 10)
            info = lambda age_animal: {'sex': random.choice([True, False]), 'age': age_animal, 'power': round(random.uniform(1, 5), 2)}
            item = random.choice([animals.Bear(), animals.Fish(), animals.Otter(), None])
            if isinstance(item, animals.Bear):
                animal = {item: info(age_bear)}
            elif isinstance(item, animals.Fish):
                animal = {item: info(age_fish)}
            elif isinstance(item, animals.Otter):
                animal = {item: info(age_otter)}
            else:
                animal = None
            river.append(animal)
        return river

    # def moving_animals(self, river):
    #     while None in river:
    #         num = len(river) - 1
    #         while True :
    #             index = random.randint(0, num)-1
    #             animal = river[index]
    #             if animal is not None:
    #                 break
    #
    #         next_step = random.randint(0, num)-1
    #         opponent = river[next_step]
    #
    #         if opponent is None:
    #             river[index], river[next_step] = None, animal
    #         elif isinstance(animal, Bear): 
    #             if isinstance(opponent, Bear): 
    #                 if animal['sex'] == opponent['sex'] :
    #                     if animal['power'] > opponent['power']: 
    #                         river[index], river[next_step] = None, animal
    #                     elif animal['power'] < opponent['power']:
    #                         river[index], river[next_step] = None, opponent 
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





