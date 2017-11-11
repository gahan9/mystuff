def answer(m):
    matrix = m  # matrix passed to function
    matrix_length = len(matrix)  # get length of matrix
    for i, elem in enumerate(matrix):
        elem[i] = 0
    sums = [sum(i) for i in matrix]  # get sum of element in row of matrix
    terminals = [i for i, item in enumerate(sums) if item == 0]  # get terminals | end-point
    non_terminals = list((set(range(matrix_length)) - set(terminals)))  # non-end-point
    total_non_terminals = len(non_terminals)  # total nodes to travel
    print("sum: {}\t terminals: {}\t non_terminals: {}\t ".format(sums, terminals, non_terminals))

    for i in range(0, total_non_terminals - 1):
        next_state = non_terminals[total_non_terminals - i - 1]  # get next state to travel
        for j in range(0, total_non_terminals - 1):
            start_state = non_terminals[j]  # define start point for the selected path
            # now update value of element .. fuse the current matrix with updated values
            matrix[start_state] = fuse(matrix[start_state], start_state, matrix[next_state], next_state)
    # the matrix is now fused with new values
    # print(matrix)
    output = []
    for i in terminals:
        output.append(matrix[0][i])
    tot = sum(output)
    output.append(tot)
    if tot == 0:
        output = [1 for i in terminals]
        output.append(len(terminals))
    return output


def fuse(start_row, start, end_row, end):
    lenV = len(start_row)  # get elements in initial row of path
    indices = (set(range(lenV)) - {start, end})  # possible state/row to explore
    sum2 = sum(end_row)
    out = [0 for i in start_row]  # neutralize current state/row
    for i in indices:  # iterate for every possible state/row
        out[i] = sum2 * start_row[i] + start_row[end] * end_row[i]   # calculation: find probability to reach to the node
    gc = gcd_list(out)  # calculation: get gcd
    output = [int(i / gc) for i in out]
    return output


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd_list(lst):
    L = len(lst)
    out = 0
    for i in range(0, L):
        out = gcd(out, lst[i])
    return out


# test cases below
if __name__ == '__main__':
    # Program Starts here....
    problem_matrix = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    print(answer(problem_matrix))

# print(answer([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
# print(answer([[0, 1, 2, 1], [4, 0, 7, 1], [9, 2, 0, 1], [0, 0, 0, 0]]))
# print(answer([[0, 7, 0, 5], [2, 0, 3, 0], [2, 5, 0, 0], [0, 0, 0, 0]]))
# print(answer([[0, 3, 1, 0, 0, 0], [0, 0, 0, 7, 0, 0], [0, 0, 0, 2, 0, 1], [0, 0, 0, 0, 5, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer([[0, 3, 2, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 7, 0, 0], [0, 0, 5, 0, 4, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer([[0, 3, 2, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 7, 0, 0], [0, 0, 0, 0, 4, 5], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 2, 3, 2, 1], [9, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
