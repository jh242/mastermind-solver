def print_remaining(all_solutions, still_possible):
    for solution in all_solutions:
        if still_possible[all_solutions.index(solution)] == 0:
            print(solution)
