'''
list
'''

'''
string
'''
str.split(sep=None, maxsplit=1) -> list
# number of non-overlapping occurrences of sub in [start, end]
str.count(sub[, start[, end]]) -> int
str.upper() -> string
# returns a copy of the string with all substrings old replaced by new
# if count is given, only the first count occurrences are replaced
str.replace(old, new[, count]) -> str
# reverse string
str[::-1]

'''
set
'''

'''
dict
Counter
defaultdict
'''

'''
deque
'''

'''
heapq
'''

'''
variable scope
https://www.w3schools.com/python/python_scope.asp
Local Scope
A variable created inside a function belongs to the local scope of that function,
and can only be used inside that function.

Global Scope
A variable created in the main body of the Python code is a global variable and
belongs to the global scope.

Global variables are available from within any scope, global and local.

Naming Variables
If you operate with the same variable name inside and outside of a function,
Python will treat them as two separate variables, one available in the global scope
(outside the function) and one available in the local scope (inside the function)

Global Keyword
If you need to create a global variable, but are stuck in the local scope, you
can use the global keyword.

The global keyword makes the variable global.
'''
