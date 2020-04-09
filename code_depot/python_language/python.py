# 1. Remove the leading 0s in a number represented by string, if all digits are 0, return '0'
    s.lstrip('0') or '0'

# 2. Greatest common divisor
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a

# 3. Sum of the squares of all digis of num n
    sum(int(d) ** 2 for d in str(n))

# 4. Sum of all even indices in an array
    sum(array[::2])

# 5. ~i means index from right, if length is n, it equals n - 1 - i

# 6. pass an integer by reference: create a list with one element, it is ugly,
#    but in Python we can do no better than that

# 7. the following values are considered False in Python
#    1) None
#    2) False
#    3) Zero of any numeric type, e.g. 0, 0.0, 0j
#    4) Empty sequence, e.g. (), [], ''
#    5) Empty mapping. e.g. {}
#    6) Objects of Class which has __bool__() or __len__ method which returns 0
#       or False
#    All other values except these values are considered True
