# Date:  8/03/2025  Primary varaible values for Learn_Lists_and_Module_03.py are stored here
# This module will be imported first with the alias, "v" so that variable invocations will be v (dot) something
'''
Ran into a Circular Import problem. So changing the color codes to direct ANSI codes 
and avoiding use of the public COLORAMA module
... more to follow
'''


# print(f'(1) The importation of vars_01 into Main has begun\n')


#-- google "python syntax of an import from statement"
#from . import funcs_01 as fn
#from . import messgs_01 as msg

#--vvv-- below codes are from https://python-forum.io/thread-36511.html
a = Ansi_temp1= "\033[0;"; b = Ansi_temp2= "m"

Ansii: dict = {'BLACK' : "\033[0;30m", 'RED' : "\033[0;31m", 'GREEN' : "\033[0;32m", 'BROWN' : "\033[0;33m",
    'BLUE' : "\033[0;34m", 'PURPLE' : "\033[0;35m", 'CYAN' : "\033[0;36m", 'LIGHT_GRAY' : "\033[0;37m",
    'DARK_GRAY' : "\033[1;30m", 'LIGHT_RED' : "\033[1;31m", 'LIGHT_GREEN' : "\033[1;32m", 'YELLOW' : "\033[1;33m",
    'LIGHT_BLUE' : "\033[1;34m", 'LIGHT_PURPLE' : "\033[1;35m", 'LIGHT_CYAN' : "\033[1;36m", 'LIGHT_WHITE' : "\033[1;37m",
    'BOLD' : "\033[1m", 'FAINT' : "\033[2m", 'ITALIC' : "\033[3m", 'UNDERLINE' : "\033[4m", 'BLINK' : "\033[5m",
    'NEGATIVE' : "\033[7m", 'CROSSED' : "\033[9m", 'END' : "\033[0m"}   #--foreground text color

Ansi_: dict = {'BLACK' : "\033[0;40m", 'RED' : "\033[0;41m", 'GREEN' : "\033[0;42m", 'BROWN' : "\033[0;43m",
    'BLUE' : "\033[0;44m", 'PURPLE' : "\033[0;45m", 'CYAN' : "\033[0;46m", 'LIGHT_GRAY' : "\033[0;47m",
    'DARK_GRAY' : "\033[1;40m", 'LIGHT_RED' : "\033[1;41m", 'LIGHT_GREEN' : "\033[1;42m", 'YELLOW' : "\033[1;43m",
    'LIGHT_BLUE' : "\033[1;44m", 'LIGHT_PURPLE' : "\033[1;45m", 'LIGHT_CYAN' : "\033[1;46m", 'WHITE' : "\033[1;47m"}
##--background text color
## bright text = 90-97, bright back ground = 100-

AnsiiB: dict = {'BLACK' : a+'90'+b, 'RED' : a+'91'+b, 'GREEN' : a+'92'+b, 'BROWN' : a+'93'+b,
    'BLUE' : a+'94'+b, 'PURPLE' : a+'95'+b, 'CYAN' : a+'96'+b, 'LIGHT_GRAY' : a+'97'+b,
    'Default' : a+'99'+b}  #--Bright fore colors

Ansi_B: dict = {'BLACK' : a+'100'+b, 'RED' : a+'101'+b, 'GREEN' : a+'102'+b, 'BROWN' : a+'103'+b,
    'BLUE' : a+'104'+b, 'PURPLE' : a+'105'+b, 'CYAN' : a+'106'+b, 'LIGHT_GRAY' : a+'107'+b,
    'Default' : a+'109'+b}  #--Bright Back colors
x_ = Ansii['LIGHT_WHITE'] + Ansi_['BLACK']
W_ = Ansii['BOLD'] + Ansii['LIGHT_WHITE']  +Ansi_['BLACK'] #HWb
w_ = Ansii['LIGHT_WHITE'] + Ansi_['BLACK']
M_ = Ansii['BOLD'] + Ansii['PURPLE']       +Ansi_['BLACK'] #Hmb
m_ = Ansii['PURPLE'] + Ansi_['BLACK']
C_ = Ansii['FAINT'] + Ansii['CYAN'] +       Ansi_['BLACK'] #DCb
R_ = Ansii['BOLD'] + Ansii['RED'] +         Ansi_['BLACK'] #HRb
Y_ = Ansii['BOLD'] + Ansii['YELLOW'] +      Ansi_['BLACK'] #HYb -- Define aliases for color combos to use inside funcs
G_ = Ansii['BOLD'] + Ansii['GREEN'] +      Ansi_['BLACK']
y_ = Ansii['YELLOW'] + Ansi_['BLACK']
z_ = Ansii['LIGHT_CYAN'] + Ansi_['BLACK']
x2= z_
x3= Y_

#print(f'\n ********** This  is  a debug test in the vars module --line 55 **********\n')
#print(f'Direct refernce to Anssi[colr_name] works but shallow copy does not. Why?\n')
#print(f'{Ansii['YELLOW']}Hello {Ansii['GREEN']}World {Ansii['RED']}in col{Ansii['LIGHT_WHITE']}or\n\n')
yy_ = Ansii['YELLOW']; g_ = Ansii['GREEN']; r_ = Ansii['RED']; w_ = Ansii['LIGHT_WHITE']
#print(f'{yy_}This is a second {g_} attempt {r_} of color coding {w_} using the shallow copies')

#clr: dict = {'b':"BLACK", 'r':"RED", 'g':"GREEN", 'y':"YELLOW", 'u':"BLUE", 'm':"MAGENTA", 'c':"CYAN", 'w':"WHITE",
#             'o':"RESET",
#             'B':"LIGHTBLACK_EX", 'R':"LIGHTRED_EX", 'G':"LIGHTGREEN_EX", 'Y':"LIGHTYELLOW_EX", 'U':"LIGHTBLUE_EX",
#             'M':"LIGHTMAGENTA_EX", 'C':"LIGHTCYAN_EX", 'W':"LIGHTWHITE_EX",
#             'D':"DIM", 'N':"NORMAL", 'H':"BRIGHT", 'O':"RESET_ALL"}
#^^ in above, single letter for Fore color alone, 2 chars for Fore + Back, 3 chars for Style + Fore + Back in that order

# COLOR and func call ALIASES
#x0 = w = fn.cj(W_)     #c0 = 'HWb';  #-- color combo shortcuts ... this one for BRIGHT WHITE on Black background
#x1 = x = fn.cj('Ncb')  #c1 = 'Ncb';  #-- Normal Cyan   ... it's short since cj(cn) has no quote marks
#x2 = z = fn.cj('Dcb')  # c2 = 'Dcb'; #-- Dim Cyan
#x3 = y = fn.cj(Y_)     #c3 = 'y';    #-- Yellow
#x4 = fn.cj('Nyb')
# Colors reminder {w}=White/b, {x}=Cyan/b, {z}=dim cyan, {y}=Yellow, {cj('HBw')}= Hight Black/w

allowed_4_Fore = 'brgyumcwoBRGYUMCW'
allowed_4_Style = 'DNHO'

symbols_01 = "▃" * 20; symbols_02 = "▔" * 20; symbols_03 = "▚" * 20

#print(f'(1x) The importation of vars_01 into Main has finished\n')

