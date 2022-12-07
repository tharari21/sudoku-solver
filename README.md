# Python Sudoku Solver Using Backtracking Algorithm


## Naive Approach
Try every possible combination for every square until you solve it. This would take O(9^81) time. Way too slow.

## Backtracking Approach
1. Find empty square on board.
2. Try all numbers in square until you find one that works (for a number to work, the number can't be in its row, column or box)
3. Repeat steps 1 and 2 until you get to a point that you can't find a correct number to put in a box. Once you're at that point, backtrack. 
By backtrack we mean go back a step and continue from there (similar to DFS)

Let's look at an example to help explain Backtracking

Say I had this board
[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
where the 0's represent empty spaces.
We'd start by finding an empty space which is the first 0 on first row. Can we put a 1 there?
No because there's a 1 in that column and row, so how about a 2? no again. How about a 3? Yes so put a 3 there. Find next empty space which is 2 spaces to the right. Can't put 1 or 2 because
those are both in the row and we can't put a 3 because we just put a 3. 
4 is also in the row so no good. We try every number until 9. Thankfully we can put a 9 there so we do. After putting 9 there, we move to next space. Now we cannot put any number here because the row and column is filled already so we backtrack to previous number and since there is no other number except for 9 we can put there we backtrack again to where we put the 3. Repeat this logic until solved.

The backtracking method will stop if it sees this route won't work.
