from scripts import elimsolutions
import random


def choose_solution():
    while True:
        solution_index = random.randint(0, 1295)
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
    print("Try ", tried_solution)
