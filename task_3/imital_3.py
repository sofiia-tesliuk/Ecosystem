from task_1.ecosystem import Ecosystem


def main():
    """
    Main program to start simulation of ecosystem
    """
    try:
        river_length = int(input("Enter river length in ecosystem: "))
        number_of_iterations = int(input("Enter number of iterations: "))
        assert (river_length > 0) and (number_of_iterations > 0), None
        ecosystem = Ecosystem(river_length)
        ecosystem.simulation(number_of_iterations)
    except (ValueError, TypeError, AssertionError):
        print('Values should be positive integers.\n')
        main()
    except AssertionError:
        main()


if __name__ == "__main__":
    main()


