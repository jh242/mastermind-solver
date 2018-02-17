from scripts import gensollist

all_solutions = []
still_possible = []

def init():
    global still_possible
    global all_solutions

    for i in range(1296):
        still_possible.append(True)

    all_solutions = gensollist.generate()

def eliminate_whites(tried_solution, whites):
    for solution in all_solutions:
        matches = 0
        if still_possible[all_solutions.index(solution)]:
            for tried_color in range(4):
                for solution_color in range(4):
                    if tried_solution[tried_color] == solution[solution_color] and tried_color == solution_color:
                        tried_solution[tried_color] = -1
                        solution[solution_color] = -2
                    elif tried_solution[tried_color] == solution[solution_color] and tried_color != solution_color:
                        matches += 1
                        tried_solution[tried_color] = -1
                        solution[solution_color] = -2
            if matches != whites:
                still_possible[all_solutions.index(solution)] = False

def eliminate_blacks(tried_solution, blacks):
    for solution in all_solutions:
        matches = 0
        if still_possible[all_solutions.index(solution)]:
            for color in range(4):
                if tried_solution[color] == solution[color]:
                    matches += 1
            if matches != blacks:
                still_possible[all_solutions.index(solution)] = False

def eliminate_last(tried_solution):
    still_possible[all_solutions.index(tried_solution)] = False

def eliminate_all(tried_solution):
    for solution in all_solutions:
        for tried_color in range(4):
            for solution_color in range(4):
                if tried_solution[tried_color] == solution[solution_color]:
                    still_possible[all_solutions.index(tried_solution)]

def grand_slam(tried_solution, blacks, whites):
    eliminate_last(tried_solution)
    if whites == 0 and blacks == 0:
        eliminate_all(tried_solution)
    elif whites == 0:
        eliminate_blacks(tried_solution, blacks)
    elif blacks == 0:
        eliminate_whites(tried_solution, whites)
