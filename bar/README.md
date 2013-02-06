Bar Problem
============

N friends are playing a game. Each of them has a list of numbers in front of himself.

Each of N friends chooses a number from his list and reports it to the game administrator. Then the game administrator sorts the reported numbers and shouts the K-th largest number.

You want to know the count all possible numbers that the game administrator can shout.

Input Format:

First line of the input contain an integer T, the number of testcases.
Then follow T testcases. For each test case the input is of the following format.

In the first line there are two numbers N and K. In each of next N lines there is an integer a_i followed by a_i integers, ith line describes the list for ith person.

All the numbers in all the lists are unique.

Output Format:

For each testcase print in a separate line the count of numbers that the game administrator can shout.

Sample Input 

      2
      3 3
      3 2 5 3
      3 8 1 6
      3 7 4 9
      20 11
      1 3
      1 2
      11 1 4 55 6 80 8 9 19 11 12 13
      15 14 177 16 17 18 10 20 21 22 37 24 25 26 27 28
      7 190 30 31 32 33 34 35
      12 81 23 195 39 40 41 42 43 49 45 46 47
      15 48 44 50 51 52 53 54 5 121 57 58 59 98 61 62
      3 63 64 65
      10 66 67 68 69 70 71 72 73 74 75
      4 76 91 29 79
      11 7 36 82 83 84 85 86 96 88 89 90
      17 77 92 93 172 95 87 97 60 99 100 101 102 103 135 186 106 107
      10 108 109 110 111 112 113 114 115 116 117
      1 118
      8 119 120 56 122 123 124 125 126
      9 127 128 129 130 131 132 133 134 104
      11 136 137 138 139 140 141 142 143 144 145 146
      20 147 148 149 150 151 152 153 154 159 156 157 158 155 180 161 162 163 164 165 166
      18 167 168 169 170 171 94 173 174 175 176 15 178 179 160 181 182 183 184
      17 185 105 187 188 189 78 191 192 193 194 38 196 197 198 199 200 201

       

Sample Output 

       6
       89 

        

Explanation

In the sample example given, for the first testcse N = 3 and K = 3. List for the first person is {2 5 3}
, {8 1 6} for second and {7 4 9} for the third. In this case all the numbers in {4, 5, 6, 7, 8, 9} have a chance to be the third biggest selected number.


All the numbers that can be shouted are : 

Testcase1:

        4 5 6 7 8 9

Testcase2:

        38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109- 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 

Constraints :

        1 <= T <= 5

        1 <= N <= 1000

        1 <= K, a_i <= N

all the numbers in input are positive and will fit in 32-bit integer
