import sys
import random

def sort_pair(my_tuple):
    x, y = (my_tuple)
    if x > y: return y, x
    else: return my_tuple
print (sort_pair((7,6)))



def choice_from_range(string:str, begin_index:int, end_index:int) -> str:
    return random.choice(string[begin_index:end_index+1])
print (choice_from_range("abcdef", 3, 5))
print('\n')



def is_palindrome(string:str) -> bool:
    polindr_string=''
    for sym in string:
        polindr_string=sym + polindr_string
    if string == polindr_string:return True;
    else:return False;

print (is_palindrome('оллоs'))


def filter_string(text:str,symbol:str):
    res_text=''
    for sym in text:
        if sym.lower() != symbol.lower():
            res_text+=sym
    return res_text.strip(' ot')

print(filter_string('I look back if you are lost','i'))

print('\n')

def join_numbers_from_range(numb1:int, numb2:int):
    summ=''
    while numb1<=numb2:
        summ=summ + str(numb1)
        numb1+=1
    return summ  
print(join_numbers_from_range(1,5))


def print_numbers(n: int):
    while n>=1:
        print (n)
        n-=1
        if n<1:
            print('finished!')
print_numbers(5)


def get_number_explanation(number:int) -> str:
    match number:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return 'just a number'
get_number_explanation(666)



def normalize_url(string_url:str) -> str:
    if string_url[:8] == 'https://':
        return string_url
    elif string_url[:7] == 'http://':
        return 'https://' + string_url[7:]
    else:
        return 'https://' + string_url

print(normalize_url('http://ya.ru')) 

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
