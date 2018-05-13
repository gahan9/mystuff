class BobTheBear(object):
    def __init__(self, salmons, salmon_len_, salmon_time_):
        self.salmons = salmons
        self.salmon_size = salmon_len_
        self.salmon_time = salmon_time_
        self.salmon_map = list(zip(self.salmon_size, self.salmon_time))

    @staticmethod
    def get_end_points(zipped_lis):
        possible_endpoints = set()
        for i in zipped_lis:
            possible_endpoints.add(i[0])
            possible_endpoints.add(sum(i))
        return possible_endpoints

    def generate_dict(self, zipped_lis):
        dict_ = {}
        possible_endpoints = self.get_end_points(zipped_lis)
        for i in possible_endpoints:
            for j in zipped_lis:
                if i in range(j[0], sum(j) + 1):
                    dict_[i] = dict_.setdefault(i, 0) + 1
        # return mapped dict values
        d = list(map(lambda x: (x, dict_[x]), dict_))
        return d

    def get_max_salmons(self):
        total_salmon = 0
        first_max = max(self.generate_dict(self.salmon_map), key=lambda x: x[1])
        total_salmon += first_max[1]
        remaining_salmon = [i for i in self.salmon_map if first_max[0] not in range(i[0], sum(i) + 1)]
        if remaining_salmon:
            second_max = max(self.generate_dict(remaining_salmon), key=lambda x: x[1])
            total_salmon += second_max[1]
        # print(first_max, second_max)
        return total_salmon


if __name__ == "__main__":
    salmons_ = int(input())
    salmon_len = list(map(int, input().split()))
    salmon_time = list(map(int, input().split()))
    # salmons_ = int('5')
    # salmon_len = list(map(int, '2 4 4 2 4'.split()))
    # salmon_time = list(map(int, '1 4 1 6 4'.split()))
    b = BobTheBear(salmons_, salmon_len, salmon_time)
    print(b.get_max_salmons())
