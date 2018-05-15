class BobTheBear(object):
    def __init__(self, salmons, salmon_len_, salmon_time_):
        self.salmons = salmons
        self.salmon_size = salmon_len_
        self.salmon_time = salmon_time_
        self.salmon_map = list(zip(self.salmon_time, self.salmon_size))
        self.salmon_endpoints = [sum(i) for i in self.salmon_map]

    @staticmethod
    def get_end_points(zipped_lis):
        possible_endpoints = set()
        for i in zipped_lis:
            possible_endpoints.add(i[0])
            possible_endpoints.add(sum(i))
        return possible_endpoints

    def generate_dict(self, zipped_lis):
        dict_ = {}
        # possible_endpoints = self.get_end_points(zipped_lis)
        possible_endpoints = range(min(self.salmon_endpoints), max(self.salmon_endpoints) + 1)
        for i in possible_endpoints:
            for j in zipped_lis:
                if i in range(j[0], sum(j) + 1):
                    dict_[i] = dict_.setdefault(i, 0) + 1
        # return mapped dict values
        return list(map(lambda x: (x, dict_[x]), dict_))

    def get_max_salmons(self):
        total_salmon = 0
        max_points = self.generate_dict(self.salmon_map)
        first_max = max(max_points, key=lambda x: x[1])
        total_salmon += first_max[1]
        possible_first_max = [i for i in max_points if i[1] == first_max[1]]
        salmons_max = []
        for first_maxima in possible_first_max:
            temp_sum = first_maxima[1]
            remaining_salmon = [i for i in self.salmon_map if first_maxima[0] not in range(i[0], sum(i) + 1)]
            if remaining_salmon:
                second_max = max(self.generate_dict(remaining_salmon), key=lambda x: x[1])
                temp_sum += second_max[1]
            salmons_max.append(temp_sum)
        return max(salmons_max)


if __name__ == "__main__":
    salmons_ = int(input())
    salmon_size = list(map(int, input().split()))
    salmon_time = list(map(int, input().split()))
    # salmons_ = int('5')
    # salmon_size = list(map(int, '2 4 4 2 4'.split()))
    # salmon_time = list(map(int, '1 4 1 6 4'.split()))
    b = BobTheBear(salmons_, salmon_size, salmon_time)
    print(b.get_max_salmons())
    """
13
1 1 1 1 1 1 1 1 1 2 4 5 9
3 5 5 6 7 7 9 9 9 6 2 4 1
    """
