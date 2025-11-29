#print(f'Date: 10/16_M2/2025   current editing line = search for "NEW"  =fatten() function')

print(f'(3) The importation of Package_03 / funcs_01 into memory has begun')
# check out the Data Engineer: https://www.youtube.com/@GambillDataEngineering

from . import vars_01 as v  #-- google "python syntax of an import from statement"
from . import mssgs_01 as msg
import keyboard
import pyautogui as gu
import webbrowser
import pyshorteners
'''
Although the MAIN module imports all the necessary module codes, this module must import the name-space aspects
of those modules, namely, those of the vars_01 module plus those of the mssgs_01 module 
'''

# Use in PyCharm: Ctrl + Shft + x to insert hash tag (#) and advance to next line (was used immediately below)
# ----------------------------------------------



def clear_d_screen(lines: int = 30):         #-- use os.clr and skip instead
    print('\n'*lines)
    gu.moveTo(200,600)
    return

def skip(n=2):        #skip this many lines
    print('\n'*n)
    return

#def gen_short_url(url: str = 'https://www.yahoo.com', text: str = '(here)', parameters: dict = None) -> str:
#    if text is None:
#        text = url
#    if parameters is None:
#        parameters = {}
#    kvs = ":".join("{}={}".format(k, v) for k, v in parameters.items())
#    template = "\033]8;{};{}\033\\{}\\033]8;;\033\\"
#    result = template.format(parameters, url, text)
#    return result

def gen_short_url(url: str = 'https://www.yahoo.com', preface: str = 'Click here-->', postfix: str = 'for more info') -> str:
    url_shortener = pyshorteners.Shortener()
    short_url = url_shortener.tinyurl.short(url)
    print(preface, short_url, postfix, end=' ')     #-- ender here allows for a postfix number 2
    return short_url        #see https://www.techgeekbuzz.com/blog/how-to-make-a-url-shortener-in-python/

##NEW
def strip_outr_bracks(nested_list):
    for sub in nested_list:
        print(f'{sub} ___ ', end="")
        print(f'\n')

def strip_inner_bracks(nested_list):
    for sub in nested_list:
        for element in sub:
            print(f'{element}, ', end="")
    print(f'\n')


def fatten(skinny, eps = 25):   #-- skinny= flat list, eps= elements per full sub-list, returns fat list
    l = len(skinny)             #-- number of elements in the input flat list
    r= len(skinny) % eps        #-- number of elements in the last, leftovers sublist
    num_fulls = int(l / eps)  # -- number of full sub-strings, each having len() equal to eps
    #n = num_fulls
    # -- see https://www.w3schools.com/python/ref_func_int.asp TRy_it= REPL
    if l <= eps:
        return skinny           #-- skinny cannot be fattened, so return it as is
    #fat = []                   #-- start it as empty, the sublists will be appended with extend()

    #  [123 ...25] [26 ... 50] [51 ...75] ... [ ... N*eps] --picture if index starts as 1
    #  [012 ...24] [25 ... 49] [50 ...74] ... [ ... (N*eps-1)] --picture if index starts as 0
    #  [012 ...((N=1)*eps-1)] [25 ... ((N=2)*eps-1)] [50 ...((N=3)*eps-1)] ... [ ... (N*eps-1)] --picture if index starts as 0
    #fat = [sub for i in range(num_fulls)]   ###- replace sub with a comprehension TO BE CONTINUED
    fat = [[skinny[(n*eps):(n+1)*eps]] for n in range(num_fulls)]
    if r != 0:                  # is there a non-full remainder?
        print(f'{r}')
        pos_idx = l-r           #positive index is equal to length minus remainder
        remain = skinny[pos_idx::]         # this walks forward to the end inclusive
        #remain_revd = skinny[-1:-int(r+1):-1]   # start at last element [-1] and walk backwards to include [-r]
        #remain =remain_revd[::-1]               # reverse the backward walk
        fat.append([remain])                ##-- I don't undestand why I have to put remainder in sq brackets ???
    return fat


def add_alpha_enum(list, start='a'):  #enumerate a list with alpahebetic sequence
    ascii_numbered_tuples = enumerate(list, ord(start))
    print(f'Below for debug are the ascii enumerate tuples\n\t')
    for i, phrase in enumerate(list, ord(start)):
        print(f'Index: {i}, Phrase: {phrase}')
    print('\n\n')
    for i, phrase in enumerate(list, ord(start)):
        print(f'({chr(i)}) {phrase}')
    #see https://www.geeksforgeeks.org/python/enumerate-in-python/
    temp_lst1 = [f'({chr(i)}) {phrase}' for i, phrase in enumerate(list, ord(start))]
    print('\n\t',temp_lst1)
    print(f'--^^^-- Abve was generated with a list comprehension: \n')
    print(f"temp_lst1 = [f\'({chr(i)}) {phrase}\' for i, phrase in enumerate(list, ord(start))]\n")
    for item in temp_lst1:
        print(item)
    return ascii_numbered_tuples

def ascii_fm_az(fm2: str = 'A-Z'):  #cap alpha's have the smaller ANSI code values than lower case
    lo_hi = fm2.split(sep ='-') #get from and to chars
    lo = lo_hi[0]; lo_ascii = ord(lo)
    hi = lo_hi[1]; hi_ascii = ord(hi)
    #print(f'debug check list = {ascii_fm_az()}')  # -- verify that list contains ascii low and hi values
    return [lo_ascii-1, hi_ascii+1]
# --^^-- notes re above func
#--^^^-- usage below
# l_01 = ascii_fm_az('a-z') # returns a list of integers, the ANSI codes
# ord returns the ascii or unicode of a string char, See:
# https://www.geeksforgeeks.org/dsa/ascii-table/
# https://symbl.cc/en/unicode-table/#block-elements

def ascii_2_str (ask = 65):
    return chr(ask)     #--^^-- use this to iterate and concatenate to varaible name
#--^^-- chr() returns the string char of a supplied unicode

def test_iterate(lo, hi):   #use this vvv to validate the while loop outputs
    ask_value = ascii_fm_az(lo, hi)[0]  #-- start at the lower ascii code (minus 1)
    while ask_value < ascii_fm_az(lo, hi)[1]:
        ask_value += 1
        print(ascii_2_str(ask_value))   #--check that we iterate from 'A' to 'Z'
    return

def get_dict(dict_name = 'clr'): #-- input a string, returns a named dictionary
    clr: dict = {'b': "BLACK", 'r': "RED", 'g': "GREEN", 'y': "YELLOW", 'u': "BLUE", 'm': "MAGENTA", 'c': "CYAN",
                 'w': "WHITE",
                 'o': "RESET",
                 'B': "LIGHTBLACK_EX", 'R': "LIGHTRED_EX", 'G': "LIGHTGREEN_EX", 'Y': "LIGHTYELLOW_EX",
                 'U': "LIGHTBLUE_EX",
                 'M': "LIGHTMAGENTA_EX", 'C': "LIGHTCYAN_EX", 'W': "LIGHTWHITE_EX",
                 'D': "DIM", 'N': "NORMAL", 'H': "BRIGHT", 'O': "RESET_ALL"}

    clr_: dict = {'W_': 'HWb', 'M_': 'Hmb', 'C_': 'DCb', 'R_': 'HRb',
                  'Y_': 'HYb'}  # -- under score for 3 char expansions
    if dict_name == 'clr':
        f_out = clr
    elif dict_name == 'clr_':
        f_out = clr_
    return f_out  # --^^-- above func returns the whole of the dictionary; better idea= use a list or dictionary of dictionaries

def get_dict_expansion(dict_name='clr', alias = 'W_'): #-- Reverse alias is the longer equivalent of input alias string
    #clr: dict = {'b':"BLACK", 'r':"RED", 'g':"GREEN", 'y':"YELLOW", 'u':"BLUE", 'm':"MAGENTA", 'c':"CYAN", 'w':"WHITE",
#                 'o':"RESET",
#                 'B':"LIGHTBLACK_EX", 'R':"LIGHTRED_EX", 'G':"LIGHTGREEN_EX", 'Y':"LIGHTYELLOW_EX", 'U':"LIGHTBLUE_EX",
#                 'M':"LIGHTMAGENTA_EX", 'C':"LIGHTCYAN_EX", 'W':"LIGHTWHITE_EX",
#                 'D':"DIM", 'N':"NORMAL", 'H':"BRIGHT", 'O':"RESET_ALL"}
    #^^ in above, single letter will rep Fore color alone, 2 chars will rep Fore + Back,
    #^^ 3 chars will rep Style + Fore + Back in that order
    clr: dict = v.Ansii()
    clr_: dict = {'W_':'HWb', 'M_': 'Hmb', 'C_':'DCb', 'R_':'HRb', 'Y_':'HYb'}  #-- under score for 3 char expansions
    if dict_name == 'clr':
        f_out = clr[alias]
    elif dict_name == 'clr_':
        f_out = clr_[alias]
    return f_out    #-- func returns expansion from named dictionary

def qif_inStr_OK(inStr, slices_list= [0, 1, 2], allowed= 'yYesnNo'):
    #--^^^-- Query if the input string chars are in the allowed_chars_string
    for s in slices_list:
        if inStr[s] in allowed:
            continue
        else:
            print(f'Bad character {inStr[s]} found in supplied input by qif')
            return False
    return True  #--if no misallowed detected, then return as true, meaning allowed

#--vv-- Below 'sl' funcs generate the poor man's GUI box (filler can be a box dwg code)
#--vv-- 'slm()' is the one that prints lines in the middle of the GUI box
def sl3(filler="*", times=90):   #-- separation line w \n above and an extra one below
    d = get_dict('clr_')
    outp: str = v.W_ + filler * times
    print('\n', outp, '\n')
    return None
#sl = sl3('🤪')   #-- https://copychar.cc

def sl2(filler="*", times=90):   #-- bottom separation line w extra \n below
    d = get_dict('clr_')
    outp: str = v.W_ + filler * times
    print(outp, '\n')
    return None

def sl1(box_id ='(__)', filler="*", times=90):   #-- top separation line w \n above
    d = get_dict('clr_')
    outp: str = f"\n{v.W_}{box_id}{filler * (times-4)}"
    print(outp)
    return None

def sl0(filler="*", times=40):   #-- separation line w no CRLF
    d = get_dict('clr_')
    outp: str = v.W_ + filler * times
    print(outp, end='')
    return None

def slm(mssg="MID MESSAGE GOES HERE", filler="**", width= 115-4):   #-- mid box messages
    d = get_dict('clr_')
    centr_fill=" "
    outpmid: str = f"{filler}{mssg.center(width, centr_fill)}{filler}"
    print(outpmid)
    return None

def outp_centrd_mssgs(mssg_type= 'intro_', frame_id= '00', lo_hi_range= 'A-Z'):
    mssg_id_prefix = mssg_type + frame_id
    #--^^^-- the message name is a concat of prefix plus an alpha char
    #--vvv-- set up to iterate thru to-be centred messages, the lo_hi_range is a string
    lo_hi = lo_hi_range.split(sep='-')  # get from and to chars & convert them to unicode integers
    lo = lo_hi[0]; lo_ascii: int = ord(lo)
    hi = lo_hi[1]; hi_ascii: int = ord(hi)
    mssg_id_i = lo_ascii - 1
    while mssg_id_i < hi_ascii + 1:     ### coding NOTE: put mssg_id_txt inside an exec() code string !!!!!
        mssg_id_i += 1
        mssg_id_txt = mssg_id_prefix + chr(mssg_id_i)   #-- iterate from a to z (or other lo to hi)
        gotten_mssg = getattr(msg, mssg_id_txt )
        outp_mssg_i: str = f'{gotten_mssg.center(120)}'
        print(outp_mssg_i)
        #exec(outp_mssg_i)   #-- THIS DIDN'T WORK
    return

def outp_in_list(list_name = 'intro_00_in_list', colors = 'GREEN', indent=10, spc=' '):
    for item in msg.getattr(list_name):
        gotten_mssg = getattr(msg, item)
        print(f'{v.Ansii[colors]}{spc:<10}{gotten_mssg}')       #-- note colon between spc and indent amount
    #print(f'{x4}\nend of for loop hit <--a debug notification\n')
    return

def outp_in_mssgs(mssg_type= 'intro_', frame_id= '00', lo_hi_range= 'A-Z'):
    spc = ' '
    mssg_id_prefix = mssg_type + frame_id
    #--^^^-- the message name is a concat of prefix plus an alpha char (cap A-Z is lower ascii than a-z)
    #--vvv-- set up to iterate thru to-be INDENTED messages, the lo_hi_range is a string
    lo_hi = lo_hi_range.split(sep='-')  # get from and to chars & convert them to unicode integers
    lo = lo_hi[0]; lo_ascii: int = ord(lo)
    hi = lo_hi[1]; hi_ascii: int = ord(hi)
    mssg_id_i = lo_ascii - 1
    while mssg_id_i <= hi_ascii-1:     ### coding NOTE: terminater at -1 because ID is inc'ed in next step !!!!!
        mssg_id_i += 1
        mssg_id_txt = mssg_id_prefix + chr(mssg_id_i)   #-- iterate from A to Z (or other lo to hi)
        gotten_mssg = getattr(msg, mssg_id_txt )    #-- HERE is where the mid message is assembled !!!
        outp_mssg_i: str = f'{gotten_mssg}'
        print(f'{spc:<10}{outp_mssg_i}')
    return

def outp_list(list_name = 'intro01_list_A', color = v.C_, indent=10):  ## 157
    for item in msg.getattr(list_name):
        print(f'{v.yy_}{spc:<10}{item}')       #-- note colon between spc and indent amount
    #print(f'{x4}\nend of for loop hit <--a debug notification\n')
    return

def webster_drive(mssg_type= 'URL_web', frame_id= '00', picks= 'A-Z'): ### NEW  !!!!
    spc = ' '
    URL_prefix = mssg_type + frame_id
    #--^^^-- the URL name is a concat of prefix plus an alpha char (must be cap A-Z)
    #--vvv-- set up to iterate thru to-be INDENTED messages, the lo_hi_range is a string
    lo_hi = lo_hi_range.split(sep='-')  # get from and to chars & convert them to unicode integers
    lo = lo_hi[0]; lo_ascii: int = ord(lo)
    hi = lo_hi[1]; hi_ascii: int = ord(hi)
    url_id_i = lo_ascii - 1
    while url_id_i <= hi_ascii-1:     ### coding NOTE: terminater at -1 because ID is inc'ed in next step !!!!!
        url_id_i += 1
        url_id_txt = url_id_prefix + chr(url_id_i)   #-- iterate from A to Z (or other lo to hi)
        gotten_url = getattr(msg, url_id_txt )    #-- HERE is where the mid message is assembled !!!
        outp_url_i: str = f'{gotten_url}'
        webbrowser.open(outp_url_i)
    return


def wait_4c_key(display_id = '(001)', allowed_01 = f'"c" or "SPACE"', allowed_02 = f' "m" '):
    intro_01x: str = (f'Hit {v.g_}{allowed_01}{v.z_} to continue to next learning frame, '
                      f'or Hit {v.g_}{allowed_02}{v.z_} to Explore More')
    outp_01x: str = f'{v.R_}next = {display_id}--> {intro_01x.center(90)}';
    print('\033[A\r', outp_01x, sep='', end='')
    reponse= 'xxx'
    wait_01 = True
    while wait_01 == True:
        #keyrd = keyboard.read_key()  # -- do TWO ??? read opertions in outer while loop
        #keyrd = keyboard.read_key()  #--^^-- for debouncing the key?
        keyrd = keyboard.read_event(suppress= True)
        keyrd = keyboard.read_event(suppress=True)
        keyrd = keyrd.name.lower()
        if keyrd == "c":  # if the "c" key is pressed
            wait_01 == False;
            response = 'c'
            # print('You Pressed the "c" key --this is a debug notification')
            break

        elif keyrd == "space":  # if the "space" key is pressed
            wait_01 == False;
            response = ' '
            # print(f'\nYou Pressed the "SPACE" key --this is a debug notification')
            break
        elif keyrd == "m":  # if the "m" key is pressed
            wait_01 == False;
            response = 'm'
            # print(f'\nYou Pressed the "m" key --this is a debug notification')
            break
        else:
            continue
    return response

def next_frame(display_id = '(00)'): ##169
    intro_01x: str = 'Hit "c" or "SPACE" to continue to next learning frame'
    intro_01y: str = 'Hit "m" to open browser to show more information re this frame'
    outp_01x: str = f'{v.R_}{display_id}: {intro_01x.center(90)}'; print(outp_01x)
    outp_01y: str = f'{v.Y_}{intro_01y.center(90)}'; print(outp_01y)
    wait_01 = True
    while wait_01 == True:
        keyrd = keyboard.read_key()  # -- do just one read opertion per while loop
        if keyrd == "c":  # if the "c" key is pressed
            wait_01 == False;
            response = 'c'
            # print('You Pressed the "c" key --this is a debug notification')
            break
        elif keyrd == "space":  # if the "space" key is pressed
            wait_01 == False;
            response = ' '
            # print(f'\nYou Pressed the "SPACE" key --this is a debug notification')
            break
        elif keyrd == "x":  # if the "x" key is pressed
            wait_01 == False;
            response = 'x'
            # print(f'\nYou Pressed the "x" key --this is a debug notification')
            break
        elif keyrd == "m":  # if the "m" key is pressed
            wait_01 == False;
            response = 'm'
            # print(f'\nYou Pressed the "m" key --this is a debug notification')
            break
        else:
            continue
    return response

def brk(mssg):      ##195
    print(f'\n(X): A debug {v.Y_}brk(mssg) point{v.W_} was hit at {v.G_}line '
          f'{gotten_line_numb_2back()}{v.W_}')
    print(f'(Y): Pdb debugger commands: l=LIST, c=CONTINUE, pp var= PrettyPrint the specific var')
    print(f'(Z): Additional message: {mssg}\n')
    breakpoint()

def get_line_numb_info_demo():      ##202
    frame_current = inspect.currentframe()
    frame_info_prior = inspect.getframeinfo(frame_current.f_back)   #--don't get from execution of this func, get from caller
    frame_info_current = inspect.getframeinfo(frame_current)
    sl3()

    print(f'(a): ',f'current= {frame_info_current}', f'Using the Inspect module we can learn the line number in the caller"s code\n\t',
          f'At current execution time it is \tLine Number {frame_info_prior.lineno}')
    print(f'(b): We can also get the file path + name out of the frame info tuple, it is: \n\t {frame_info_current.filename}')
    print(f'(c): We can also get the name of the function we are inside, at moment we get: \t{frame_info_current.function}')
    return

def gotten_line_numb_1back():  ##214
    frame_current = inspect.currentframe()
    frame_info_prior = inspect.getframeinfo(frame_current.f_back)   #--don't get from execution of this func, get from caller
    frame_info_current = inspect.getframeinfo(frame_current)
    return f'{frame_info_prior.lineno}'

def gotten_line_numb_2back():   ##220 #-- not finished see stack inspect 2 back !!!!
    frame_current = inspect.currentframe()
    frame_info_2priors_back  = sys._getframe(2)   #--get frame info from caller's caller
    frame_info_current = inspect.getframeinfo(frame_current)
    return f'{frame_info_2priors_back.f_lineno}'    #--Google "python inspect two frames back"

def halt2_study(maybe, feature):    ##226
    if (maybe.lower() == 'n' or maybe.lower() == 'no' or maybe.lower() == 'not'):
        return
    else:
        print(f'The above ^^^^ printouts executed above {v.G_}line {gotten_line_numb_2back()}{v.W_} demonstrate exercise of {v.Y_}{feature}{v.W_} methods')
        wait = input('<Enter> to continue to next demonstartion\n')
    return

def gen_index_templ4(numb_indices):     ##234 --a func that prints out a template of input number of indices plus one
    skip_diz_template_create = range(numb_indices + 1)
    skip_diz_template = list(skip_diz_template_create)
    print(f'{v.G_}', end = '')
    for i in skip_diz_template: print(format(i ,"02d"), end = '__')  #-- apply the format() function one int at a time
    print(f'{v.W_}')
    print(f'\n{v.M_}Template printed out above for {numb_indices} plus one indices{v.W_}\n')

def gen_preFilled_list4(numb_indices, filler = 0):   ##242 #--func prints out a list of arg1 number of indices plus one
    skip_diz_template_A = [filler] * (numb_indices +1)    #-- and returns the gen'd list filled with the filler
    for i in skip_diz_template_A: print(format(i ,"02d"), end = ' ')  #-- no CRLF
    print(f'\nPre-filled list is printed above for {numb_indices} plus one indices\n')
    return skip_diz_template_A

def halt4_ideas(halt4_IDs_params):      ##248
    p = halt4_IDs_params         #-- shallow assign creates a shorter var name for the input dictionary
    original = p['tute_input_var1']     #-- get the original list example
    result = p['tute_output1']
    esc = '\033['; wht_text = esc + '37m'; yel_text = esc + '33m'; red_text = esc + '31m'  #-- import colorama
    print(f'\n#0{p['tute_ID']}: Output of {p['tute_name']} {p['tute_actions']} to produce \t{p['tute_output1']}')
    print(f' \t\t\t\t original input was = \t\t{original}\n')
    print(f'{yel_text}FOOD FOR THOUGHT: ({v.G_}Halted at {gotten_line_numb_2back()}{v.W_}) '
          f'What other applications can {p['tute_name']} be used for?{wht_text}')
    print(f'(1): {p['tute_name']} used for {p['tute_actions']} {p['tute_suggest1']} ____ in context of ____')
    print(f'(2): {p['tute_name']} used for {p['tute_actions']} {p['tute_suggest2']}____ in context of ____')
    print(f'(3):', end= " ")
    halt_02 = input(f'Do you have any more application ideas for {red_text}{p['tute_name']}{wht_text} ??__\n'
                    f'type xx to exit\n')
    idea_numb = 1
    now: datetime = datetime.now()  # <-- set this (hinted at) object to current time
    file_base_path4 = 'C:/Users/gideon/Python_Projects_A0/Project_A01_PyBasics_2/.venv/'  # --absolute PATH to THE Venv folder
    Title = f'Test Run for saving numbered ideas of more uses of {p['tute_name']}'
    file_w_path4 = file_base_path4 + f'{now: %Y~m%m~d%d}.txt'   #--file name follows my Obsidian notes

    try:  # -- This "try BLOCK" is used to cope with exceptions like a FileExistsError
        with open(file=file_w_path4, mode="wt") as file:  # --"w" for initial write mode
            file.write(f'{Title}' + f'{now: %Y~m%m~d%d:} for example Obsidian Note \r\n')
            file.write(f'({idea_numb}) {halt_02}\n')  #<--- save idea 01 into the file
    except FileExistsError:
        print(f'That file already exists in the target folder as {file_w_path4}')

# repeat for more ideas in below while loop  which is still part of the func VVVVVVV

    while halt_02 != 'xx':
        idea_numb += 1
        file_base_path4 = 'C:/Users/gideon/Python_Projects_A0/Project_A01_PyBasics_2/.venv/'
        Title = f'Save user input for idea number {idea_numb}'
        file_w_path4 = file_base_path4 + f'{now: %Y~m%m~d%d}.txt'

        try:  # -- This "try BLOCK" is used to cope with exceptions like a FileExistsError
            with open(file=file_w_path4, mode="a") as file:  # --"a" is append
                file.write(f'{Title}' + f'{now: %Y~m%m~d%d:} for Obsidian Note \r\n')
                file.write(f'({idea_numb}): {halt_02}\n')
        except FileExistsError:
            print(f'That file already exists on the deskto as {file_w_path4}')

        halt_02 = input(f'Do you have any more application ideas for use of {red_text}{p['tute_name']}{wht_text} ??__\n'
                        f'type xx to exit\n')


def choice_of_die_outcomes(method_ID_numb, method_name, verb, skip_diz_list_a): ##416    #-- last arg is a skip control
    if skip_diz_list_a[method_ID_numb] == 1:
        print(f'method number {method_ID_numb} has been skipped\n')
        return None                               #--skip this tutorial if skip position for tutorial 01 is set to 1
    face_imgs_row1 = ['🤬', '🧐', '🤓🤓', '😲😲', '🤩🤩', '😋   🤪',   '🤠🤠🤠' ]
    face_imgs_row2 = ['☠️', ' ',   '  ',   '😲',    '🤩🤩', '😋😛🤪',   '🤠🤠🤠' ]
    print('\n\n', '#' * 20)

    dice_faces: int = range(1,7)    #-- generates a sequence (not list) of integers 1-6 (default start of range is 0)
    go_again = 'y'
    while go_again == 'y':
        roll_1 = choice(dice_faces)
        roll_2 = choice(dice_faces)
        print(f'\n#:00; example of random choice made with the CHOICE() function')
        print(f' 1st die roll gives you a \t{roll_1}\t{face_imgs_row1[roll_1]}')
        print(f' \t\t\t\t\t\t\t\t{face_imgs_row2[roll_1]}\n')
        print(f' 2nd die roll gives you a \t{roll_2}\t{face_imgs_row1[roll_2]}')
        print(f' \t\t\t\t\t\t\t\t{face_imgs_row2[roll_2]}\n')
        print(f' The SUM of the two rolls is \t{roll_1 + roll_2} \n')
        go_again = input('Try again? Enter y or other here__')

# Indently's code for printing out all the methods is as follows
def gen_list_of_methods(): ##499
    i: int =0
    for method in dir(list):    #<-- how do we set the path for directory? Don't have to. We're executing inside Py!
        i += 1
        print(i, method, sep=': ')
        if i > 100:
            break
        else:
            pass
    return

#print(f'import of funcs has finished')

# CODE DISCARD ZONE **************************************************************** vvvvvvv
#print(f'importation of funcs is about to hit the cj() func')
# NO LONGER USING COLORAMA !!!!
#def cj(chars: str = 'HWb', dict_name = 'clr'):     #-- COLORAMA color commands generator using the clr dictionary
#    numb = len(chars)
#    allowed_4_Fore = 'brgyumcwoBRGYUMCW'
#    allowed_4_Style = 'DNHO'
#    dict = get_dict(dict_name) #--using above function for picking one of n dictionaries
#
#    if numb < 1:
#        print(f'argument error in cj function call')
#        return None
#
#    elif numb < 2:
#        if qif_inStr_OK(chars, [0], allowed_4_Fore):  #-- check for valid input String
#            pass
#        else:
#            print(f'qif_inStr_OK found a bad input char at below breakpoint')
#            breakpoint()
#            return None
#        sum: str = getattr(Fore, d[f'{chars[0]}'])    #-- if one char it is FORE color
#        return sum
#
#    elif numb < 3:
#        if qif_inStr_OK(chars, [0, 1], allowed_4_Fore):  #-- check for valid input String
#            pass
#        else:
#            print(f'Bad character in inputs to cj()')
#            return None
#        #sum: str = getattr(Fore, d[f'{chars[0]}'])  + getattr(Back, d[f'{chars[1]}']) # -- if 2 chars
#        return #sum
#
#    elif numb < 4:
#        if qif_inStr_OK(chars, [1, 2], allowed_4_Fore):
#            pass
#        elif qif_inStr_OK(chars, [0], allowed_4_Style):
#            pass
#        else:
#            print(f'Bad character in inputs to cj() found by qif at numb=3')
#            return "error in numb=3"
#        #sum: str = getattr(Style, d[f'{chars[0]}'])  + getattr(Fore, d[f'{chars[1]}'])  + getattr(Back, d[f'{chars[2]}']) # -- if 3
#        return #sum
#    else:
#        print(f'arguments error in cj function call')
#        return None
#

#--vv-- next are repeated char printouts for creating title boxes (sl= single line of filler char)