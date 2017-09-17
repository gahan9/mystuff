from fractions import Fraction
from pprint import pprint
# import numpy


loop_probability = lambda x : Fraction(1, 1-x)

paths = []
def find_paths_from(current_path, d, next_stage_probability):
    # current_path: [0]
    # next_stage_probability: {0: [(1, Fraction(1, 2)), (5, Fraction(1, 2))], 1: [(0, Fraction(4, 9)), (3, Fraction(1, 3)), (4, Fraction(2, 9))], 2: [], 3: [], 4: [], 5: []}
    # d: {0: [1, 5], 1: [0, 3, 4], 2: [], 3: [], 4: [], 5: []}
    global paths
    future_nodes = d[current_path[-1]]
    # print("future_nodes {}".format(future_nodes))
    if future_nodes:
        for node in future_nodes:
            if node not in current_path:
                [find_paths_from(current_path + [node], d, next_stage_probability)]
        # [find_paths_from(current_path + [node], d, next_stage_probability) for node in future_nodes if node not in current_path]
    else:
        paths.append(current_path)


def answer(m):
    pprint(m)
    terminals = []
    stage_probability = {}
    for rows in range(len(m)):
        if sum(m[rows]) == 0:
            terminals.append(rows)
            stage_probability[rows] = 0

    # a= numpy.array(m)
    # null_cols = numpy.where(~a.any(axis=0))[0]
    d={}
    stage_probability = {}
    next_stage_probability = {}
    count =0
    for row in m:
        count2=0
        if count in terminals:
            d[count] = []
            # if count2 in null_cols and count2 !=0:
            #     print(null_cols)
            # continue
        current_row_denominator = sum(row)
        next_stage_probability[count] = []
        d[count] = []
        for element in row:
            if element != 0:
                next_stage_probability[count].append((count2, Fraction(element, current_row_denominator)))
                d[count].append(count2)
            count2 +=1
        count+=1

    print(next_stage_probability)

    final_state_probability = []
    find_paths_from([0], d, next_stage_probability)
    for path in paths:
        stage_probability[path[-1]] = 1
        for x in range(len(path)-1):
            print(path[x], path[x+1])
            current_to_next = [y[1] for y in next_stage_probability[path[x]] if y[0] == path[x+1]][0]
            next_to_current = [y[1] for y in next_stage_probability[path[x+1]] if y[0] == path[x]]
            # print(next_to_current)
            if path[x] in d[path[x+1]] and path[x+1] in d[path[x]] and next_to_current:
                pass
                stage_probability[path[-1]] = stage_probability[path[-1]] * loop_probability(current_to_next * next_to_current[0])
            else:
                stage_probability[path[-1]] = stage_probability[path[-1]] * current_to_next

    for states in terminals:
        if states not in stage_probability:
            stage_probability[states] = Fraction(0)

    print(stage_probability)

# print(answer([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer())
# print(answer())
