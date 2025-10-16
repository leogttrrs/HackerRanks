Link do desafio: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.

David wants to perform some number of swap operations such that:

Each container contains only balls of the same type.
No two balls of the same type are located in different containers.

Each row in the array represents a container.
The number in the containers represents the amount of balls of each type inside the container
The types of balls are represented by the columns.

### Example:
```
Containers = 
[ [1, 3, 1],
  [2, 1, 2],
  [3, 3, 3] ]
```
Container 0: One `type 0` ball, Three `type 1` balls, One `type 2` ball

Container 1: Two `type 0` balls, One `type 1` ball, Two `type 2` balls

Container 2: Three `type 0` balls, Three `type 1` ball, Three `type 2` balls

Output: Impossible

### Example 2:
```
Containers = 
[ [0, 2, 1],
  [1, 1, 1],
  [2, 0, 0] ]
```
Output: Possible

