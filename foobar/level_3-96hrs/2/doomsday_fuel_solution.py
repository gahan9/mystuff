def answer(m):
    matrix = m
    matrix_length = len(matrix)
    for i,elem in enumerate(matrix):
        elem[i] = 0
    sums = [sum(i) for i in matrix]
    terminals = [i for i,item in enumerate(sums) if item==0]
    non_terminals = list((set(range(matrix_length)) - set(terminals)))
    total_non_terminals = len(non_terminals)
    print("sum: {}\t terminals: {}\t non_terminals: {}\t ".format(sums, terminals, non_terminals))

    for i in range(0, total_non_terminals-1):
        next_state = non_terminals[total_non_terminals-i-1]
        for j in range(0,total_non_terminals-1):
            start_state = non_terminals[j]
            matrix[start_state] = fuse(matrix[start_state], start_state, matrix[next_state], next_state)
    output = []
    for i in terminals:
        output.append(matrix[0][i])
    tot=sum(output)
    output.append(tot)
    if tot == 0:
        output = [1 for i in terminals]
        output.append(len(terminals))
    return output


def fuse(start_row, start, v2, end_row):
    lenV = len(start_row)
    indices = (set(range(lenV))-{start, end_row})
    sum2 = sum(v2)
    out = [0 for i in start_row]
    for i in indices:
        out[i] = sum2 * start_row[i] + start_row[end_row] * v2[i]
    gc = gcd_list(out)
    output = [int(i / gc) for i in out]
    return output


def gcd (a,b):
    if (b == 0):
        return a
    else:
        return gcd (b, a % b)

def gcd_list(lst):
    L=len(lst)
    out=0
    for i in range(0,L):
        out=gcd(out,lst[i])
    return out

# test cases below
# print(answer([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
# print(answer([[0, 1, 2, 1], [4, 0, 7, 1], [9, 2, 0, 1], [0, 0, 0, 0]]))
# print(answer([[0, 7, 0, 5], [2, 0, 3, 0], [2, 5, 0, 0], [0, 0, 0, 0]]))
print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer([[0, 3, 1, 0, 0, 0], [0, 0, 0, 7, 0, 0], [0, 0, 0, 2, 0, 1], [0, 0, 0, 0, 5, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer([[0, 3, 2, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 7, 0, 0], [0, 0, 5, 0, 4, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer([[0, 3, 2, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 7, 0, 0], [0, 0, 0, 0, 4, 5], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 2, 3, 2, 1], [9, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
