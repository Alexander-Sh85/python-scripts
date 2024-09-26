
import sys

def is_leap_year(year:int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0)
print(is_leap_year(int(sys.argv[1])))


def has_upper_case(string:str) -> bool:
    return (string != string.lower())
has_upper_case('')


def get_age_difference(x:int,y:int) -> int:
    return 'The age difference is ' + str(abs(y-x))
print(get_age_difference(2001, 2018))


def letter_multiply(word:str,char:str,count:int) -> str:
	return word.replace(char,char * count)

print(letter_multiply('python','n',4))

def trim_and_repeat(text,offset=0,repetitions=1):
    return text[offset:] * repetitions

print(trim_and_repeat('python',3,3))




def get_hidden_card(card,count=4):
    return '*' * count  + str(card)[-4:]

print(get_hidden_card(123456789,14))

from random import randint
stark = 'Arya'

# BEGIN (write your solution here)
print (f'''Do you want to eat, {stark}?
Yes, I'm hungry, mom.''')
# END

magic = '\nyou'
print(magic[1])  # => ?

one = 'Naharis'
two = 'Mormont'
three = 'Sand'

# BEGIN (write your solution here)
print(f'{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}')
# END


value = 'Hexlet'

# BEGIN (write your solution here
print(value[2:5])

print(0.1+0.2)

print (str(2) + 'times')
for i in range(10): print(randint(1,10))
