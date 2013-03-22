You want to create a staff to use in your martial arts training, and it has to meet some specific requirements.
  
1. You want it to be composed of two smaller staves of equal length so that you can either use it as a single staff or as two smaller ones.

2. You want the full sized staff's center of gravity to be exactly in the middle of the staff.

You have a very, very long branch from which you can cut the pieces for your staff.  The mass of the branch varies significantly throughout it, so you use just any two pieces of the same length.  Given a description of the mass throughout the branch, determine the longest staff you can make, then return three integers on a single line, the first two indicating the first index of each half-staff, and the third indicating the length of each half-staff.
     
The input will be given on a single line as a string of digits [1-9], each digit representing the mass of a section of the branch.  All sections are the same size and the maximum length of the string is 500. Here is an example:
      
41111921111119
11119   11119

If the indicated sections are cut from the branch they will satisfy your requirements.  They are both the same length, and they can be put together as either 9111111119 or 1111991111, both of which have a center of gravity exactly in the center of the staff.


Center of gravity can be determined by taking a weighted average of the mass of each section of the staff.  Given the following distances and masses:
Distance: 12345678
Mass: 22241211

Sum of the mass of each section: 2 + 2 + 2 + 4 + 1 + 2 + 1 + 1 = 15
Weighted sum of the masses:
2*1 + 2*2 + 2*3 + 4*4 + 1*5 + 2*6 + 1*7 + 1*8 = 60
Weighted sum / regular sum = 60 / 15 = 4

This means that the center of mass is in section 4 of the staff.  If we wanted to use this staff the center of gravity would need to be (8+1)/2 = 4.5.

Here is an example problem:

131251141231
----    ----

If we take the sections indicated we get 1312 and 1231.  By reversing the first one and putting them together we get 21311231

Sum of the mass of each section: 2 + 1 + 3 + 1 + 1 + 2 + 3 + 1 = 14
Weight sum of the masses:
2*1 + 1*2 + 3*3 + 1*4 + 1*5 + 2*6 + 3*7 + 1*8 = 63
Weighted sum / regular sum = 63 / 14 = 4.5

This puts the center of mass exactly in the center of the staff, for a perfectly balanced staff.  There isn't a longer staff that can be made from this, so the answer to this problem is

0 8 4

Because the half-staves begin at indices 0 and 8 (in that order) and each is of length 4.
