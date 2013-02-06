Reverse Polish Notation
=======================

expression consisting of operands and binary operators can be written in Reverse Polish Notation (RPN) by writing both the operands followed by the operator. For example, 3 + (4 * 5) can be written as "3 4 5 * +".
 
 You are given a string consisting of x's and *'s. x represents an operand and * represents a binary operator. It is easy to see that not all such strings represent valid RPN expressions. For example, the "x*x" is not a valid RPN expression, while "xx*" and "xxx**" are valid expressions. What is the minimum number of insert, delete and replace operations needed to convert the given string into a valid RPN expression?
  
Input:
The first line contains the number of test cases T. T test cases follow. Each case contains a string consisting only of characters x and *.
   
Output:
Output T lines, one for each test case containing the least number of operations needed.
    
Constraints:
1 <= T <= 100
The length of the input string will be at most 100.

Sample Input:
5
x
xx*
xxx**
*xx
xx*xx**

Sample Output:
0
0
0
2
0

Explanation:
 
For the first three cases, the input expression is already a valid RPN, so the answer is 0.
For the fourth case, we can perform one delete, and one insert operation: *xx -> xx -> xx*
