import re
print(re.findall(r'c.t', 'cat cut c9t ctt'))
# ['cat', 'cut', 'c9t']

print(re.findall(r'ab*', 'a ab abb abbb abc'))
# same thing without the 'c' at the end
# if r'ab+' same thing

print(re.findall(r'colou?r', 'color colour colouur'))
# shows first two words

print(re.findall(r'a{3}', 'aa aaa aaaa aaaaa'))
# aaa aaa aaa

print(re.findall(r'a{2,4}', 'a aa aaa aaaa aaaaa'))
# idk?

print(re.findall(r'^Hello', 'Hello world'))
# prints Hello

print(re.findall(r'world$', 'Hello world/ nworld Hello'))
# it's not correct

print(re.findall(r'[aeiou]', 'hello world'))

print(re.findall(r'[^aeiou]', 'hello world'))
# everything except vowels

print(re.findall(r'\d+', 'abc123xyz'))
# all together 123

print(re.findall(r'\s+', 'Hello world'))
# empty string / whitespace

print(re.findall(r'\S+', 'Hello world'))
# ['Hello', 'world']

print(re.findall(r'w+', 'Hello, world!'))
# w

print(re.findall(r'W+', 'Hello, world!'))
# empty

print(re.findall(r'^Hello', 'Hello world/nHello again', re.MULTILINE))
# 'Hello'

print(re.match(r'Hello', 'Hello world'))
# <re.Match object; span=(0,5), match='Hello'>
# can be used in the code as a boolean in an "if match ()"

print(re.fullmatch(r'Hello world', 'Hello world'))
# <re.Match...>

print(re.split(r', ', 'apple, banana, cherry'))
# list of the 3 fruit

print(re.findall(r'\d++', 'There are 3 apples and 5 bananas.'))
# shows 3 and 5 in an list


# for Vanity Plates make the code in regex


