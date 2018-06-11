Karnataka Elections (100 Marks)

In the recent Karnataka Assembly elections, BJP and Congress have emerged as the two largest parties. BJP fell short of few seats, and could not make government in spite of having overwhelming public support. This is the beauty of politics, where winners may become losers and losers may become winners.

The Think-Tank of BJP has gathered in New Delhi to discuss the possible causes of their failure. For the brain-storming a large map of Karnataka has been brought which contains details of the various constituencies and the winning party for those constituencies. The map contains only details about the constituencies in which either BJP or Congress won. Each constituency is described by a point in the  2D plane.

The senior leadership of BJP has insisted on identifying the strongest belt of Congress in Karnataka. Their strategy is to break the strongest belt of congress in the next election.

The strongest belt of congress is decided as follows :
It is a rectangular area with sides parallel to the coordinate axes.
This area contains only those constituencies which are won by Congress, and no BJP won constituency.
If there are multiple such rectangular areas, the strongest belt is the one which contains maximum number of Congress won constituencies.
Out of all such rectangular areas having maximum number of Congress won constituencies, the strongest belt is the one which has minimum area (notice that if there are many such rectangular areas having same minimum area, you can select any one as the strongest belt).
The strongest belt can have zero area also.

You are given the details of N constituencies. Each constituency is represented by its x and y coordinates and a character ( C or B for Congress and BJP respectively), which represents the winning party of that constituency.

Your task is to find the strongest belt of Congress.

Input Format
The first line of input contains an integer N representing the total number of constituencies.
Following N lines contains details of the constituencies. Each line contains 2 integers x and y and a character c. If c is C, then congress won this constituency, else if it is B, then BJP won this constituency. There is at least one constituency in which Congress won.

Constraints
1 <= N <= 550
0 <= x, y <= 1000

Output Format
Print 2 integers in separate lines. First integer represents the number of constituencies in the strongest belt of congress. The second integer represents the area of the strongest constituency of the congress.
Sample TestCase 1
Input

2
1 1 C
2 2 B
Output

1
0
Explanation



There is only one Congress constituency which can be enclosed inside a rectangle of side 0 x 0 and total area = 0 x 0 = 0. The strongest belt is shown in yellow in the above figure.
Sample TestCase 2
Input

3
1 1 C
1 2 C
3 4 B
Output

2
0
Explanation



The strongest congress belt is shown in yellow in the above figure. It is a rectangle of side 1 x 0, having an area 0 and containing 2 congress won constituencies.
Sample TestCase 3
Input

7
1 1 C
1 3 C
3 3 C
4 1 B
4 2 B
5 1 B
5 3 B
Output

3
4
Explanation

The area shaded in yellow in the following image shows the strongest belt of Congress.

The strongest belt is a rectangle having dimensions 2 x 2. It has an
area of 4 units and it is containing 3 congress won constituencies.




Time Limit(X):
0.75 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
C, C++, C++11, C++14, C#, Java, Java 8, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, Whitespace