from collections import Counter
import itertools
import numpy


class Problem(object):
    def __init__(self, *args, **kwargs):
        pass


def main(matrix, *args):
    congress_coordinates, congress_x, congress_y, bjp_coordinates, bjp_x, bjp_y = args
    cntr = Counter(congress_x)
    null_max = 0
    mapper = {}
    for key, val in cntr.items():
        if key not in bjp_coordinates:
            null_max = val
            mapper[0] = mapper.get(0, [])
            mapper[0].append(val)
    return mapper, null_max
    """
    # linear... size 0
    x = matrix
    mapper = {}
    count = 0
    for i in x:
        if sum(i) is not 0:
            if 2 not in i:
                ones = numpy.where(i == 1)
                twos = numpy.where(i == 2)
                if ones[0].size > 1:
                    print(ones[0])
                    if twos[0].size > 0:
                        index_set = [a for a in itertools.combinations(ones[0].tolist(), 2) if len(set(twos).intersection(set(a))) is 0]
                    else:
                        index_set = list(itertools.combinations(ones[0].tolist(), 2))
                    for ii in index_set:
                        lis = list(map(lambda q: (count, q), ii))
                        print(lis)
                        mapper[len(lis)] = mapper.get(len(lis), [])
                        mapper[len(lis)].append(lis)
                elif ones[0].size == 1:
                    print(ones[0])
        count += 1
    return max(mapper.keys())
    """


if __name__ == "__main__":
    constituencies = int(input().strip())
    mapping_matrix = numpy.zeros(shape=[10, 10])
    congress_coordinates = []
    congress_x, congress_y = [], []
    bjp_coordinates = []
    bjp_x, bjp_y = [], []
    for i in range(constituencies):
        x, y, winner = input().strip().split()
        x, y = map(int, (x, y))
        if winner == "C":
            mapping_matrix[x][y] = 1
            congress_coordinates.append((x, y))
            congress_x.append(x)
            congress_y.append(y)
        else:
            mapping_matrix[x][y] = 2
            bjp_coordinates.append((x, y))
            bjp_x.append(x)
            bjp_y.append(y)
    res, null_mx = main(mapping_matrix, congress_coordinates, congress_x, congress_y, bjp_coordinates, bjp_x, bjp_y)
    # print(mapping_matrix.tolist())
    # print(max(main(mapping_matrix), main(mapping_matrix.transpose())))
    print(null_mx)
    print(0)
