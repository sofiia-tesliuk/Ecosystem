from ecosystem import *


def main():
    n = int(input("Input length of river: "))
    i = int(input("Input count of iteration: "))
    eco = Ecosystem()
    c = eco.add_amimals(n)
    k = 0
    while k < i:
        eco.move()
        k += 1
        print("This is a river after {} years".format(k))
        print(eco.river)


main()
