print(fr'Path = C:\Users\gideon\PycharmProjects\PythonProject\GG_Project-2_Strings_and-Files\.venv', '\n\n')

print(f'Date: 11/20_E7/2025  \t\t updated Learn 47 String methods with new ideas to present See ##NEW !!!')



#Below copied from Scratch_01 on 10/12/2025: (and Package_03 copied into this venv)
import inspect
import sys
import os
import time
import keyboard             #--- enable single key press inputs
import pyautogui as gu      #--- enable cursor control
import webbrowser           #--- enable opening up desired URL's for learning frames
import pyperclip            #--- enable use of clipboard
#import random
from random import choice   #--- enable random choice() methodnnn
from random import shuffle   #--- enable random shuffle() method

from Package_03 import vars_01 as v  #-- google "python syntax of an import from statement"
from Package_03 import mssgs_01 as msg
from Package_03 import funcs_01 as fn
from Package_03 import funcs_02 as f2

pause_1 = 5     #--time.sleep() in seconds
pause_2 = 1

print(f'Current working directory is {os.getcwd()}')  #-- https://www.youtube.com/watch?v=VfRuZOFNfpc


print(f'Copied from Idently 47 List methods 4/16/2025 and modified  https://www.youtube.com/watch?v=bnSYeYFRCaA&t=108s')
print(f'Link to Old Man BACK page here: https://oldmanlearningsupport.blogspot.com'); time.sleep(pause_2)
print(f'Google the following as ##New: "dynamic selection of string method applied to a string"'); time.sleep(pause_2)
print(f'Import of func_02 as f2 is ##New !!, includes a ##New gen_options_table() function'); time.sleep(pause_2)

print(f'\n(A)\t\tLearn about the {v.yy_}Python dir(object){v.z_} function here: https://www.google.com/search?q=python+dir+function&sourceid=chrome&ie=UTF-8')
time.sleep(pause_1)
print(f'\n(B)\t\tLearn about the {v.yy_}Python help(function){v.z_} function here: https://www.geeksforgeeks.org/python/help-function-in-python/')
time.sleep(pause_1)



fn.skip(2); fn.sl0('*=', 60); fn.skip(2)

## type = STR

tuple_of_dicts= f2.enum_var_methods_dict(str)
first_tuple = tuple_of_dicts[0]
second_tuple = tuple_of_dicts[1]
fn.skip(2)
print(f'Here are the 47 methods in a first dictionary:\n{first_tuple}'); time.sleep(pause_1)
print(f'Here is the REVERSE second dictionary:\n{second_tuple}'); time.sleep(pause_1)

#breakpoint()
## type = LIST

fn.skip(2); fn.sl0('*=', 60); fn.skip(2)

tuple_of_dicts= f2.enum_var_methods_dict(list)
first_tuple = tuple_of_dicts[0]
second_tuple = tuple_of_dicts[1]
fn.skip(2)

#print(help(list))  #-- not very useful
#fn.skip(2)

print(f'Here are the ___ methods in a first dictionary:\n{first_tuple}'); time.sleep(pause_1)
print(f'Here is the REVERSE second dictionary:\n{second_tuple}'); time.sleep(pause_1)

#breakpoint()
## type = TUPLE

fn.skip(2); fn.sl0('*=', 60); fn.skip(2)

tuple_of_dicts= f2.enum_var_methods_dict(tuple)
first_tuple = tuple_of_dicts[0]
second_tuple = tuple_of_dicts[1]
fn.skip(2)
print(f'Here are the ___ methods in a first dictionary:\n{first_tuple}'); time.sleep(pause_1)
print(f'Here is the REVERSE second dictionary:\n{second_tuple}'); time.sleep(pause_1)

#breakpoint()
## type = DICT

fn.skip(2); fn.sl0('*=', 60); fn.skip(2)

tuple_of_dicts= f2.enum_var_methods_dict(dict)
first_tuple = tuple_of_dicts[0]
second_tuple = tuple_of_dicts[1]
fn.skip(2)
print(f'Here are the ___ methods in a first dictionary:\n{first_tuple}'); time.sleep(pause_1)
print(f'Here is the REVERSE second dictionary:\n{second_tuple}'); time.sleep(pause_1)

#breakpoint()
## type = SET
fn.skip(2); fn.sl0('*=', 60); fn.skip(2)

tuple_of_dicts= f2.enum_var_methods_dict(set)
first_tuple = tuple_of_dicts[0]
second_tuple = tuple_of_dicts[1]
fn.skip(2)

print(f'Here are the ___ methods in a first dictionary:\n{first_tuple}')
print(f'Here is the REVERSE second dictionary:\n{second_tuple}')

fn.skip(2); fn.sl0('*=', 60); fn.skip(2)

#breakpoint()
## type = BOOL
tuple_of_dicts= f2.enum_var_methods_dict(bool)
first_tuple = tuple_of_dicts[0]
second_tuple = tuple_of_dicts[1]
fn.skip(2)

print(f'Here are the ___ methods in a first dictionary:\n{first_tuple}')
print(f'Here is the REVERSE second dictionary:\n{second_tuple}')

fn.skip(2); fn.sl0('*=', 60); fn.skip(2)

#breakpoint()

n=0

n+=1;
sMethod = 'capitalize'
sMethod_ = sMethod + '( )'

cols= 3 #-- numb of columns in the "what next" options table
rows = 2
opts_dict = {'g': f'{v.yy_}G ={v.z_} Goog {sMethod_}',
             'u': f'{v.yy_}U ={v.z_} YouTube {sMethod_}',
             'o': f'{v.yy_}O ={v.z_} Old Man Back page re ___',
             'x': f'{v.yy_}X ={v.z_} Jump to next study frame',
             'a': f'{v.yy_}A ={v.z_} TBD', 'b' : f'{v.yy_}B ={v.z_} TBD'}
opts_keys = {'0': 'g', '1': 'u', '2': 'o', '3': 'x', '4': 'a', '5': 'b'}

allowed = 'guoxab'
allowed_ = list(allowed)

## String Method 01 = CAPITALIZE

samp_1 = 'the quick Brown fox Beat the slow turtle.'
samp_2 = 'every Good Boy Deserves Favor'
samp_3 = 'what goes UP Must Come down. HELLO WORLD'

f2.study(samp_1, samp_2, samp_3, subject = 'string methods', sMethod = 'capitalize', meth_ID= n)

print(f'({n})\t\tBelow example shows the {v.yy_}{sMethod_} method{v.z_} applied to "DEBUG NEEDED HERE"')

'''
q_Google_1 = f'What are some practical uses for the {sMethod_} function of python?'
# q_Google_2 = f'Using the pyperclip module of Python'
# q_Google_3 = f'Using the {sMethod} method of Python'
q_W3School_1 = f'https://www.w3schools.com/python/ref_string_{sMethod}.asp'
url_tail1 = f'/search?q={q_Google_1}'
url_full = f'https://www.google.com' + url_tail1
webbrowser.open(url_full)
webbrowser.open(q_W3School_1)
#: https://www.google.com/search?q=%22Stack+Exchange%22+OR+StackOverflow
# https://webapps.stackexchange.com/questions/39818/how-should-i-write-the-url-for-a-specific-google-search-queryhttps://webapps.stackexchange.com/questions/39818/how-should-i-write-the-url-for-a-specific-google-search-query
# https://www.w3schools.com/python/ref_string_capitalize.asp
#pyperclip.copy("This text will be copied to your clipboard.")
#pyperclip.copy(q_Google_1)
'''

fn.skip(2); fn.sl0('*=', 60); fn.skip(2)

## String Method 02 = CASEFOLD
n+=1;
sMethod = 'casefold'
sMethod_ = sMethod + '( )'

cols= 3 #-- numb of columns in the "what next" options table
rows = 2
opts_dict = {'g': f'{v.yy_}G ={v.z_} Goog {sMethod_}',
             'u': f'{v.yy_}U ={v.z_} YouTube {sMethod_}',
             'o': f'{v.yy_}O ={v.z_} Old Man Back page re ___',
             'x': f'{v.yy_}X ={v.z_} Jump to next study frame',
             'a': f'{v.yy_}A ={v.z_} TBD', 'b' : f'{v.yy_}B ={v.z_} TBD'}
allowed = 'guoxab'
allowed_ = list(allowed)

samp_1 = 'the quick Brown fox Beat the slow turtle.'
samp_2 = 'every Good Boy Deserves Favor'
samp_3 = 'what goes UP Must Come down. HELLO WORLD'

f2.study(samp_1, samp_2, samp_3, subject = 'string methods', sMethod = 'casefold', meth_ID= n)

##New
display_id = '(22)'   #-- print Header box for frame number 22
fn.sl1(display_id, f'{v.yy_}+=', 70)      #-- print the top line
fn.slm(msg.intro_22, f'{v.g_}|||', 90)    #-- middle line = OPTIONS PANEL
fn.sl0(f'{v.yy_}-+', 68)

print(f'{v.z_}=')

cols= 3 #-- numb of columns in the "what next" options table
rows = 2
opts_dict = {'g': f'{v.yy_}G ={v.z_} Goog {sMethod_}',
             'u': f'{v.yy_}U ={v.z_} YouTube {sMethod_}',
             'o': f'{v.yy_}O ={v.z_} Old Man Back page re ___',
             'x': f'{v.yy_}X ={v.z_} Jump to next study frame',
             'a': f'{v.yy_}A ={v.z_} TBD', 'b' : f'{v.yy_}B ={v.z_} TBD'}
allowed = 'guoxab'
allowed_ = list(allowed)

opts_keys = {'0' : 'g', '1' : 'u', '2' : 'o', '3': 'x', '4': 'a', '5': 'b'}
f2.gen_options_table(cols,rows, opts_dict, opts_keys)
fn.sl0(f'{v.yy_}-+', 68)
print(f'\n{v.z_}{allowed_ =}\n')
print(f'Length of g= {len("{v.yy_}G ={v.z_} Goog {sMethod_}")}')
print(f'Length of u= {len("{v.yy_}U ={v.z_} YouTube {sMethod_}")}')
print(f'Length of o= {len("{v.yy_}O ={v.z_} Old Man Back page re ___")}')
print(f'Length of x= {len("{v.yy_}X ={v.z_} Jump to next study frame")}')

##New

breakpoint()
#: 3: center        --> pads with n fill chars and centers sample_1 in whole
n+=1; print(n, ':', sample_1.center(60, '#')) # outputs: #########the quick Brown fox beat the slow turtle.##########

#: 4: count       --> counts the number of occurrences of arg in the sample_1
n+=1; print(n, ':', sample_1.count('t'))  # outputs: 5 (There are 5 T's in 'the quick Brown fox Beat the slow turtle.'

#: 5: encode       --> converts sample_1 into specified alternate coding, for example UTF-8
n+=1

#: 6: endswith      -->returns Boolean to test of whether sample_1 ends with any letters in tuple
n+=1; print(n, ':', sample_1.endswith(('.', '?', '!')))  #note 3 )'s at end outputs True because ends with period

#: 7: expandtabs    --> locates tabs (\t) inside sample_3 and makes them bigger
sample_3= 'hello\tthere\tmy\tpretty'
n+=1; print(n, ':', sample_3.expandtabs(10))  #outputs: hello     there     my        pretty

#: 8: find      --> locates arg substring in sample_1 and gives its starting index
n+=1; found = sample_3.find('\t')
print(n, ':', sample_3.find('\t'))  #outputs: 5 (1st place is index=0)
print(sample_3[found:])             #<-- using slice method tp print from found position to end
                                    # reminder: 'https://www.youtube.com/watch?v=bnSYeYFRCaA&t=108s'
#: 9: format    -->   inserts substitute substrings into main string
n+=1; sample_4 = 'The {subject} is {action}ing {adverb} {object}'
print(n, ':', sample_4.format(subject= 'elephant', action= 'work', adverb= 'very', object= 'hard' ))
sample_5 = 'The {} is {}ing {} {}'
print(n, ':', sample_5.format('elephant', 'work', 'very', 'hard' ))     #<-- same result using blank curly pairs
                        # both prints output: The elephant is working very hard
#: 10: format_map   --> uses a specified dictionary object and replaces in-string keys with their dictionary values
n+=1; map: dict = {'subject' : 'Elephant', 'action' : 'Work',  'adverb' : 'Very',  'object' : 'Well'}
print(n, ':', sample_4.format_map(map))   #<-- Note that map is a dictionary and keys are strings, as are their values

#: 11: index ---> similar to find except that it returns an error if substring not found as opposed to returning a -1 (False)
n+=1; found = sample_3.find('\t')
print(n, ':', sample_3.index('\t'))  #outputs: 5 as position of escape-Tab (1st place is index=0)
# print(n, ':', sample_3.index('\n'))  #outputs an error message in output window

#: 12: isalnum      --> Is the sample string purely Alpha-Numeric ? (Only A-Z, a-z, 0-9)
sample_6 = 'abcdefg123'
sample_7 = 'abcdefgH'
n+=1; print(n, ':', sample_5.isalnum())
print(n, ':', sample_6.isalnum())

#: 13: isalpha      --> Is the sample string purely Alpha (not even numbers allowed)
n+=1; print(n, ':', sample_6.isalpha())
print(n, ':', sample_7.isalpha())

#: 14: isascii      --> Is the sample string purely ASCII coded?
n+=1; print(n, ':', sample_6.isascii())

#: 15: isdecimal    --> Is the sample string purely 0-9?

#: 16: isdigit    --> Is the sample string purely numbers but in any form including funny fonts

#: 17: isidentifier    --> Can the sample string operate as valid Python variable name?

#: 18: islower      --> Is the sample string purely lower case a-z?
#: 19: isnumeric    ---> stick with is decimal

#: 20: isprintable  --> Is the sample string usable in a one-line print() statement?
#: 21: isspace      --> Only spaces
#: 22: istitle      --> 1st leter of each word is capital
#: 23: isupper

#: 24: join      -->  join the string arguments
joiner: str = '---'   #this will be inserted between the to-be-joined args
n+=10; print(n, ':', joiner.join([sample_1, sample_2, sample_3]))

#: 25: ljust    ---> pads to the right with filler
n+=1; print(n, ':', sample_6.ljust(30, '*'))  #outputs: abcdefg123********************

#: 26: lower    ---> converts all to LOWER case, no arg

#: 27: lstrip   --->  strip argument off of left side of sample
n+=2; print(n, ':', sample_6.lstrip('abc')) #outputs: defg123

#: 28: maketrans --> converts text into a translation table for use with translate() function
table = sample_3.maketrans('ht', '-=') #--> plan to replace EACH h and t with RESPECTIVE chars of 2nd arg of SAME length
n+=1; print(n, ':', table)               #---> creates an ascii coded translation dictionary -can use emoji's
print(sample_3.translate(table))        #---> Translate according to pre-made Table

#: 29: partition  #--> specify a partitioning substring that breaks sample into 3 LIST items with partitioner in middle
n+=1; print(n, ':', sample_6.partition('fg'))   #outputs: ('abcde', 'fg', '123')

#: 30: removeprefix #--> remove specified opening substring
n+=1; print(n, ':', sample_5.removeprefix('Th'))

#: 31: removesuffix     #---> same as prefix but from other end of sample
n+=1; print(n, ':', sample_5.removesuffix('{}'))

#: 32: replace  #--> remplace specified substring (1st arg) with 2nd arg, optional 3rd arg is number of times to do
n+=1; print(n, ':', sample_5.replace('{}', 'BRACKS'))

#: 33: rfind  #--> Starting from the RIGHT, find position in sample of arg text, position is counted from left !!!
n+=1; print(n, ':', sample_1.rfind('slow')) #outputs: 29 which is index of 's'  (rindex does same but returns error)

#: 34: rindex
n+=1; print(n, ':', sample_1.rindex('slow'))    #--> Breaks as an error if not found

#: 35: rjust    #--> Justifies to the RIGHT
n+=1; print(n, ':', sample_1.rjust(60, '_'))

#: 36: rpartition    #--> same as 3-part partition but looks for middle part from the RIGHT side of sample

#: 37: rsplit    #--> starting from RIGHT, split into LIST of substrings using the provided splitter upto max times
n+=2; print(n, ':', sample_1.rsplit(' ', maxsplit=4)) #outputs: ['the quick Brown fox', 'Beat', 'the', 'slow', 'turtle.']

#: 38: rstrip   #--> starting from RIGHT, remove just the first instance of the specified substring
n+=1; print(n, ':', sample_1.rstrip('turtle.')) #<--- requires the whole ending substring?

#: 39: split  #--> starting from LEFT, split into LIST of substrings using the provided splitter upto max times
n+=1; print(n, ':', sample_1.split(' ', maxsplit=3))

#: 40: splitlines  #--> searches for \n and uses it as terminator for creating a list
sample_8 = 'Please be sure to like\nand SUBSCRIBE\nAs well as wathcing\n'
n+=1; print(n, ':', sample_8.splitlines(keepends= False)) #<-- if True, the \n terminators are included in LIST

#: 41: startswith  #--> Boolean result= True/False if sample starts with specified substring
n+=1; print(n, ':', sample_8.startswith('Please'))
print(n, ':', sample_8.startswith('please'))        #<-- and is case sensitive

#: 42: strip    #--> remove the specified substring
n+=1; print(n, ':', sample_8.strip('watching'))       #<-- can be in mid of sample string? NOT WORKING HERE !!!!

#: 43: swapcase    #--> Changes UPPERS to lowers and vise versa

#: 44: title    #--> forces 1st alpha letter of each word to be capped
n+=2; print(n, ':', sample_4.title())

#: 45: translate    #--> See maketable above

#: 46: upper
#: 47: zfill    #--> Zero fill: prefixes the sample with n 0's (for what use, don't know)

# Process finished with exit code 0

##########  EXTRA SECTION: USEFUL f-string METHODS #####
# from https://www.youtube.com/watch?v=EoNOWVYKyo0

#: 50: Inserting commas or underscores into large numbers
biggie: int = 1000000000    #<-- lots of zeroes
n=50; print(n, ':', f'{biggie:,}')  #inserts commas for every 3 zeroes
print(n, ':', f'{biggie:_}')        #inserts underscores for every 3 zeroes, NO OTHER CHARs allowed

#: 51: Use f-string to right-align strings
short = 'Hi You'; short_2 = "Yes it's You"
n+=1; print(n, ':', f'{short:>20}')     #<--- Total string length is 20 chars
print(n, ':', f'{short_2:>20}')
print(n, ':', f'{short_2:<19}', '|')     #<--- left-aligned plus '|" as end indicator
print(n, ':', f'{short_2:^19}', '|')     #<--- CENTER-aligned plus '|" as end indicator
print(n, ':', f'{short_2:_^19}', '|')    #<--- filler char inserted after colon :

#: 52:  Date/time tricks (to be continued)

# (new) Indently ALL f-string tricks from https://www.youtube.com/watch?v=9saytqA0J9A

#60 The basic f-string usage = avoid plus signs and open/close quotes
n=60; print('\n\n\nBasic combining of strings calls for "str1" + "str2"')
my_name: str = 'Gideon'; my_age: int = 73 #<-- next want to combine string plus integer
print('NAME =' + 'Gideon ' + 'AGE = ' + str(my_age))
print(n, ':', 'Above was printed as concatenation of only strings')
print(f'NAME =  {my_name}   AGE = {my_age}')
print(n, ':', 'Above was printed as an f-string using { } for evaluating different types of objects')
n+=1; print('\n', n, ':', f" 5 + 6 = {5+6},  5*6 = {5*6}, 5^3 = {5**3}")
print('Above was printed with  an f-string using { } for evaluating different math expressions')

#: 62 : Auto complete of literal plus value for DEBUGGING runs
debug_var = 125
n+=1; print('\n', n, ':', f"{debug_var = }")
print('Above was printed with  an f-string using {var=} for auto insertion of var name')

#: 63 :  Auto complete even works for Boolean function tests !!!
n+=1; print('\n', n, ':', f"{isinstance(debug_var, int) = }")
print('Above was printed with an f-string using { } for evaluating a Boolean inquiry and auto competing the result')

#: 64 :  Rounding high precision floats and converting value to percentage
multi_digit: float = 8765.4167;  compare_percent: float = 0.5678
n+=1; print('\n', n, ':', f"{multi_digit:.2f}", f"{compare_percent:.2%}")
print('Above was printed with an f-string using { } for rounding to 2 decimal places (2f) and shifting dec point 2 places')
biggie2: float = 1_234_567.8901    #<-- lots of digits (see biggie int above as reminder)
print('\n', n, ':', f"{biggie2:,.1f}")      #<-- don't forget period b4 1f !!
print(' ^^^^ Above uses f-string { } for rounding to 1 decimal place AND insering commas every 3 zeroes')

#: 65 :  Dealing with DATE-TIME issues
from datetime import datetime       #<-- this is a class (a type) that has its own methods
time_now: datetime = datetime.now()  #<-- declares var time_now as being of type, datetime
n+=1; print('\n', n, ':', f"{time_now:%X}")
print(' ^^^^ Above uses f-string { } for limit to just the short form date  (% X )') #<-- can be lower case X too
print('\n', n, ':', f"{time_now:%C}")
print(' ^^^^ Above uses f-string { } for long form date + military time  (% C )')
print('\n', n, ':', f"{time_now:%H:%M:%S}")
print(' ^^^^ Above uses f-string { } for long form time  (% H : M : S )') #<-- note colon (:) separators
print('\n', n, ':', f"{time_now:%H:%M}")
print('\n', n, ':', f"{time_now:%H military :%M time H:M}")
print('\n', '\033[96mThis should be colored blue due to the 033 escape sequence')
print('\033[91m This should be colored red  due to the 033 escape sequence')
print('\033[92m Check out Python Tutorial: Escape Sequence Explained at https://www.youtube.com/watch?v=hExrjJ_KR48')
print('\033[93m Check out Caleb Curry\'s Python Tutorial: at ..')
print('\t https://www.youtube.com/watch?v=9miLWHISMqc&list=PL_c9BZzLwBRKK8ndQBBKolg7IxrC5T6Ws&index=20')

#: 66 :  FRench Raw data specifier for f-strings (at 9:40 / 1942 in Indently video)
print('\n \033[95m This should be colored what? due to the 033 escape sequence')
print('\033[97m This should be colored what? due to the 033 [97m escape sequence, Answer: back to WHITE !!')

raw_text: str = r'Back slashes are \n treated as \b literals \t when the r-string attribute is used'
n+=1; print('\n', n, ':', raw_text)
print('\t On other hand, \t tabs and backups \bare not ignored \" if not \"raw\" ')

sample_11: str = 'My_Name'
sample_path: str = fr'\User\{sample_11}\Documents\PythonTutorials'  #<-- note fr-string !!!!!!!!! the 'f' allows {samp}
print('\nThe path to target folder is:', sample_path) #<-- the French string (fr) sample_path includes raw back slashes

#: 67:  Nested f-strings
n+=1; print('\n', n, ':', f'{5+5=}    {10 + 10=}    {10*10=}      {10**10=:,}') #<-- note also use of biggie colon-comma
print(f'{5+5=}    {10 + 10=} {r'User\Folder\Docs'}  <-- this is a nested r-string')

#: 68:  CUSTOM F-STRINGS !!!!!!!!!!
class Special_text:
    def __init__(self, text : str) -> None:
        self.text = text

    def __format__(self, format_spec: str) -> str:
        match format_spec:      #<--- test for cases of where format_spec is one thing or another
            case 'up':
                return self.text.upper()
            case 'low':
                return self.text.lower()
            case 'len':
                return str(len(self.text))      #<-- this will return the length count as a string
            case _:             #<-- all other cases default to next
                raise ValueError(f'Supplied format specifier {format_spec} is not valid')

my_sample_text_1: Special_text = Special_text('this started off as all lower case but of type: special_text')
my_sample_text_2: Special_text = Special_text('THIS STARTED OFF AS ALL UPPER CASE BUT OF TYPE: SPECIAL_TEXT')
n+=1; print('\n', n, ':', f'{my_sample_text_1:up}')
print('\t', f'{my_sample_text_2:low}')
print('\t', f'{my_sample_text_2:len} <--this is the length count')