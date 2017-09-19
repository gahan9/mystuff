from fractions import Fraction
import collections

loop_probability = lambda x : Fraction(1, 1-x)

def calculate_loop_states(sources, next_stage_probability, loop_states=[], calculated_loop_states=[]):
    # [v for v,k in next_stage_probability.items() if source in k and v in next_stage_probability[source]]
    record = calculated_loop_states
    loop_list = {}
    for source in sources:
        if not source in record:
            record.append(source)
            if source in loop_list:
                loop_list[source].update([v for v,k in next_stage_probability.items() if source in k and v in next_stage_probability[source]])
            else:
                loop_list[source] = [v for v,k in next_stage_probability.items() if source in k and v in next_stage_probability[source]]
    if not loop_list or source not in loop_list:
        # print("> ", loop_states, record)
        return loop_states
    else:
        loop_states.append(loop_list)
        return calculate_loop_states(loop_list[source], next_stage_probability, loop_states, record)


def calculate_probability_of_node(matrix, terminals):
    d={}
    count =0
    next_stage_probability={}
    for row in matrix:
        count2=0
        if count in terminals:
            d[count] = []
        current_row_denominator = sum(row)
        d[count] = []
        for element in row:
            if element != 0:
                if count in next_stage_probability:
                    next_stage_probability[count].update({count2: Fraction(element, current_row_denominator)})
                else:
                    next_stage_probability[count] = ({count2: Fraction(element, current_row_denominator)})
                d[count].append(count2)
            count2 +=1
        count+=1
    return next_stage_probability, d


def find_all_paths(next_stage_probability, start, end, path=[]):
    path = path + [start]
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
    # print("***********************")
    # from pprint import pprint
    # print("matrix is:")
    # pprint(m)
    # global paths
    paths = []
    terminals = []
    stage_probability = {}
    for rows in range(len(m)):
        if sum(m[rows]) == 0:
            terminals.append(rows)
            stage_probability[rows] = 0

    next_stage_probability, d = calculate_probability_of_node(m, terminals)
    # print("next_stage_probability: {}".format(next_stage_probability))

    paths_to_terminal = {}
    for terminal in terminals:
        paths_to_terminal[terminal] = find_all_paths(next_stage_probability=next_stage_probability, start=0, end=terminal)
    # print("paths_to_terminal: {}".format(paths_to_terminal))

    # this is important stage where next_stage_probability is your tree and you need to calculate probability to reach to states in terminals which are values 0 rows in matrix
    terminal_probability = {}
    for terminal_state in paths_to_terminal:
        if paths_to_terminal[terminal_state]:
            probability_for_this_terminal = 0
            considered_loop = []
            for path in paths_to_terminal[terminal_state]:
                this_path_probability = 1
                for x in range(len(path)-1):
                    source, destination = path[x], path[x+1]
                    current_to_next = next_stage_probability[source][destination]
                    #################################################
                    # I need this valie of loop_list to be accurate #
                    #################################################
                    # loop_list = [v for v,k in next_stage_probability.items() if source in k and v in next_stage_probability[source]]
                    loop_list = calculate_loop_states([source], next_stage_probability)
                    this_path_probability = this_path_probability * current_to_next
                    # loop_list = set(loop_list) - {source}
                    # print(">> ",path, (source, destination),loop_list, this_path_probability)
                    if loop_list:
                        for loop_state in loop_list:
                            # print((source, loop_state))
                            for key_state in loop_state:
                                for next_state in loop_state[key_state]:
                                    if not considered_loop.__contains__((key_state, next_state)) and not considered_loop.__contains__((next_state, key_state)):
                                        # loop_val = next_stage_probability[source][loop_state] * next_stage_probability[loop_state][source]
                                        if key_state in next_stage_probability and next_state in next_stage_probability:
                                            if next_state in next_stage_probability[key_state] and key_state in next_stage_probability[next_state]:
                                                loop_val = next_stage_probability[key_state][next_state] * next_stage_probability[next_state][key_state]
                                                this_path_probability = this_path_probability * loop_probability(loop_val)
                                                considered_loop.append((key_state, next_state))
                    # print(this_path_probability)
                probability_for_this_terminal = probability_for_this_terminal + this_path_probability
                terminal_probability[terminal_state] = probability_for_this_terminal
        else:
            terminal_probability[terminal_state] = Fraction(0)
    # print(terminal_probability)
    max_denominator = max([v.denominator for k,v in terminal_probability.items()])

    final_state_probability = []
    for terminal in terminal_probability:
        current_denominator = terminal_probability[terminal].denominator
        if not  current_denominator == max_denominator:
            multiplier = max_denominator / current_denominator
            # print(multiplier)
        else:
            multiplier = 1
        final_state_probability.append(int(terminal_probability[terminal].numerator * multiplier))
        # print("terminal {} : {} --> {}".format(terminal, stage_probability[terminal], int(terminal.numerator * multiplier)))
    final_state_probability.append(max_denominator)
    return final_state_probability


# test cases below
# print(answer([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(answer([[0, 7, 0, 5], [2, 0, 3, 0], [0, 6, 0, 0], [0, 0, 0, 0]]))
print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(answer([[0, 3, 1, 0, 0, 0], [0, 0, 0, 7, 0, 0], [0, 0, 0, 2, 0, 1], [0, 0, 0, 0, 5, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(answer([[0, 3, 2, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 7, 0, 0], [0, 0, 5, 0, 4, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(answer([[0, 3, 2, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 7, 0, 0], [0, 0, 0, 0, 4, 5], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 2, 3, 2, 1], [9, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
