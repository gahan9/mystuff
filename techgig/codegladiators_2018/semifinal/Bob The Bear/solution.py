class BobTheBear(object):
    def __init__(self, salmons, salmon_len_, salmon_time_):
        self.salmons = salmons
        self.salmon_size = salmon_len_
        self.salmon_time = salmon_time_
        self.salmon_map = list(map(lambda x, y: (x, x+y), self.salmon_time, self.salmon_size))
        self.salmon_endpoints = set(self.salmon_time + [i[1] for i in self.salmon_map])

    def generate_result(self):
        salmon_count = 0
        for i in self.salmon_endpoints:
            for j in self.salmon_endpoints:
                if i is not j:
                    temp_sum = 0
                    for k in self.salmon_map:
                        range_ = range(k[0], k[1] + 1)
                        if i in range_ or j in range_:
                            temp_sum += 1
                    salmon_count = temp_sum if temp_sum > salmon_count else salmon_count
        return salmon_count


if __name__ == "__main__":
    salmons_ = int(input())
    salmon_size = list(map(int, input().split()))
    salmon_time = list(map(int, input().split()))
    # salmons_ = int('5')
    # salmon_size = list(map(int, '2 4 4 2 4'.split()))
    # salmon_time = list(map(int, '1 4 1 6 4'.split()))
    b = BobTheBear(salmons_, salmon_size, salmon_time)
    print(b.generate_result())
    """
13
1 1 1 1 1 1 1 1 1 2 4 5 9
3 5 5 6 7 7 9 9 9 6 2 4 1
    """
