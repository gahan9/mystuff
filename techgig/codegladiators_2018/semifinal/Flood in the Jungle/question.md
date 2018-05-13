## Flood in the Jungle  (100 Marks)

A group of monkeys are living in Sunderbans forests. There are N trees in Sunderbans (numbered from 0 to N-1) on which these monkeys live. Every year floods hit the forest of Sunderbans. The monkeys have a tradition of meeting on a tree after the flood.

Last night Sunderbans has been hit hard by a sudden flood. The flood was very strong and it has submerged everything except the mighty trees on which the monkeys live.


 ![](https://www.techgig.com/files/nicUploads/56714001252294.jpg) ![](https://www.techgig.com/files/nicUploads/791330661186107.jpg)


All the monkeys now have to meet on some tree. Due to the flood the trees have become weak so jumping **from** them is dangerous. **Whenever a monkey jumps fro m a tree A to a tree B, the tree A gets submerged a little while the tree B remains unaffected.** The monkeys don't know how to swim. So, they move from one tree to another tree by jumping. Every tree has been assigned a 2D - coordinate value. A monkey can only jump between two trees if the euclidean distance between them is less than or equal to **C**. **C** is called the jumping capacity of the monkeys.


The trees have threshold values. The threshold value of the ith tree is given by ti. It means that no more than ti monkeys can jump off from the ith tree.
You are given the coordinates of the trees, their threshold values, the number of monkeys on the trees, and the jumping capacity of the monkeys. You have to tell the number of the trees on which the **all** monkeys can meet after the flood. The meeting can happen on a tree if all the monkeys can come to this tree.



##### Input Format

The first line of input contains 2 integers N and C, denoting the number of trees and the jumping capacity of the monkeys.

Following N lines contains xi yi mi ti  - the x-coordinate of the ith tree, the y-coordinate of the ith tree, the number of monkeys on the ith tree and the maximum number of monkeys that can jump off from the ith tree.

The last line of the input is kept blank.



##### Constraints

    1 <= N <= 200

    0 <= C <= 100, 000

    -100, 00 <= xi, yi <= 100, 00

    0 <= mi <= 15

    1 <= ti <= 200





##### Output Format

One line with space separated integers denoting the numbers of the trees on which the meeting can happen. These numbers should be in **ascending order** and should be from 0 to N-1. If there is no tree on which the meeting can happen then print -1.




##### Sample TestCase 1

###### Input

    3 100.0
    1 10 5 5
    5 10 5 1
    8 10 5 4

###### Output

    -1

###### Explanation

There are 5 monkeys on the 1st tree (0-based indexing) while only 1 can jump off this tree. Similarly, there are 5 monkeys on the 2nd tree but only 4 can jump off. So, there is no tree where all the monkeys from the 1st tree and 2nd tree can meet. Hence, answer is -1.



Note that trees are numbered from 0 to 2.

##### Sample TestCase 2

###### Input

    3 100.0
    1 10 5 20
    5 10 5 20
    8 10 5 20

###### Output

    0 1 2

###### Explanation

The meeting can happen on all the trees.



