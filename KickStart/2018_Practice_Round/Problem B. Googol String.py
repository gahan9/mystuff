"""https://code.google.com/codejam/contest/4374486/dashboard#s=p1
Problem B. Googol String

A "0/1 string" is a string in which every character is either 0 or 1. There are two operations that can be performed on a 0/1 string:

switch: Every 0 becomes 1 and every 1 becomes 0. For example, "100" becomes "011".
reverse: The string is reversed. For example, "100" becomes "001".
Consider this infinite sequence of 0/1 strings:

S0 = ""

S1 = "0"

S2 = "001"

S3 = "0010011"

S4 = "001001100011011"

...

SN = SN-1 + "0" + switch(reverse(SN-1)).

You need to figure out the Kth character of Sgoogol, where googol = 10100.
"""
from threading import Thread


class GoogolString(object):
    def __init__(self):
        # string-format: aXb0a(X')b
        self.string = ""
        self.result_string = "0"
        self.string_length = 2**60

    def switch(self, arg):
        return arg.replace("0", "2").replace("1", "0").replace("2", "1")

    def generate_string(self, string=None):
        if not string:
            string = self.string
        return "{}0{}".format(string, self.switch(string[::-1]))

    def demo_str(self, length=7):
        s = '0'
        for st in range(1, length):
            print("{:2} : {:^65}".format(st, s))
            s = self.generate_string(s)

    def small_input_string(self, max_value=7):
        # don't set max_value over 20 it will fu(|< your system
        c = 0
        while c < max_value:
            self.string = self.generate_string()
            c += 1
        return self.string

    def get_position(self, pos):
        """ approach alternative """
        # print("Line 1: {:5} - {:5}".format(pos, bin(pos)))
        if ('0' not in bin(pos)[2:]) or (pos == 0):
            # print("Line 2(if): If condition satisfied for: {:4} : {:5}".format(pos, bin(pos)))
            return 0
        # print("Line 3: expression data: x: {} \t bin(x): {} \t len(bin(x)): {}".format(pos, bin(pos), len(bin(pos))))
        y = 2 ** (len(bin(pos)) - 3) - 1
        # print("Line 4: evaluation [2 ** (len(bin(x)) - 3) - 1]: {}".format(y))
        # print("Line 5: Next arg: {}".format(y - (pos - y)))
        result = self.get_position(y - (pos - y)) ^ 1
        # print("Line 6: evaluation.. fn : {}".format(result))
        return result

    @staticmethod
    def swap(x):
        return '0' if x == '1' else '1'

    def string_generator(self, max_iter=6):
        # don't set max_value over 30 it will fu(|< your system
        for i in range(1, max_iter):
            common_set = 2 ** (i - 1)
            self.result_string += "0" + self.result_string[:common_set - 1] \
                                  + self.swap(self.result_string[:common_set]) \
                                  + self.result_string[common_set:]
        return self.result_string


if __name__ == "__main__":
    googl = GoogolString()
    # thr = Thread(target=googl.small_input_string, args=(20,))
    # thr.start()
    # string = small_input_string()  # generated static small input string according to requirements
    t = int(input())
    for i in range(1, t + 1):
        lookup_index = int(input()) - 1
        print("Case #{}: {}".format(i, googl.get_position(lookup_index)))
