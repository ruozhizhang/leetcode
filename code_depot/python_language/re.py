'''
regular expression

import re
re.findall(pattern, string)
re.split(pattern, string)
re.sub(pattern, replace, string)

'''

# 1. re.findall(pattern, string) -> list of strings containing all matches
string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'
result = re.findall(pattern, string)
print(result)
# Output: ['12', '89', '34']

# 2. re.split(pattern, string) -> list of strings after splitting using pattern
# if pattern is not found, returns ['']
string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'
result = re.split(pattern, string)
print(result)
# Output: ['Twelve:', ' Eighty nine:', '.']

# 3. re.sub(pattern, replace, string) -> a string where matched occurrences are
# replaced with content of replace variable
# if pattern is not found, returns the original string

# multiline string
string = 'abc 12\
de 23 \n f45 6'
# matches all whitespace characters
pattern = '\s+'
# empty string
replace = ''
new_string = re.sub(pattern, replace, string)
print(new_string)
# Output: abc12de23f456

# 4. When r or R prefix is used before a regular expression, it means raw string.
# For example, '\n' is a new line whereas r'\n' means two characters: a backslash \ followed by n.
# Backlash \ is used to escape various characters including all metacharacters.
# However, using r prefix makes \ treat as a normal character.

string = '\n and \r are escape sequences.'
result = re.findall(r'[\n\r]', string)
print(result)
# Output: ['\n', '\r']
