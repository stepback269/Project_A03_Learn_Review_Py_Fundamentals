import inspect
import sys
import os
import keyboard             #--- enable single key press inputs
import pyautogui as gu      #--- enable cursor control
import webbrowser           #--- enable opening up desired URL's for learning frames
import pyperclip            #--- enable use of clipboard
#import random
from random import choice   #--- enable random choice() method
from random import shuffle   #--- enable random shuffle() method

from Package_03 import vars_01 as v  #-- google "python syntax of an import from statement"
from Package_03 import mssgs_01 as msg
from Package_03 import funcs_01 as fn

print(f'(4) The importation of Package_03 / Scratch_01 has begun')

print(f'Testing slicing problem')
test_list_10 = list(range(10))
print(f'{test_list_10 =} ')
test_slice = test_list_10[7::]
print(f'{test_slice =} ')
pos_index= len(test_list_10)-3 # -R equals -3 because [ ... 7, 8, 9] where index of 9 is -1
print(f'{pos_index =} ')
print(f'-R equals -3 here because [ ... 7, 8, 9] where index of 9 is -1')
print(f'So pos_index= len(test_list_10)-R is correct\n\n')
# breakpoint()

os.system('cls')
print(f'\n\n', '*'*60,'\n')
##clear the screen using https://www.naukri.com/code360/library/how-to-clear-a-screen-in-python
# Search for "## (" to find frame headings in here

## (0.0)
print(f'{v.g_}(0.0){v.W_} '
      f'Date: 10/06_M2/2025  '
      f'--Status: Updating Scratch_01 for {v.yy_}Reviewing List and String methods{v.W_} creating fatten() function (09)\n')

l1 = ['apples', 'oranges', 'fruits']
l2 = [[1,2,3]]
l1.extend(l2)

print(f"TESTING: in order are:\n l1 = ['apples', 'oranges', 'fruits']\nl2 = [[1,2,3]] and extend result")
print(f'{l1}\n')  #-- It works

skinny= list(range(115))
fat = fn.fatten(skinny)
print(f'This is the skinny list\n{skinny}\n')
print(f'This is the fat list\n{fat}\n')
print(f'{v.yy_}{fat[0]}')
fn.strip_outr_bracks(fat[1])
print(f'\t\t{v.z_}--^^*-- above was gen\'ed using my strip_outr_bracks() function{v.yy_}' )
fn.strip_inner_bracks(fat[2])
print(f'\t\t{v.z_}--^^*-- above was gen\'ed using my strip_inner_bracks() function{v.yy_}' )
print(f'tuple({fat[3]}){v.z_}\n')
print(f'remainder= {v.yy_}{fat[4]}{v.z_}')
fn.skip(2)
breakpoint()

print(f'\t\t(1) {v.yy_}Firstly{v.W_} click on below {v.yy_}OLD MAN BACK PAGES{v.W_} link to see concept map')
print(f' URL= https://oldmanlearningsupport.blogspot.com/2025/08/frame-000-of-learn-lists-and-modules.html#mid_01\n')

## (0.1)
print(f'{v.g_}(0.1){v.W_} \t\t(2) Click on below link to {v.yy_}REAL PYTHON{v.W_} to see their LISTS course (unlocked part)')
print(f' URL= https://realpython.com/videos/getting-started-lists/\n')
url = 'https://realpython.com/videos/getting-started-lists/'
preface2 = f'\t'
postfix2 = 'for Real Python on getting started with lists'
print(preface2, end=''); fn.gen_short_url(url); print(postfix2)

## (0.2)
url = 'https://www.geeksforgeeks.org/python/url-shorteners-and-its-api-in-python-set-1/'
preface2 = f'{v.g_}(0.2){v.W_} \t'
postfix2 = 'on G4G re SHORTENERS services'
print(preface2, end=''); fn.gen_short_url(url); print(postfix2)

## (0.3)
print(f'\t\t{v.g_}\u007B Hello \u007D {v.W_} <-- printed using Unicodes for curly brackets ( {v.g_}\u007B and \u007D {v.W_})')
url = 'https://unicodeplus.com'
preface2 = f'{v.g_}(0.3){v.W_} \t'
postfix2 = 'on lookup UNICODE escapes = backslash U + code'
print(preface2, end=''); fn.gen_short_url(url); print(postfix2,'\n')

## (_3)
print(f'\t\t(3) See also {v.yy_}Geeks for Geeks{v.W_} re Lists at below ')
print(f' URL= https://www.geeksforgeeks.org/python/python-lists/\n')

## (_4)
print(f'\t\t(4) Further see Metcalfe tutorial re {v.yy_}If Else in a List Comprehension{v.W_} USING THE LINK below ')
print(f' URL= https://www.youtube.com/watch?v=EL--NjvBw6o\n')
print(f'(5) {v.r_}WARNING: Re-reading is not an effective learning mehtod{v.W_}')
print(f'{v.g_} Try creating a conceptual mind map from memory: https://www.youtube.com/watch?v=Z24Td5mtKOs{v.W_}')


print('\n', '*'*40, '\n')
print(f'LEARNING TO WORK WITH LISTS\n')
print(f'Main Concepts = CREATION --> ANATOMY --> CHANGE --> SKILLS\n')
print(f'{v.yy_}Creation = (1) via Literals, (2) via LIST() function, (3) via Comprehension{v.W_}')
print(f'{v.g_} Can you explain / draw out each of these without looking further below ???{v.W_}\n\n\n\n')

## (1a)
my_1st_list = ['strng_1', 172, 10.03, [0.1, 2, 3]]
print(f"(1a) Code used for below output was: {v.yy_}my_1st_list = ['strng_1', 172, 10.03, [0.1, 2, 3]];"
      f" print(f'(\u007Bmy_1st_list\u007D){v.W_}")
print(f'(1a) CREATION {v.yy_}example of a heterogeneiuos list{v.W_} generated with literals is this \n\t{my_1st_list}\n')

## (1b)
my_1st_list_ = ['strng_1', 'strng_2', 'strng_3', 'strng_4']
print(f'(1b) Creation {v.yy_}example of a homogeneiuos list{v.W_} generated with literals is this \n\t{my_1st_list_}')
print(f'Type of item 0 in the list is {type(my_1st_list_[0])}')
print(f'{v.yy_}Type of item 3{v.W_} in the list is {type(my_1st_list_[3])}\n')

## (_2)
#creation via passing in an iterable  sequence, e.g a string, to the list() function
my_2nd_list = list('ABCDEFGHIJ')
print(f'\n (2) Creation example of list {v.yy_}generated with list() func getting a string{v.W_}  is this \n\t{my_2nd_list}\n')

## (3a)
#creation via passing in a tuple to the list() function
my_3rd_list = list((5, 6, 7, 8, 9, 10))
print(f'\n (3a) Creation example of list generated {v.yy_}with list() func getting a  Tuple{v.W_}  is this \n\t{my_3rd_list}\n')

## (3b)
#creation via passing in a set to the list() function
my_3rd_list_ = list({5, 6, 7, 8, 9, 10})
print(f'\n (3b) Creation example of list generated {v.yy_}with list() func getting a  Set{v.W_}  is this \n\t{my_3rd_list_}\n')

## (3c)
#creation via using range() as argument in  the list() function
my_3rd_list_ = list(range(100,111))
print(f'\n (3c) Creation example of list generated {v.yy_}with range (100,110) as arg for list() func {v.W_}  is this'
      f' \n\t{my_3rd_list_}\n')

## (3d)
#creation via using append() as filler in a for loop
my_3rd_list_ = []  #-- start empty
for n in range(200,211):
    my_3rd_list_.append(n)
print(f'\n (3d) Creation example of list generated {v.yy_}with append using range (200,211) as for loop control{v.W_}  is this'
      f' \n\t{my_3rd_list_}\n')
fn.skip(2)

## (3e)
#creation of Sieve of Eratosthenes via using filered append() in a for loop

primes = [2,3]      #--seed the primes list
last_testable = 502
print(f'(3e)\t\tCreating List of PRIMES from 4 to {last_testable} using {v.yy_}Sieve of Eratosthenes{v.z_}\n')

for testable in range(4,last_testable):
    testable_could_be_a_prime = True
    for prime in primes:
        #if testable_could_be_a_prime == False:     #-- This is not needed
            #break       #--break out of the primes loop & try next testable because current testable cannot be a prime
        if testable % prime == 0:  #if testable subject is divisible by a prime, testable is not a prime
            testable_could_be_a_prime = False
            break  # --break out of the primes loop & try next testable because ....
        else: continue
    if testable_could_be_a_prime == True:
        primes.append(testable)  #testable was not divisible by any of the current primes

print(f'(3e)\t\tThe primes list (split) is as follows:')

left_over= len(primes)  #  |0|1|....|24|25| ...... |last|
prnt_line_first = 0; prnt_line_last = 24

fail_safe=0
keep_looping = True
while keep_looping:
    fail_safe += 1
    print(f'fail_safe = {fail_safe}')
    if fail_safe >= 200:
        keep_looping == False
        break
    if left_over <= 25:
        print(f'\t{v.yy_}{primes[prnt_line_first:prnt_line_last+1:]}{v.z_}')  #-- print what is leftover
        keep_looping == False
        break
    else:
        print(f'\t{v.yy_}{primes[prnt_line_first:prnt_line_last+1:]}{v.z_}')
        prnt_line_first = prnt_line_last+1
        prnt_line_last = prnt_line_first + 24
        left_over -= 25         # I forgot this critical step, Have to reduce leftover size !!!
    continue

fn.skip(2)

breakpoint()

## (4a-b)
#creation via list comprehensions
my_4th_list = [j**2 for j in range(13)]
print(f'\n (4a) Creation example of list generated {v.yy_}with list comprehension {v.W_}  is this \n\t{my_4th_list}')
print(f'See also TwT: 10 Comprehensions later below\n')

my_4th_list_ = [j**3 for j in range(11)]
print(f'\n (4b) Creation example of CUBES list generated {v.yy_}with list comprehension {v.W_}'
      f'  is this \n\t{my_4th_list_}\n')

## (5a) range() as an iterable
string_05 = f'hello'
my_5th_list = [string_05 for _ in range(10)]
print(f'\n (5a) Creation example of list generated by range() {v.yy_}with list comprehension {v.W_}'
      f'is this \n\t{my_5th_list}\n')

## (5b) range() as an iterable
my_ranged_list = list(range(10))
print(f'\n (5b) Creation example of list {v.yy_}generated by list(range()){v.W_}'
      f'is this \n\t{my_ranged_list}\n')

## (6a) Slicing
print(f'\n (6a) {v.yy_}SLICING{v.W_} using [2:5] of the list of above example (5b) is this\n\t{my_ranged_list[2:5]}\n')

print(f'\n (6b) {v.yy_}SLICING{v.W_} using [::-1] of the list of above example (5b) is this\n\t{my_ranged_list[::-1]}\n')
print(f'\n (6c) {v.yy_}SLICING{v.W_} using [-1:-4:-2] of the list of above example (5b) is this\n\t{my_ranged_list[-1:-4:-2]}\n')

## (7a) List shuffling
display_id = '(007)'   #-- print GUI box for aside number 007
fn.sl1(display_id, f'{v.g_}▉', 78)      #-- get the sl1 function from the funcs module !!!
fn.slm(msg.aside_007, f'{v.g_}▉▉')  #-- middle line uses text fetched from the messages module !!!!
fn.sl2(f'{v.g_}▉', 80)

frame_id = '007'
prefix = 'msg.aside_007'  #-- warning: this is just a 'string', not a variable name (not a pointer)!

test_shuffled_list = list('ABCDEFGHIJK')
print(test_shuffled_list)
shuffle(test_shuffled_list) #-- see https://www.geeksforgeeks.org/python/python-ways-to-shuffle-a-list/
print(f'The shuffled SAME list is as follows\n', test_shuffled_list)
list_of_nameStrings = [prefix[4:] + n for n in test_shuffled_list] #-- remove 'msg.' bc gotten() specifies msg
print(f'The list of concatenated strings is this\n\t{list_of_nameStrings}')

# mssgs_list_007= [msg.prefix+n for n in test_shuffled_list]
#fn.outp_in_mssgs('aside_', frame_id, 'A-K') #--note: logic error here was fixed
fn.outp_in_list(list_name = list_of_nameStrings, colors = 'GREEN', indent=10)
print('\n')

## (8a)
display_id = '(008)'   #-- print GUI box for aside number 008
fn.sl1(display_id, f'{v.g_}▉', 78)      #-- get the sl1 function from the funcs module !!!
fn.slm(msg.aside_008, f'{v.g_}▉▉')  #-- middle line uses text fetched from the messages module !!!!
fn.sl2(f'{v.g_}▉', 80)

frame_id = '008'
print(f'FRAME {frame_id}:  STUDY THE ENUMERATE FUNCTION\n')
test_2benumerd_list = ['It was the best of times,', 'It was the worst of times,', 'It was the age of wisdom,',
                       "It was the age of foolishness,", "It was the epoch of belief,", "It was the epoch of incredulity,",
                       r"https://www.markpack.org.uk/31802/a-tale-of-two-cities-not-just-a-great-opening-line-a-great-opening-paragraph/"]
print(test_2benumerd_list)
fn.add_alpha_enum(test_2benumerd_list)

print('\n\n')

## (9a)
display_id = '(009)'   #-- print GUI box for aside number 009
fn.sl1(display_id, f'{v.g_}▉', 78)      #-- get the sl1 function from the funcs module !!!
fn.slm(msg.aside_009, f'{v.g_}▉▉')  #-- middle line uses text fetched from the messages module !!!!
fn.sl2(f'{v.g_}▉', 80)
print(f'{v.z_}')        #--sl2 leaves the text as green

frame_id = '009'
url = 'https://www.youtube.com/watch?v=twxE0dEp3qQ&t=225s'
preface2 = f'(9_)\t'
postfix2 = 'for TwT on 10 Comprehensions to know\n'
print(preface2, end=''); fn.gen_short_url(url); print(postfix2)

print(f'(9_)\t A LIST COMPREHENSION has a general form per the following:')
print(f'\t\t{v.yy_}< [ >{v.z_} \t\t Starts with an open Square bracket')
print(f'\t\t{v.yy_}< Insertable evaluatable Expression >{v.z_} \t\t example: x squared')
print(f'\t\t{v.yy_}< Iteration(s) >{v.z_} \t\t example: for x in Iterable ... such as range(10)')
print(f'\t\t{v.yy_}< Insertion conditional >{v.z_} \t\t example: if len(x)>1 ... or if x%2==0')
print(f'\t\t{v.yy_}< ] >{v.z_} \t\t Ends with a close Square bracket --can be on separate line\n\n')

example_9a_list = []
for x in range(10):
    example_9a_list.append(x)   #-- add integer 0-9 into empty list
print(f'(9a) Example list generated with explicit for loop using append() is as follows:')
print(f'\t\texample_9a_list = {v.yy_}{example_9a_list}{v.z_}\n\n')

example_9a_list = [x for x in range(10)]
print(f'(9a\') Example list generated with simple comprehension is as follows:')
print(f'\t\texample_9a_list = {v.yy_}{example_9a_list}{v.z_}\n\n')

## (9b)
example_9b_list = [x**2 for x in range(10)]
print(f'(9b) Example list generated with x squared as comprehension expression is as follows:')
print(f'\t\texample_9a_list = {v.yy_}{example_9b_list}{v.z_}')
print(f'\t\t\t\tSee Twt at 2:09/21:34\n\n')

## (9c)
example_9c_list = [x for x in range(1, 51) if x%2 ==0]
print(f'(9c) Example list generated with conditional that appends only if x mod 2 ==0 is as follows:')
print(f'\t\texample_9c_list = {v.yy_}{example_9c_list}{v.z_}')
print(f'\t\t\t\tSee Twt at 3:22/21:34\n\n')

## (9d)
example_9d_first_list = ['any', 'albany', 'alimony', 'antelope', 'apple', 'bobcat', 'crown', 'arguably']
example_9d_filtered_list = []

for string in example_9d_first_list:
    if len(string) < 2:  #the filter requires a length of 2 or more AND first char= "a" AND last char = "y"
        continue        #-- the continue means we skip the append step !!!
    if string[0] != 'a':
        continue
    if string[-1] != 'y':
        continue
    example_9d_filtered_list.append(string)  #-- if the tested string passes all 3 excluding filters, add to out list

print(f'Original list is as follows:')
print(f'\t\texample_9d_first_list = {v.yy_}{example_9d_first_list}{v.z_}')
print(f'(9d) Example of a filtered list generated with 3 IF filteres inside for loop is as follows:')
print(f'\t\texample_9d_list = {v.yy_}{example_9d_filtered_list}{v.z_}')
print(f'\t\t\t\tSee Twt at 5:38/21:34\n\n')

## (9d')
example_9d_filtered_list =  [               ##-- we spread the bracket contente over multiple lines
        string for string in example_9d_first_list
        if len(string) >= 2
        if string[0] == 'a'
        if string[-1] == 'y'
                            ]               ##-- close bracket is here !!!!
print(f'(9d\') Example of a filtered list generated with 3 IF filteres inside iffy comprenhension [] as follows:')
print(f'\t\texample_9d_list = {v.yy_}{example_9d_filtered_list}{v.z_}')
print(f'\t\t\t\tSee Twt at 7:12/21:34\n\n')


## (9e)                 --- at 7:46/21:34       --flattening a nested list (lists inside main list)
example_9e_first_list = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
example_9e_flattened_list = []

for row in example_9e_first_list:
    for column_item in row:
        example_9e_flattened_list.append(column_item)       #-- there are 3 cols per row in our example

print(f'Original list is as follows:')
print(f'\t\texample_9e_first_list = {v.yy_}{example_9e_first_list}{v.z_}')

print(f'(9e) Example of a flattened list generated with 2 for loops, one nested in other is as follows:')
print(f'\t\texample_9e_list = {v.yy_}{example_9e_flattened_list}{v.z_}')
print(f'\t\t\t\tSee Twt at 8:19/21:34\n\n')

example_9e_flattened_list = [column_item for row in example_9e_first_list for column_item in row]
        #Note: read the comprehension RIGHT to Left: we do Col. item per row and then per row in main matrix

print(f'(9e\') Example of a flattened list generated with comprehension using 2 for loops, one nested in other is as follows:')
print(f'\t\texample_9e_list = {v.yy_}{example_9e_flattened_list}{v.z_}')
print(f'\t\t\t\tSee Twt at 9:04/21:34\n\n')

## (9f)                 --- at 9:26/21:34       -- IF/ELSE comprehension
example_9f_first_list = list(range(10))             #-- gen first list as 0-9 using range inside list() function
example_9f_cat_list = []

# print(f'Debug: 1st list {example_9f_first_list}')

for number in example_9f_first_list:
    if number % 2 == 0:
        example_9f_cat_list.append("Even")
    else:
        example_9f_cat_list.append("Odd_")

print(f'Original list is as follows:')
print(f'\t\texample_9f_first_list = {v.yy_}{example_9f_first_list}{v.z_}')

print(f'(9e) Example of a Catergorizer list generated with IF/ELSE append selection is as follows:')
print(f'\t\texample_9f_list = {v.yy_}{example_9f_cat_list}{v.z_}')
print(f'\t\t\t\tSee Twt at 9:26/21:34\n\n')

example_9f_cat_list.clear()
example_9f_cat_list = [
                        "Even" if number % 2 == 0 else "Odd_" for number in example_9f_first_list
                        ]
print(f'(9f\') Example of a Catergorizer list generated with IF/ELSE comp insert selection is as follows:')
print(f'\t\texample_9f_list = {v.yy_}{example_9f_cat_list}{v.z_}')
print(f'\t\t\t\tSee Twt at 10:50/21:34\n\n')

print(f'(9f\") Example of a Non-list Comprehension')
Rng_Comp_9 = ("Even" if x % 2==0 else "Odd-" for x in range(20))
Tuple_Comp_9 = tuple(Rng_Comp_9)

print(f'\t\t Example: {v.yy_}Tuple_Comp_9 = tuple(("Even" if x % 2==0 else "Odd-" for x in range(20))){v.z_}')
print(f'\t\texample_9f\" Tuple = {v.yy_}{repr(Tuple_Comp_9)}{v.z_}')
print(f'\t\t\t\tSee Twt at 11:14/21:34 = https://youtu.be/twxE0dEp3qQ?t=674')
print(f'\t\t\t\tSee Convert range() object to Tuple in Google='
      f' https://www.google.com/search?q=python+convert+range+object+to+tuple+type\n\n')


## (9g)                 --- at 11:40/21:34       -- Nested comprehensions
print(f'(9g) Example of Nested Comprehensions ,, see TwT at 11:25/21:34')


import pprint
printer= pprint.PrettyPrinter()  #-- Pretty Printer will give us nicer output

example_9g_3D_list = []
l3d = example_9g_3D_list

for a in range(5):              #-- a is outer loop of 3 level nest
    l1 = []
    for b in range(5):          #-- b is first inner loop of 3 level nest
        l2 = []
        for c in range(5):      #-- c is most inner loop of 3 level nest
            l2.append(c)        #-- generate a c level list
        l1.append(l2)           #-- generate a b level list
    l3d.append(l1)              #-- generate the a level list by appendng the b level lists

printer.pprint(example_9g_3D_list)
print(f'\n\n')

## (9g')                 --- at 11:40/21:34       -- Nested comprehensions
print(f'(9g\') Example of Nested Comprehensions ,, see TwT at 12:44/21:34 https://youtu.be/twxE0dEp3qQ?t=764')
example_9g_3D_list = []
l3d = example_9g_3D_list

l3d = [[[data_item for data_item in range(5)] for l2 in range(5)] for l1 in range(5)]
# ----^^^--  Important: Note the 3 square brackets, making data_item the inner most list
# --^^^-- l1 is rows (5 of them), l2 is columns (5 of them), data_item (of use annonymous _) is depth layers (5 of them)
# --^^^-- See TwT at 14:25/21:34 = https://youtu.be/twxE0dEp3qQ?t=866

printer.pprint(l3d)
print(f'(9g\')\t\t--^^^-- above is output of triple for-loop comprehension with 3 brackets up front')

## (9h)                 --- at 14:57/21:34 ot TwT       -- Function call inside comprehension definition
print(f'\n\n(9h) Example of {v.yy_}FUNCTION CALLS INSIDE Comprehension{v.z_} ,, see TwT at 14:57/21:34')

def exponent(x, power=2):
    return x**power

def valid (x):      #-- a dummy argument validity testing function
    return True

x2_power_of_2 = [exponent(x, 2) for x in range(10) if valid(x) == 1]
x2_power_of_3 = [exponent(x, 3) for x in range(10) if valid(x) == 1]

print(f'{x2_power_of_2}')
print(f'{x2_power_of_3}')
print(f'\n(9hg\')\t\t--^^^-- above is output of function calls in insertion of comprehension and also in backside filter')
print(f'\t\tFirst line is squares, Second line is cubes')

## (9i)                 --- at 14:57/21:34 ot TwT       -- Dictionary gen'ing comprehension
print(f'\n\n(9i) Example of {v.yy_}DICTIONARY Comprehensions{v.z_} ,, see TwT at 15:45/21:34')

list_of_key_val_pairs = [("a", 1), ("b", 2), ("c", 81)]
gend_dict_9i = {k:v for k, v in list_of_key_val_pairs}
#               ^^^ the insertion is in form k:v which is syntax for a key:value dictionary item
#                           ^^^ the two for-loop grabls are from the respective tuples
print(f'(9i)\t\tgenerated_dict_9i = {v.yy_}{gend_dict_9i}{v.z_}\n')

## (9j)                 --- at 16:50/21:34 ot TwT       -- Set gen'ing comprehension
print(f'\n\n(9j) Example of {v.yy_}SET generating Comprehension{v.z_} ,, see TwT at 16:50/21:34')

nums_list = [1, 2, 2, 3,3,3, 4,4,4,4]
unique_squares = {x**2 for x in nums_list}

print(f'(9j)\t\tgenerated_set_of uniques_9j = {v.yy_}{unique_squares}{v.z_}')
print(f'\t\tOriginal list of non-unique input valuse was this: {v.yy_}{nums_list}{v.z_}\n')

## (9k)                 --- at 18:06/21:34 ot TwT       -- GENERATOR comprehension
print(f'\n\n(9j) Example of {v.yy_}GENERATOR Comprehension{v.z_} ,, see TwT at 18:06/21:34')
# https://youtu.be/twxE0dEp3qQ?t=1086

sum_of_squares = sum(x**2 for x in range(21))
example_9k_list_2Bsummed = [x**2 for x in range(21)]

print(f'(9k)\t\tList of squares to be added is this: \n\t{v.yy_}{example_9k_list_2Bsummed}{v.z_}')
print(f'The sum is equal to \n\t{v.yy_}{sum_of_squares}{v.z_}\n')

print(f'TO BE CONTINUED .... \n\n')
breakpoint()