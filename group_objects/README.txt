There are N objects kept in a row. The ith object is at position x_i. You want to partition them into K groups. You want to move all objects belonging to the same group to the same position. Objects in two different groups may be placed at the same position. What is the minimum total amount by which you need to move the objects to accomplish this?

Input:
The first line contains the number of test cases T. T test cases follow. The first line contains N and K. The next line contains N space seperated integers, denoting the original positions x_i of the objects.

Output:
Output T lines, containing the total minimum amount by which the objects should be moved.

Constraints:
1 <= T <= 1000
1 <= K <= N <= 200
0 <= x_i <= 1000

Sample Input:
3
3 3
1 1 3
3 2
1 2 4
4 2
1 2 5 7

Sample Output:
0
1
3

Explanation:

For the first case, there is no need to move any object.
For the second case, group objects 1 and 2 together by moving the first object to position 2.
For the third case, group objects 1 and 2 together by moving the first object to position 2 and group objects 3 and 4 together by moving object 3 to position 7. Thus the answer is 1 + 2 = 3.
