from fractions import Fraction

loop_probability = lambda x : Fraction(1, 1-x)


def calculate_probability_of_node(matrix, terminals):
    count =0
    next_stage_probability={}
    for row in matrix:
        count2=0
        current_row_denominator = sum(row)
        for element in row:
            if element != 0:
                if count in next_stage_probability:
                    next_stage_probability[count].update({count2: Fraction(element, current_row_denominator)})
                else:
                    next_stage_probability[count] = ({count2: Fraction(element, current_row_denominator)})
            count2 +=1
        count+=1
    return next_stage_probability


def find_all_paths(next_stage_probability, start, end, path=[]):
    print("###########################")
    path = path + [start]
    print(path)
    if start == end:
        return [path]
    if not next_stage_probability.__contains__(start):
        return []
    paths = []
    for node in next_stage_probability[start]:
        if node not in path:
            newpaths = find_all_paths(next_stage_probability, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def answer(m):
    print("-"*50)
    from pprint import pprint
    print("matrix is:")
    pprint(m)
    terminals = []
    for rows in range(len(m)):
        if sum(m[rows]) == 0:
            terminals.append(rows)

    next_nodes = calculate_probability_of_node(m, terminals)
    print(next_nodes)
    _final = main(matrix=m, terminals=terminals, _next=next_nodes)


def main(matrix, terminals, _next, probability_set={}, elements_travelled=[], last_probability=1):
    for row in range(len(matrix)):
        print("row: {}".format(row))
        current_path = []
        if not row in terminals:
            for value in matrix[row]:
                if value:
                    current_value_index = matrix[row].index(value)
                    current_value = value
                    current_path.append(value)
                    if value not in probability_set:
                        probability_set[value] = 1
                    if current_value < row:
                        print(Fraction(value, sum(matrix[row])))
                        # print(loop_probability(Fraction() * Fraction(value, sum(matrix[row]))))
                        probability_set[value] = probability_set[value] * loop_probability(Fraction() * Fraction(value, sum(matrix[row])))
                        print(last_probability)
                        print("loop at: {} and {}".format(row, matrix[row].index(value)))
                    elif matrix[row].index(value) > row:
                        last_probability = last_probability * Fraction(value, sum(matrix[row]))
                        # print(Fraction(value, sum(matrix[row])))
                        print(last_probability)




    # final_state_probability = []
    # for terminal in terminal_probability:
    #     current_denominator = terminal_probability[terminal].denominator
    #     if not  current_denominator == max_denominator:
    #         multiplier = max_denominator / current_denominator
    #         # print(multiplier)
    #     else:
    #         multiplier = 1
    #     final_state_probability.append(int(terminal_probability[terminal].numerator * multiplier))
    #     # print("terminal {} : {} --> {}".format(terminal, stage_probability[terminal], int(terminal.numerator * multiplier)))
    # final_state_probability.append(max_denominator)
    # return final_state_probability


# test cases below
# print(answer([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
# print(answer([[0, 1, 2, 1], [4, 0, 7, 1], [9, 2, 0, 1], [0, 0, 0, 0]]))
# print(answer([[0, 7, 0, 5], [2, 0, 3, 0], [2, 5, 0, 0], [0, 0, 0, 0]]))
print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer([[0, 3, 1, 0, 0, 0], [0, 0, 0, 7, 0, 0], [0, 0, 0, 2, 0, 1], [0, 0, 0, 0, 5, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer([[0, 3, 2, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 7, 0, 0], [0, 0, 5, 0, 4, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer([[0, 3, 2, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 7, 0, 0], [0, 0, 0, 0, 4, 5], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 2, 3, 2, 1], [9, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
