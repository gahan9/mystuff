Counting Leafs (100 Marks)
==========================

You are given a tree with N nodes numbered from 0 to N-1 . You are also given a node X which you are supposed to delete. You have to tell the number of leaf nodes in the tree after deleting the given node. Note that deleting a node deletes all the nodes in its subtree.

![image](https://i.imgur.com/tMS7N5G.jpg)

In the input you are given an array A, where Ai is the parent of ith node. The node with parent -1 is the root of the tree. It is guaranteed that there is exactly one root of the tree.

Input Format
First line contains an integer N - the number of nodes in the tree.
Second line contains N integers representing the array A.
Third line contains an integer representing the node to delete.

Constraints
```python
1 <= N <= 100
-1 <= Ai <= (N-1)
0 <= X <= (N-1)
```
Output Format
Print a single integer representing the number of leafs in the tree after deleting the given node.

Sample TestCase 1
Input
```
5
-1 0 0 1 1
2
```
Output
```
2
```
Explanation

The corresponding tree is shown in the problem statement above. Initially, there are 3 leafs 2, 3 and 4 (marked in green color). If we delete the node 2, two leafs are left i.e 3 and 4. Hence, answer is 2.
Sample TestCase 2
Input
```
5
-1 0 0 1 1
1
```
Output
```
1
```
Explanation
After deleting node 1 the only leaf node left is 2.
![image](https://image.ibb.co/c7ZYg7/index.jpg)