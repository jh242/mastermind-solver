from scripts import gensollist

all_solutions = []
still_possible = []


def init():
    global still_possible
    global all_solutions

    for i in range(1296):
        still_possible.append(0)

    all_solutions = gensollist.generate()


def eliminate_whites(tried_solution, whites):
    tried_solution_copy = tried_solution[:]
    for solution in all_solutions:
        matches = 0
        solution_copy = solution[:]
        if still_possible[all_solutions.index(solution_copy)]:
            for tried_color in range(4):
                for solution_color in range(4):
                    if tried_solution_copy[tried_color] == solution_copy[solution_color] and tried_color == solution_color:
                        tried_solution_copy[tried_color] = -1
                        solution_copy[solution_color] = -2
                    elif tried_solution_copy[tried_color] == solution_copy[solution_color] and tried_color != solution_color:
                        matches += 1
                        tried_solution_copy[tried_color] = -1
                        solution_copy[solution_color] = -2
            if matches != whites:
                still_possible[all_solutions.index(solution)] = 1


def eliminate_blacks(tried_solution, blacks):
    tried_solution_copy = tried_solution[:]
    for solution in all_solutions:
        solution_copy = solution[:]
        matches = 0
        if still_possible[all_solutions.index(solution_copy)]:
            for color in range(4):
                if tried_solution_copy[color] == solution_copy[color]:
                    matches += 1
            if matches != blacks:
                still_possible[all_solutions.index(solution)] = 1


def eliminate_last(tried_solution):
    still_possible[all_solutions.index(tried_solution)] = 1


def eliminate_all(tried_solution):
    for solution in all_solutions:
        for tried_color in range(4):
            for solution_color in range(4):
                if tried_solution[tried_color] == solution[solution_color]:
                    still_possible[all_solutions.index(solution)] = 1


def grand_slam(tried_solution, blacks, whites):
    eliminate_last(tried_solution)
    if whites == 0 and blacks == 0:
        eliminate_all(tried_solution)
    else:
        eliminate_blacks(tried_solution, blacks)
        eliminate_whites(tried_solution, whites)
