# Date:  10/09/2025  Primary varaible values for Learn_Lists_and_Module_03.py are stored here
# This module will be imported first with the alias, "v" so that variable invocations will be v (dot) something
'''
Ran into a Circular Import problem. So changing the color codes to direct ANSI codes 
and avoiding use of the public COLORAMA module
... more to follow
'''


print(f'(1) The importation of Package_03 / vars_01 into memory has begun')


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
W_ = Ansii['LIGHT_WHITE']
w_ = Ansii['LIGHT_WHITE'] + Ansi_['BLACK']
M_ = Ansii['PURPLE']
m_ = Ansii['PURPLE'] + Ansi_['BLACK']
C_ = Ansii['CYAN']
R_ = Ansii['BOLD'] + Ansii['RED']
Y_ = Ansii['BOLD'] + Ansii['YELLOW']
G_ = Ansii['BOLD'] + Ansii['GREEN']
y_ = Ansii['YELLOW'] + Ansi_['BLACK']
z_ = Ansii['LIGHT_CYAN'] + Ansi_['BLACK']
x2= z_
x3= Y_


yy_ = Ansii['YELLOW']; g_ = Ansii['GREEN']; r_ = Ansii['RED']; w_ = Ansii['LIGHT_WHITE']



allowed_4_Fore = 'brgyumcwoBRGYUMCW'
allowed_4_Style = 'DNHO'

symbols_01 = "▃" * 20; symbols_02 = "▔" * 20; symbols_03 = "▚" * 20

#print(f'(1x) The importation of vars_01 into Main has finished\n')

