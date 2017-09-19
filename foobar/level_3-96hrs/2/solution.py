from fractions import Fraction
from pprint import pprint
import collections

loop_probability = lambda x : Fraction(1, 1-x)

def find_paths_from(current_path, d):
    global paths
    future_nodes = d[current_path[-1]]
    if future_nodes:
        [find_paths_from(current_path + [node], d) for node in future_nodes if node not in current_path]
    else:
        paths.append(current_path)


def answer(m):
    pprint(m)
    global paths
    paths = []
    terminals = []
    stage_probability = {}
    for rows in range(len(m)):
        if sum(m[rows]) == 0:
            terminals.append(rows)
            stage_probability[rows] = 0
    d={}
    stage_probability = {}
    count =0
    next_stage_probability={}
    for row in m:
        count2=0
        if count in terminals:
            d[count] = []
            # if count2 in null_cols and count2 !=0:
            #     print(null_cols)
            # continue
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

    print(">>",next_stage_probability)

    find_paths_from([0], d)
    print(paths)
    paths_to_terminal = {}
    for path in paths:
        terminal_state = path[-1]
        stage_probability[terminal_state] = 1
        calculated_path = []
        for x in range(len(path)-1):
            source, destination = path[x], path[x+1]
            current_to_next = next_stage_probability[source][destination]
            # loop_list = [{s: v} for s in sl for v,k in next_stage_probability.items() if s in k] # [{0: 1}, {1: 0}]
            loop_list = [v for v,k in next_stage_probability.items() if source in k]
            stage_probability[path[-1]] = stage_probability[path[-1]] * current_to_next
            # print(stage_probability[path[-1]])
            loop_values = []
            if loop_list:
                for items in loop_list:
                    if items in next_stage_probability[source] and (source, items) not in calculated_path and (items, source) not in calculated_path :
                        loop_val = next_stage_probability[source][items] * next_stage_probability[items][source]
                        # print(">>",next_stage_probability[source][items], next_stage_probability[items][source], loop_val, loop_probability(loop_val))
                        stage_probability[path[-1]] = stage_probability[path[-1]] * loop_probability(loop_val)
                        calculated_path.append((source, items))
            # print(">Path:{} Source:{} Destination:{} \tloop_list: {} \tcurrent_probability: {}".format(path, source, destination, loop_list, stage_probability[path[-1]]))
        if not terminal_state in paths_to_terminal:
            paths_to_terminal[terminal_state] = stage_probability[terminal_state]
        else:
            paths_to_terminal[terminal_state] += stage_probability[terminal_state]

    # print("paths to terminal: {} \t stage_probability: {}".format(paths_to_terminal, stage_probability))
    stage_probability = paths_to_terminal
    # print("paths to terminal: {} \t stage_probability: {}".format(paths_to_terminal, stage_probability))
    for states in terminals:
        if states not in stage_probability:
            stage_probability[states] = Fraction(0)

    # stage_probability = dict(sorted(stage_probability.items(), key=operator.itemgetter(1), reverse=False))
    stage_probability = collections.OrderedDict(sorted(stage_probability.items()))
    print(stage_probability)
    max_denominator = max([v.denominator for k,v in stage_probability.items()])

    final_state_probability = []
    for terminal in stage_probability:
        current_denominator = stage_probability[terminal].denominator
        if not  current_denominator == max_denominator:
            multiplier = max_denominator / current_denominator
            # print(multiplier)
        else:
            multiplier = 1
        final_state_probability.append(int(stage_probability[terminal].numerator * multiplier))
        # print("terminal {} : {} --> {}".format(terminal, stage_probability[terminal], int(terminal.numerator * multiplier)))
    final_state_probability.append(max_denominator)
    return final_state_probability
# print(answer([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(answer([[0, 7, 0, 5], [2, 0, 3, 0], [0, 0, 0, 0], [0, 6, 0, 0], [0, 0, 0, 0]]))
print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer([[0, 3, 2, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 7, 0, 0], [0, 0, 5, 0, 4, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer([[0, 3, 2, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 7, 0, 0], [0, 0, 0, 0, 4, 5], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# 4 - 56/155 , 5 -
# print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 2, 3, 2, 1], [9, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
"""
{0: [(1, Fraction(1, 2)), (5, Fraction(1, 2))],
 1: [(0, Fraction(1, 3)),
     (2, Fraction(1, 6)),
     (3, Fraction(1, 4)),
     (4, Fraction(1, 6)),
     (5, Fraction(1, 12))],
 2: [(0, Fraction(9, 11)), (1, Fraction(1, 11)), (5, Fraction(1, 11))],
 3: [],
 4: [],
 5: []}
"""
# print(answer())
# print(answer())
