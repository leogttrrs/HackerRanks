Problema em https://www.hackerrank.com/challenges/challenging-palindromes/problem

You have two strings, a and b. Find a string, S, such that:

- Scan be expressed as  where  is a non-empty substring of  and  is a non-empty substring of .
- S is a palindromic string.
= The length of S is as long as possible.
- For each of the q pairs of strings (a and b) received as input, find and print string S on a new line. If you're able to form more than one valid string , print whichever one comes first alphabetically. If there is no valid answer, print "-1" instead.

Output Format:

For each pair of strings (a and b), find some S satisfying the conditions above and print it on a new line. If there is no such string, print  instead.

Sample Input
```
3
bac
bac
abc
def
jdfh
fds
```
Sample Output
```
aba
-1
dfhfd
```