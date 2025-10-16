Given a  2D array, arr , an hourglass is a subset of values with indices falling in the following pattern:

a b c  
  d  
e f g

There are 16 hourglasses in a 6x6 array. The hourglass is the sum of the values in an hourglass. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.

Example

arr=
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
The 16 hourglass sums are:

-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18
The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2:

0 4 3
  1
8 6 6
