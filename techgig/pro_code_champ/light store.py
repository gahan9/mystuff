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


def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


# end of function lcs


def main():
    x = input().strip()
    try:
        y = input().strip()
    except Exception as e:
        y = ""
    x_len = len(x)
    y_len = len(y)
    common = lcs(x, y)
    print(common)
    return abs(max(x_len, y_len) - common)


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