# Date: 8/03/2025
# This module will hold the message lines for the Learn_Lists_and_Modules main
# This module will be imported as "msg"
'''
... more to follow
'''
import vars_01 as v #-- we are NOT importing the primary vars because main already loaded them !!!
#from . import funcs_01 as fn

#v = vars_01() #-- because above ^^^ imports are blocked
#fn = funcs_01()

#print(f'(1) The importation of mssgs_01 into Main has begun\n')


# Title Box ('00')      --- vvv --- capital A-Z has lower ascii code than lower case a-z
intro_00a = f'{v.yy_}WELCOME TO LEARNING AND REVIEWING re PYTHON LISTS{v.W_}'
intro_00b = f'{v.yy_}AND re LAYERED importing of MODULES{v.W_}'

intro_00A = f'(00)  <-- This is the {v.yy_}current lesson frame number{v.W_}'
intro_00B = f'The frame number (display_id) {v.yy_}will be incrementing{v.W_} as we advance thru lessons'
intro_00C = f'At the moment this is {v.yy_}merely an introductory{v.W_} first frame'
intro_00D = f'We will be exercising various {v.yy_}Python list methods{v.W_} here'
intro_00E = 'Additionally, many other Python features are brought to light at the same time including but not limited to:'

intro_00F = f'(a) Using the {v.yy_}Package_01 / vars_01{v.W_} module to print different colors on the console'
intro_00G = f'(b) Using {v.yy_}string alignment{v.z_} (e.g., Str.center, spc:<10, more)'
intro_00H = f'(c) Using the {v.yy_}funcs_01 module{v.z_} to repeatedly generate indented lists like this one'
intro_00I = f'(d) Using the {v.yy_}Webster module{v.z_} to open additional info/{v.r_}MUSIC{v.z_} in the web browser'
intro_00J = f'(e) Using the {v.yy_}Keyboard module{v.z_} to detect {v.g_}single{v.z_} keystroke inputs'
intro_00K = f'(f) Linking to {v.yy_}my own "Back of Stage" blog{v.z_} to provide more {v.g_}on-topic{v.z_} information'
intro_00L = f'(g) Opening a {v.yy_}"More to Explore"{v.z_} informational web page ---> {v.yy_}Look in your browser -->{v.z_}'


intro_00_in_list = [intro_00F, intro_00G, intro_00H, intro_00I, intro_00J, intro_00K, intro_00L ]
#--^^^-- used in the outputting of the indented list ???


intro_00M = f'For this first frame (00) we additionally {v.yy_}link to Back Stage web page explaining "aliases" -->{v.z_}'

# Frame ender options
intro_00X: str = 'Hit "c" or "SPACE" to continue to next learning frame'
intro_00Y: str = 'Hit CAPITAL "A-Z" to open browser TABS showing more information re this frame'

#--^^^--usages:
#outp_01x: str = f'{cj('Hrb')}{display_id}: {intro_01x.center(90)}'; print(outp_01x)
#outp_01y: str = f'{cj('Hyb')}{intro_01y.center(90)}'; print(outp_01y)

# Title Box ('01')
intro_01 = f'This will be a further exercise showing ANSI foreground and background colors'


# Colors reminder {w}=White/b, {x}=Cyan/b, {z}=dim cyan, {y}=Yellow, {cj('HBw')}= Hight Black/w
#print(f'\n{v.x_}TEST of color generator function, cj[abc]\'s Style, Fore, Back permutations\n')

intro_01A = f'{v.x_}bW = \t{v.Ansii['BLACK']}{v.Ansi_['WHITE']}This should be plain-Black on lite-white backround {v.W_}and then back to white/b'
intro_01B = f'{v.x_}HbY = \t{v.Ansii['BLACK']}{v.Ansi_['YELLOW']}This should be brite Black on lite yellow backround {v.x_}and then back to normal cyan'
intro_01C = f'{v.x_}HcW = \t{v.Ansii['CYAN']}{v.Ansi_['WHITE']}This should be brite Cyan on brite white backround {v.x_}and then back to normal'
intro_01D = f'{v.x_}DcW = \t{v.Ansii['CYAN']}{v.Ansi_['WHITE']}This should be dim Cyan on brite white backround {v.x_}and then back to normal'
intro_01E = f'{v.x_}Hbu = \tThis should be brite Black on brite blue backround {v.x_}and then back to normal'
intro_01F = f'{v.x_}Uw = \tThis should be brite blue on dim white backround {v.x_}and then back to normal'
intro_01G = f'{v.x_}HbY = \t{v.symbols_01}{v.symbols_02}{v.symbols_03}{v.x_}and then back to normal cyan'
#--^^-- symbols_01 = "▃" * 20; symbols_02 = "▔" * 20; symbols_03 = "▚" * 20;
intro_01H = f'\n{v.x_}See the adjacent browser for more info from G4G re Colorama {v.y_}and TermColor -->{v.x_}'
intro_01I = f'{v.x_}Also see the adjacent browser for {v.y_}Symbol picker website -->{v.x_}'
intro_01J = f'\nNote that not all fore and background combinations work well with text chars\n'
intro01_list_A = []
intro01_list_B = []
#--^^^-- Add function to step thru lists and print them out e.g. print intro_{display_id){next_abc}

aside_001 = f'{v.z_}First "Aside" frame re: {v.yy_}The WEBSTER module{v.z_}'
aside_001A = f'(a) There are {v.yy_}hundreds of External Modules{v.z_} (a.k.a. "Libraries"for Python)'
aside_001B = f'See: https://www.youtube.com/results?search_query=external+libraries+python'
aside_001C = f'(b) Some are very {v.yy_}simple like COLORAMA and WEBSTER{v.z_} (latter discussed here)'
aside_001D = f'(c) Some are very complex and have a {v.yy_}steep learning curve{v.z_}'
aside_001E = f'(e) WEBSTER in particualr has very {v.yy_}limited control{v.z_} over the local Web Browser'
aside_001F = f'(f) WEBSTER can open new URL\'s in the Browser {v.r_}BUT CANNOT CLOSE THEM{v.z_} !!!!'
rt_arrow_001G = f'-{v.yy_}={v.r_}' *20
aside_001G = f'\n\t{v.r_}PLEASE CLOSE THE THREE DEMO URL\'S OPENED IN THE CURRENT BROWSER {rt_arrow_001G}--->{v.z_}\n'
aside_001H = f'(1) A first  of the three links to {v.yy_}MUSIC TO CODE BY{v.z_} (e.g. Chill Flow)'
aside_001I = f'(2) A second of the three links to {v.yy_}Old Man\'s Back Stage{v.z_} page'
aside_001J = f'(3) A last   of the three links to {v.yy_}Old Man\'s Links for Python Noobs{v.z_} page'
aside_001K = f'--^^^--- These are {v.g_}just for Demo purposes{v.z_} of webster\'s capabilities'
aside_001L = f'LOGIC ERROR IN WHILE LOOP that REQUIRED AN EXTRA MESSAGE LINE was fixed'


aside_002 = f'{v.z_}Second "Aside" frame re: {v.yy_}AVOID SHINY DISTRACTIONS{v.z_}'
aside_002A = f'(a) There are ALWAYS {v.yy_}One-better External Modules{v.z_} than your current ones'
aside_002B = f'RICH may be {v.yy_}better than COLORAMA{v.z_}. SELENIUM may be {v.yy_}better than WEBSTER{v.z_}'
aside_002C = f'(b) Each is a {v.r_}TEMPTATION{v.z_} to distract you from the {v.g_}PRImARY GOAL{v.z_}'
aside_002D = f'And that is: TO LEARN THE FUNDAMENTALS FIRST (strings, lists, dictionaries, etc.)'
aside_002E = f'(c) So no more diversions. Let\'s get straight to the 11 LIST METHODS'
aside_002F = f'(d) We want to understand MORE than just the methods.'
aside_002G = f'(e) We want a {v.r_}DEEP understanding{v.z_} of how to {v.yy_}cleverly{v.z_} use the methods.'

aside_007 = f'{v.z_}"Aside" frame re: {v.yy_}Random Shuffling of a LIST{v.z_}'
aside_007A = (f'(a) 007A <--This is link to {v.yy_}Learn Python Interactively{v.z_} URL= '
              f'https://learnpython.ai/welcome-to-learnpython)')
aside_007B = f'(a.1) 007B <-- {v.yy_}Re Libraries,{v.z_} See https://www.youtube.com/results?search_query=external+libraries+python'
aside_007C = f'(b) 007C <-- This is link to {v.yy_}Indently T-strings{v.z_} https://www.youtube.com/watch?v=vymJMn97wks'
aside_007D = f'(c) 007D <-- This is link to {v.yy_}Bro Code LIST Comprehensions{v.z_} https://www.youtube.com/watch?v=YlY2g2xrl6Q'
aside_007E = f'(e) 007E <-- This is link to {v.yy_}Reddit Learn PY wiki{v.z_} https://www.reddit.com/r/learnpython/wiki/index/'
aside_007F = f'(f) 007F <-- This is link to {v.r_}Py org"s wiki {v.z_} https://wiki.python.org/moin/'
rt_arrow_001G = f'-{v.yy_}={v.r_}' *10
aside_007G = (f'(g) 007G <-- This is link to {v.r_} Luke"s {rt_arrow_001G}--->{v.z_}\n'
              f'\thttps://www.youtube.com/watch?v=wUSDVGivd-8&t=1132s')
aside_007H = (f'(1) 007H <-- This is link to {v.yy_}MUSIC TO CODE BY{v.z_} \n'
              f'\thttps://www.youtube.com/watch?v=npNU0JIYZA0&list=RDnpNU0JIYZA0&start_radio=1')
aside_007I = f'(2) 007I <-- This is link to {v.yy_}Old Man\'s Back Stage{v.z_} page https://oldmanlearningsupport.blogspot.com'
aside_007J = (f'(3) 007J <-- This is link to {v.yy_}Old Man\'s Links for Python Noobs{v.z_} page\n'
              f'\t https://steppingback269.blogspot.com/2025/07/links-for-python-noobs.html')
aside_007K = f'--^^^--- These are {v.g_}just for Demo purposes{v.z_} of webster\'s capabilities'
aside_007L = f'007L <-- This is link to ______________________'

aside_008 = f'{v.z_}"Aside" frame re: {v.yy_}Enumerate applied to a LIST{v.z_}'

aside_009 = f'{v.z_}"Aside" frame re: {v.yy_}TwT\'s 10 COMPREHENSIONS to know{v.z_}'

append_01 = f'{v.yy_}THE APPEND() METHOD{v.z_}'
append_01A = f'{v.z_}The APPEND() function extends by by ONE item & is inherently built in for all instances of LIST objects'
append_01B = (f'{v.z_}(a) A {v.yy_}LIST{v.z_} is a {v.yy_}MUTABLE{v.z_} object that can be enlarged, shrunk '
              f'or cleared{v.z_}')
append_01C = f'{v.z_}(b) Assume a GROUP defined by alist of people names, namely: \n'
append_01D = f'\t\t\t\t▌▌ {v.g_}group_01: list[str] = ["Adam", "Bill", "Charlie", "David"]{v.z_}\n'
append_01E = f'{v.z_}(c) Assume a new person is joinng this group_01, namely: \n'
append_01F = f'\t\t\t\t▌▌ {v.g_}group_01.append("Ernie"){v.z_}\n'
append_01G = f'(d) If we now print out the modified {v.yy_}MUTABLE{v.z_} list: |{v.g_}print(group_01){v.z_} , we get:'
append_01H = f'\t\t\t\t▌▌ {v.g_}["Adam", "Bill", "Charlie", "David", "Ernie"]{v.z_}'
append_01I = f'See Indently at https://www.youtube.com/watch?v=0yySumZTxJ0&t=432s See also the extend() method'
append_01J = f'(e) WHAT CLEVER ADDITIONAL USES CAN BE MADE OF THE append() CAPABILITY ???'
append_01K = f'(e) https://oldmanlearningsupport.blogspot.com/2025/08/mind-mapping-append-method-relative-to.html'



URL_music00A = f'https://www.youtube.com/watch?v=2szaePjsCIw'  #--vvv-- Description of this URL is next below
URL_descip00A = f'Future Music Explodes Brain Power --Chill Vibes' #https://www.youtube.com/@ChillVibesMusic999
URL_music00B = f'https://www.youtube.com/watch?v=FibqV8cU_tQ&list=PL3mW7rMEvWWPdj7ddPKAIJKRCz1P52GJi'
URL_descip00B = f'Deep Work Music for Coders —- Chill Vibes'
URL_music00C = f'https://www.youtube.com/watch?v=l9nh1l8ZIJQ&list=RDl9nh1l8ZIJQ&start_radio=1&t=374s'
URL_descip00C = f'rogramming / Coding / Hacking music vol.16 -- JimTV'
URL_music00D = f'https://www.youtube.com/watch?v=ka4KN2KEGmI'
URL_descip00D = f'Programming / Coding / Hacking music vol.24 -- JimTV'
URL_music00E = f'https://www.youtube.com/watch?v=mhNg55_IYiw&list=RDmhNg55_IYiw&start_radio=1'
URL_descip00E = f'Music for Work — Deep Focus Mix for Programming -- Chill Flow' #https://www.youtube.com/@chillflow09
URL_music00F = f'https://www.youtube.com/watch?v=yjqz4hx3b0E'
URL_descip00F = f'Music for Work — Deep Focus Mix for Programming, Coding -- Chill Flow'

URL_Pydoc00A = f'https://steppingback269.blogspot.com/2025/07/links-for-python-noobs.html'  #Python Documentation
                                                                            # (explanation next below)
URL_Pyexp00A = f'Links for Python Noobs -- Old Man Learns to Code (OML2c)'
URL_Pydoc00B = f'https://docs.python.org/3/' #  ---Official documentation for Python 3.13.5
URL_Pyexp00B = f'Official Python 3.13.5 documentation'
URL_Pydoc00C = f'https://wiki.python.org/moin/BeginnersGuide'
URL_Pyexp00C = f'Beginner\'s Guide to Python'

URL_web00A = f'https://www.youtube.com/watch?v=xumUjW99b_0'
URL_web00B = f'https://www.youtube.com/watch?v=6GTt10GDWII'
URL_web00C = f'https://docs.python.org/3/tutorial/modules.html'
URL_web00D = f'https://www.youtube.com/playlist?list=PLyf3HIc5hqTNgTtHaNOlLTRVTQAhIgcvZ'
URL_web00E = f'https://medium.com/@tarakshah/how-to-add-code-snippets-in-blogger-posts-8fc1421d827'
URL_web00F = f'https://symbl.cc/en/unicode-table/'
URL_web00G = f'https://www.youtube.com/watch?v=4gGSy4jUlu4'
URL_web00H = f'https://www.youtube.com/watch?v=Ffeb5ibQDP0'
URL_web00I = f'https://www.youtube.com/watch?v=EoNOWVYKyo0'


# ... to be continued
#print(f'(2x) The importation of mssgs_01 into Main has finished\n')