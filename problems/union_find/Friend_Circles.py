'''
https://leetcode.com/problems/friend-circles/

There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature. For example, if A is a direct friend of B,
and B is a direct friend of C, then A is an indirect friend of C. And we defined a
friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other,
otherwise not. And you have to output the total number of friend circles among all
the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.

Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct
friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle,
so return 1.

Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
'''

# Approach 1: DFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        seen = [0] * n
        numCircles = 0
        for i in range(n):
            if seen[i] == 0:
                numCircles += 1
                seen[i] = 1
                stack = [i]
                while stack:
                    cur = stack.pop()
                    for nxt in range(n):
                        if cur != nxt and M[cur][nxt] == 1 and seen[nxt] == 0:
                            seen[nxt] = 1
                            stack.append(nxt)

        return numCircles

# Approach 2: Union Find
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        parent = {i : i for i in range(n)}
        rank = {i : 0 for i in range(n)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootX] = rootY
                rank[rootY] += 1
            return True

        res = n
        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    if union(i, j):
                        res -= 1

        return res
