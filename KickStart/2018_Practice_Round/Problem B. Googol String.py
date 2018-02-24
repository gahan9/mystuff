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


def switch(arg):
    return arg.replace("0", "2").replace("1", "0").replace("2", "1")


def generate_string(string):
    return "{}0{}".format(string, switch(string[::-1]))


def small_input_string(max_value=18):
    c = 0
    s = ""
    while c < max_value:
        s = generate_string(s)
        c += 1
    return s

if __name__ == "__main__":
    string = small_input_string()  # generated static small input string according to requirements
    t = int(input())
    for i in range(1, t+1):
        lookup_index = int(input()) - 1
        result = string[lookup_index]
        print("Case #{}: {}".format(i, result))
