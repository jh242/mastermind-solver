from scripts import elimsolutions
from random import randint
from tests import printremaining


def choose_solution():
    while True:
        solution_index = randint(0, 1295)
        if elimsolutions.still_possible[solution_index] == 0:
            return elimsolutions.all_solutions[solution_index]


elimsolutions.init()
tried_solution = choose_solution()
print("Try ", tried_solution)

while True:
    whites = int(input("Whites (Input 9 to exit): "))
    if whites == 9:
        break
    blacks = int(input("Blacks: "))
    elimsolutions.grand_slam(tried_solution, blacks, whites)
    tried_solution = choose_solution()
    # printremaining.print_remaining(elimsolutions.all_solutions, elimsolutions.still_possible)
    if elimsolutions.still_possible.count(0) == 1:
        print("The answer is ", tried_solution)
        break
    else:
        print("Try", tried_solution)
