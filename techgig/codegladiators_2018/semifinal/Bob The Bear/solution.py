class BobTheBear(object):
    def __init__(self, salmons, salmon_len_, salmon_time_):
        self.salmons = salmons
        self.salmon_size = salmon_len_
        self.salmon_time = salmon_time_
        self.salmon_map = list(map(lambda x, y: (x, x+y), self.salmon_time, self.salmon_size))
        self.salmon_endpoints = set(self.salmon_time + [i[1] for i in self.salmon_map])

    def generate_dict(self, zipped_lis):
        dict_ = {}
        for i in self.salmon_endpoints:
            for j in zipped_lis:
                if i in range(j[0], j[1] + 1):
                    dict_[i] = dict_.setdefault(i, 0) + 1
        # return mapped dict values
        return dict_
        # return list(map(lambda x: (x, dict_[x]), dict_))

    def get_max_salmons(self):
        salmons_count_on_endpoint = self.generate_dict(self.salmon_map)
        salmons_max = []
        for endpoint, salmon in salmons_count_on_endpoint.items():
            temp_sum = salmon
            remaining_salmon = self.generate_dict([i for i in self.salmon_map if endpoint not in range(i[0], i[1] + 1)])
            try:
                second_max = max(remaining_salmon, key=lambda x: remaining_salmon[x])
                temp_sum += remaining_salmon[second_max]
            except ValueError:
                pass
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
