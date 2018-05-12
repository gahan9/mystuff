import sys


class BobTheBear(object):
    def __init__(self, salmons, salmon_len_, salmon_time_):
        self.salmons = salmons
        self.salmon_size = salmon_len_
        self.salmon_time = salmon_time_
        self.salmon_map = self.map_salmon()

    def map_salmon(self):
        return zip(self.salmon_size, self.salmon_time)

    def map_all(self):
        l = list((i, j) for i, j in self.salmon_map)
        return l


if __name__ == "__main__":
    # sal_ = int(input())
    # len_ = map(int, input().split())
    # time_ = map(int, input().split())
    sal_ = int('5')
    salmon_len = map(int, '2 4 4 2 4'.split())
    salmon_time = map(int, '1 4 1 6 4'.split())
    b = BobTheBear(sal_, salmon_len, salmon_time)
    print(b.map_all())
