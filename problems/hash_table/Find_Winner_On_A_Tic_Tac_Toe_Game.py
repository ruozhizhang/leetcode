'''
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places
"O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column,
or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row
and column of the grid where they mark their respective character in the order in which A
and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return
"Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is
initially empty and A will play first.

Example 1:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"

Example 2:
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO "
"   "    "   "    "   "    "   "    "   "    "O  "

Example 3:
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"

Example 4:
Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "

Constraints:
1 <= moves.length <= 9
moves[i].length == 2
0 <= moves[i][j] <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
'''

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        '''
        algorithm:
        1. there can only be 8 ways to win the game: 3 horizontally, 3 vertically, 2
        diagonally, use a dict to record how many nodes have been put in each way for
        each player
        2. increase the count as traversing the moves, if the count of any player reaches
        three, he wins, otherwise, return 'Pending' if total moves are less than 9, else
        return 'Draw'
        '''
        d = {
            0 : [0, 0],
            1 : [0, 0],
            2 : [0, 0],
            3 : [0, 0],
            4 : [0, 0],
            5 : [0, 0],
            6 : [0, 0],
            7 : [0, 0]
        }

        def play(p, m):
            target = [m[0], m[1] + 3]
            if m[0] == m[1]:
                target.append(6)
            if m[0] + m[1] == 2:
                target.append(7)

            for i in target:
                d[i][p] += 1
                if d[i][p] == 3:
                    return True
            return False

        for i, m in enumerate(moves):
            if play(i % 2, m):
                return 'A' if i % 2 == 0 else 'B'

        return 'Draw' if len(moves) == 9 else 'Pending'
