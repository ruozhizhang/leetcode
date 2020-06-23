'''
https://leetcode.com/problems/expressive-words/

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo",
"hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters
that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by
any number of applications of the following extension operation: choose a group consisting
of characters c, and add some number of characters c to the group so that the size of the
group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get
"hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we
could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo",
then the query word "hello" would be stretchy because of these two extension operations:
query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy.

Example:
Input:
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

Notes:
0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
'''

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        res = 0
        for word in words:
            if self.isStretchy(S, word):
                res += 1
        return res

    def isStretchy(self, S, word):
        m, n = len(S), len(word)
        i = j = 0
        while i < m and j < n:
            if S[i] != word[j]:
                return False

            pre_i = i
            i += 1
            while i < m and S[i] == S[i - 1]:
                i += 1

            pre_j = j
            j += 1
            while j < n and word[j] == word[j - 1]:
                j += 1

            if i - pre_i < j - pre_j or i - pre_i > j - pre_j and i - pre_i < 3:
                return False

        return i == m and j == n
