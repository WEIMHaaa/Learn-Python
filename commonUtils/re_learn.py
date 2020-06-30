import re

print(re.search(r'abc', 'abcef'))
print(re.fullmatch(r'abc', 'abcef'))
print(re.fullmatch(r'abc', 'abc'))
