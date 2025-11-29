#print(f'Date: 10/27_E1/2025   current editing line = search for "NEW"  = get_keystroke() function')

print(f'(3) The importation of Package_03 / funcs_02 into memory has begun')
# check out the Data Engineer: https://www.youtube.com/@GambillDataEngineering
# see #NEW this page: https://oldmanlearningsupport.blogspot.com/2025/10/argslist-of-parameter-passing.html

from . import vars_01 as v  #-- google "python syntax of an import from statement"
from . import mssgs_01 as msg
import keyboard
import pyautogui as gu
import webbrowser
import pyshorteners

from . import vars_01 as v  #-- google "python syntax of an import from statement"
from . import mssgs_01 as msg
from . import funcs_01 as fn

'''
Although the MAIN module imports all the necessary module codes, this module must import the name-space aspects
of those modules, namely, those of the vars_01 module plus those of the mssgs_01 module 
'''

# Use in PyCharm: Ctrl + Shft + x to insert hash tag (#) and advance to next line (was used immediately below)
# ----------------------------------------------

def get_keystroke():
    key_read = ''
    keyrd = keyboard.read_event(suppress = True)
    keyrd = keyboard.read_event(suppress=True)
    key_read = key_read.join(keyrd.name.lower())
    return key_read

def get_allowed_keystroke(allowed: str = ''.join(chr(i) for i in range(ord('A'), ord('z') + 1))):
    '''
    This function waits for a key hit (e.g. A-Z and a-z)
    :param allowed: is a string of the allowed alpha characters
    see https://www.geeksforgeeks.org/python/alphabet-range-in-python/ w respect to 'a-z'
    :return: the key stroke if allowed, other wise type Try Again
    '''

    valid_hit = False
    while valid_hit == False:
        keyrd = keyboard.read_event(suppress = True)
        keyrd = keyboard.read_event(suppress=True)
        key_read = keyrd.name
        if key_read in allowed:
            valid_hit = True
            break
        else:
            valid_hit = False
            print(f'{v.r_}The typed key, {v.yy_}{key_read}{v.r_} is not valid. Try again{v.z_}')
    return key_read


def enum_var_methods_dict(var= str):
    ''' The built-in dir(object) function generates a list of methods recognized by the specified object.
    The present enumerating function (above, named "enum_var_methods_dict" associates a method number (1-47 for string methods)
        with each found method and appends them into a dictionary ("var_meths_dict"), the number being the key of
        the KV pair and the method name being the 'value'. It also generates a reverse dictionary and RETURNS both dicts in a tuple.
        Additionally, it prints the KV pairs as a tabular list, where "n_cols" is the number of columns, "w_pCol" is the width of
        each column and "var" is the ID of the object. We use modulo math (%) to determine when to include a CRLF. '''

    stepper: int = 1;   #-- steps through the columns of each row by incrementing +1
    n_cols =3           #-- number of printed out columns
    w_pCol = 70         #-- width per column
    var_meths_dict = {}    #<-- start with an empty dictionary and add each found to it
    reverse_var_dict = {}
    print(f'\t\tBelow is a listing of methods for the data type: {var}\n')

    for found_method in dir(var):
        if '__' not in found_method:        #<-- leave out the Dunder methods
            key = 'var_meth_#' + str(stepper)
            var_meths_dict[key] = found_method   # goggle "python add kv pair to dict"
            reverse_var_dict[found_method] = key
            outp_str = f'>> {key} : {v.yy_}{found_method}{v.z_}'
            if stepper % n_cols != 0:
                print(f'{outp_str:<{w_pCol}}', end="")  #<-- a colon plus space is inserted as separator for each item
            else:
                print(f'{outp_str}')

            stepper += 1
    return var_meths_dict, reverse_var_dict

cols= 3 #-- numb of columns in the "what next" options table
rows = 2
opts_dict = {'g': 'G= Google search', 'u': 'U= YouTube search', 'o': 'O= Old Man Back page', 'x': 'X=Jump to next study frame',
             'a' : 'A= To be determined', 'b': 'B= To be determined'}
opts_keys = {'0' : 'g', '1' : 'u', '2' : 'o', '3': 'x', '4': 'a', '5': 'b'}

def gen_options_table(cols, rows, opts_dict, opts_keys):
    col_width = int(120/cols)
    for c in range(0,(cols*rows)):
        cc = str(c)
        outp_key =  opts_keys[cc]
        outp = opts_dict[outp_key]
        outp_1 = outp.center(col_width,'.')
        outp_2 = outp_1.center(col_width,':')

        if int((c+1)%cols) != 0:
            print('▉', outp.center(col_width,' '), end="")
        else:
            print('▉', outp.center(col_width,' '), '▉')
    return

n=1 #-- this declaration needed for below --vvv-- function

samp_1 = 'the quick Brown fox Beat the slow turtle.'
samp_2 = 'every Good Boy Deserves Favor'
samp_3 = 'what goes UP Must Come down. HELLO WORLD'

opts_dict = {'g': 'G= Google search', 'u': 'U= YouTube search', 'o': 'O= Old Man Back page', 'x': 'X=Jump to next study frame',
             'a' : 'A= To be determined', 'b': 'B= To be determined'}
opts_keys = {'0' : 'g', '1' : 'u', '2' : 'o', '3': 'x', '4': 'a', '5': 'b'}

Args_lst = []   #--start w empty list and add necessary dictionaries, e.g. the study_calls one below --vvv--
study_calls = {'Calld_by' : 'f2.study.1001',
            "Read_Me.html" : "https://oldmanlearningsupport.blogspot.com/2025/10/argslist-of-parameter-passing.html",
            'subject' : 'String Methods',
            'sMethod' : 'capitalize',
            'meth_ID' : 1, 'Calld_id' : '1001',
            'numb_of_samps' : 3,
            'samps' : [samp_1, samp_2, samp_3]}
option_calls = {'Calld_by' : 'f2.gen_options_table.1001',
            "Read_Me.html" : "https://oldmanlearningsupport.blogspot.com/2025/10/argslist-of-parameter-passing.html",
            'cols' : 3, 'rows' : 2,
            'fwd_dict': opts_dict,
            'rev_dict' : opts_keys}

#Args_lst.join(study_calls)
#Args_lst.join(option_calls)
# def study(Args_lst):

def study(*samps, subject = 'String Methods', sMethod = 'capitalize', meth_ID= n):

    #Replace above set of parameters with a compiled list of parameter-passing dictionaries
    #and then unpack at least the first dictionary here (pop it off the listing)
    sMethod_ = sMethod + '()'
    '''
    The Args_lst listing of parameter dictionaries
    Not all functions will need such a registry of parameter transfers
    However the current "study" function can have a large list of arguments/ parameters by itself and then the
    inside called function, gen_options_table, will also have a long list
    Each Parameter Dictionary in the Args_lst list will include at least a first key of type string and named "Calld_by"
    and whose KV value mate will be another string have the form: "module.func_name.params_id" where module is the name of
    the module in which the current function resides (e.g. fn, f2, f3, etc.) and func_name is tested to make sure it 
    matches the name of the current function    while params_id is a unique number (say, based on date) assigned to the
    assemblage of parameters further stored inside the Args_lst listing.
    Ideally, each Parameter Dictionary in the Args_lst list will include a second key of type string and named "Read_Me.html"
    and whose KV value mate will be and HTML address to a read me posting on the web, for example inside my Old Man Back Pages
    blog. For example, this:
    https://oldmanlearningsupport.blogspot.com/2025/10/argslist-of-parameter-passing.html
    '''

    print(f'\t\t\t\t\t\tFIRST, we are studying {v.yy_}{subject.upper()}{v.z_}\n\n')
    print(f'({n})\t\tBelow example shows the {v.yy_}{sMethod_} method{v.z_} applied to a set of input string samples\n\n')
    for samp in samps:
        print(f'The input string sample is this:\n\t\t{v.yy_}{samp}{v.z_}')
        samp_dot_attr = getattr(samp, sMethod, None)
        #Note the addition of parens to samp_dot_attr in the line below !!!!
        print(f'The resulting output of applying the {sMethod_} method is this:\n\t\t{v.g_}{samp_dot_attr()}{v.z_}')
    print(f'Note that only the first letter has been capitalized irrespective of punctuation\n')
    print(f'What are some practical uses for the {sMethod_} function of python?\n')

    q_Google_1 = f'What are some practical uses for the {sMethod_} function of Python?'
    # q_Google_2 = f'Using the pyperclip module of Python'
    # q_Google_3 = f'Using the {sMethod} method of Python'

    q_W3School_1 = f'https://www.w3schools.com/python/ref_string_{sMethod}.asp'

    url_tail1 = f'/search?q={q_Google_1}'
    url_full = f'https://www.google.com' + url_tail1

    ##New
    #cols = 3  # -- numb of columns in the "what next" options table
    #rows = 2
    #opts_dict = {'g': 'Google search', 'u': 'YouTube search', 'o': 'Old Man Back page', 'x': 'Jump to next study frame'}
    #opts_keys = {'0': 'g', '1': 'u', '2': 'o', '3': 'x'}

    gen_options_table(cols, rows, opts_dict, opts_keys)
    print(f'\n\nEnter a valid 1-Hit key stroke')
    test_01 = get_allowed_keystroke()
    print(f'This is a test of the keystroke function in f2. Hit key name = {test_01}')

    '''
    reponse1 = input(f'Would you like to dig deeper via Google? (y/n)\n')

    if reponse1 == 'y':
        print(f'{v.M_}Get a Notebook and take Handwritten Notes !!!{v.z_}')
        webbrowser.open(url_full)
        print(f'LOOK inside the browser for {v.yy_}New TAB (Google result) for {sMethod_}', '-=' * 20, f'>{v.z_}')
    fn.skip()
    reponse2 = input(f'Would you like to dig deeper via W3 Schools? (y/n)\n')
    if reponse2 == 'y':
        print(f'{v.r_}Get a Notebook and take Handwritten Notes !!!{v.z_}')
        webbrowser.open(q_W3School_1)
        print(f'LOOK inside the browser for {v.yy_}New TAB (W3 Schools result) for {sMethod_}', '-=' * 20, f'>{v.z_}')
    fn.skip()
    '''
    return None

