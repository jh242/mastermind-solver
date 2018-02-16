
#Generate a list of possible solutions

def generate():
    possible_solutions = []
    current_construction = []

    for first_slot_color in range(1,7):
        for second_slot_color in range(1,7):
            for third_slot_color in range(1,7):
                for fourth_slot_color in range(1,7):
                    current_construction.append(first_slot_color)
                    current_construction.append(second_slot_color)
                    current_construction.append(third_slot_color)
                    current_construction.append(fourth_slot_color)
                    possible_solutions.append(current_construction)
                    current_construction.clear()

    return possible_solutions
