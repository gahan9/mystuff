"""
 The Light Store (100 Marks)
A light store owner has several bulb chains of different types which consist of bulbs of different colors in different order. In addition to that, he has large collection of bulbs of each colors. A bulb chain is identified by the color sequence of its bulbs. He wants to transform one type of bulb chain into another type of bulb chain by either by:

Adding a bulb at some location.
Removing a bulb from a location.
Replacing a bulb with another bulb of different colour.

Given two color sequences of two different bulb chains, Find the minimum no. of operations required to do this transformation. (Assume each color can be represented by a character and hence, color sequence of a bulb chain can be represented as sequence of characters or a string.)


Input Format
You need to read two line having two color sequences(A and B) from STDIN.

Constraints
1<= Length(A) <=100
1<= Length(B) <=100



Output Format
You need to print minimum no. of operations required to transform first bulb chain into the second(integer).

Sample TestCase 1
Input

asdfgh
sdfgh

Output

1


"""

from difflib import SequenceMatcher


def lcs(string1, string2):
    match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))

    # print(match)  # -> Match(a=0, b=15, size=9)
    # print(string1[match.a: match.a + match.size])  # -> apple pie
    # print(string2[match.b: match.b + match.size])
    return match


def over_lcs(X, Y, m, n):
    if m == 0 or n == 0:
       return 0
    elif X[m-1] == Y[n-1]:
       return 1 + over_lcs(X, Y, m-1, n-1)
    else:
       return max(over_lcs(X, Y, m, n-1), over_lcs(X, Y, m-1, n))


def main():
    x = input().strip()
    try:
        y = input().strip()
    except Exception as e:
        y = ""
    x_len, y_len = len(x), len(y)
    val = abs(max(x_len, y_len) - over_lcs(x, y, x_len, y_len))
    if x_len is y_len:
        operation_cost = 0
        match = lcs(x, y)
        operation_cost += max(match.b, match.a)
        x = x[match.a + match.size:]
        y = y[match.b + match.size:]
        return val + operation_cost + abs(len(x) - len(y))
    return val


if __name__ == "__main__":
    print(main())

"""
acbcbcbcbcdcbcbc
cbcbcbcbcbcbcbcb

acbcbcbcbcdcbcbc 
== > removal of a
cbcbcbcbcdcbcbc

cbcbcbcbcdcbcbc 
== > replace d
cbcbcbcbcbcbcbc

cbcbcbcbcbcbcbc
== > add b
cbcbcbcbcbcbcbcb

"""