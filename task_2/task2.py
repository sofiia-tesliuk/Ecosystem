from task_2.ecosystem import *


def main():
    n = int(input("Input length of river: "))
    i = int(input("Input count of iteration: "))
    eco = Ecosystem()
    c = eco.add_animals(n)
    k = 0
    while k < i:
        string = ""
        eco.move()
        k += 1
        print("This is a river after {} years".format(k))
        for animal in eco.river:

                # string += animal.__class__.__name__()
                string += animal.__class__.__name__[0]

        print(string.replace('N', " "))


main()
