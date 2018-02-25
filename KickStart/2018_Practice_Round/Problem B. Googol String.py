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
        self.string = ""

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
        c = 0
        while c < max_value:
            self.string = self.generate_string()
            c += 1
        return self.string


def string_generator(max_iter=6):
    result_string = "0"
    for i in range(1, max_iter):
        if i == 0:
            pass
        elif i == 1:
            result_string = "0"
        else:
            common_set = 2**(i-1)
            result_string += "0" + result_string[:common_set]


if __name__ == "__main__":
    googl = GoogolString()
    thr = Thread(target=googl.small_input_string, args=(40,))
    thr.start()
    # string = small_input_string()  # generated static small input string according to requirements
    t = int(input())
    for i in range(1, t + 1):
        lookup_index = int(input()) - 1
        result = googl.string[lookup_index]
        print("Case #{}: {}".format(i, result))
