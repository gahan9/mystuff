"""
Attribute-Selection (100 Marks)
===============================

One of the tedious work in data analysis is handling multiple attributes of various types. Many of these attributes are not even relevant to the analysis task. So removing these attributes is necessary to make the analysis efficient.
Sachin is a famous Data-Analyst. Currently, he is working on a new algorithm for attribute selection.

The algorithm works in two phases-

### Phase-1-

In the first phase, S-value of every attribute is found out. S-value of an attribute is its relevance to the class. Higher the S-value is, lesser the attribute is relevant to the class. After that k most relevant attributes are selected and rest are removed.

### Phase-2-

In the second phase, all the redundant attributes among the selected relevant attributes are removed. To find the redundant attributes, A-value for every attribute is found out. If A-value of an attribute is odd then it is removed otherwise the attribute is accepted.
A-value of an attribute is the number of x s such that. `gcd(x,b)=1`, where `1<=a<=b` and b is the S-value of the attribute.

Now Sachin is wondering how many attributes would remain after deleting all the redundant attributes. So help Sachin to find it out.
Input Format
First line of input contains an Integer N denoting the size of Array.
Next line of input contain a elements of the array `(1 to 10^18)`.
Last line of input contains an Integer K.

Constraints

    (1<=N<=10^5)
    (1<=A[i]<=10^18)
    (1<=K<=N)


Output Format
You must return an integer- Number of selected attributes by the algorithm.
Sample TestCase 1
Input

    3
    1
    2
    3
    2

Output

    0

"""
import statistics


def get_relevant(arr, val):
    # arr: [1, 2, 3]
    var = statistics.stdev(arr)
    array = [(i, abs(i - var)) for i in arr]
    array = sorted(array, key=lambda x: x[1])
    return array[:val]


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def main():
    array_size = int(input().strip())
    elements = [int(input().strip()) for _ in range(array_size)]
    k = int(input().strip())
    relevant_data = get_relevant(elements, k)
    d_map = {}
    for attrib, s_value in relevant_data:
        a_value = 0
        for i in range(1, int(s_value)+1):
            if gcd(i, s_value) is 1:
                a_value += 1
        if a_value % 2 is 0 and a_value is not 0:
            d_map[attrib] = (s_value, a_value)
    return len(d_map)


if __name__ == "__main__":
    print(main())
