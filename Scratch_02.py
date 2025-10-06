# Date: 2025~m09~d19 based on Neural Nine at https://www.youtube.com/watch?v=SPM1tm2ZdK4&t=15s
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.remote_connection import FirefoxRemoteConnection
from webdriver_manager.chrome import ChromeDriverManager

options=Options()
options.add_experimental_option("detach", True)     #--note underscore after "add"
#driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()),
#                         options=options)

driver= webdriver.Chrome(service=Service(FirefoxRemoteConnection(remote_server_addr).install()),
                         options=options)

driver.get("https://www.neuralnine.com/")       #--This is lecturor's home page and launches CHROME (it works)

driver.maximize_window()                        #-- at 4:38 /21:37 This instructs Chrome to maximize the opened window

links = driver.find_elements("xpath", "//a[@href]")  #--this will search the web page for all "a tag" elements

for link in links:
    print(link)                     #-- prints raw attributes

#example output (partial)
#C:\Users\gideon\Python_Projects_A0\Project_A03_Learn_Fundamentals\.venv\Scripts\python.exe C:\Users\gideon\Python_Projects_A0\Project_A03_Learn_Fundamentals\.venv\Package_03\Scratch_02.py
#<selenium.webdriver.remote.webelement.WebElement (session="e0268ae375af4b2928e57dd863fc49fb", element="f.11D80D9585F44F64C6F8EDBA6AABB1A3.d.713F663656D8FFC218D37ADB20355E29.e.18")>
#<selenium.webdriver.remote.webelement.WebElement (session="e0268ae375af4b2928e57dd863fc49fb", element="f.11D80D9585F44F64C6F8EDBA6AABB1A3.d.713F663656D8FFC218D37ADB20355E29.e.19")>
#<selenium.webdriver.remote.webelement.WebElement (session="e0268ae375af4b2928e57dd863fc49fb", element="f.11D80D9585F44F64C6F8EDBA6AABB1A3.d.713F663656D8FFC218D37ADB20355E29.e.20")>

print(f'\n\n', "-="*30, f'\n\n')  #--separate the example outputs
for link in links:
    print(link.get_attribute("innerHTML"))  #-- also prints the HTML source text inside the found "a tags"

#example output (partial)
#Skip to content
#Blog
#Books
#Extras
#Home
#Privacy Policy
#Services
#Terms and Conditions
#Tutoring
#<img fetchpriority="high" width="500" height="500" src="https://neuralnine.com/wp-content/uploads/2025/04/neuralnine_logo_circle.png"

print(f'\n\n', "-="*30, f'\n\n')  #--separate the example outputs
for link in links:
    if "Book" in link.get_attribute("innerHTML"):      #-- test the found a-tags for string "Book" inside them
        link.click(Command, CLICK_ELEMENT)              #-- ERROR DOESN'T WORK
        break               #-- click on the first found link and break out of the for loop


breakpoint()


#PATH="C:\\ProgramFiles(x86)\\chromedriver-win32\\chromedriver.exe"
#PATH2= "C:\\Program Files(x86)\\Mozilla Firefox\\firefox.exe"

#driver= webdriver.Firefox(PATH2)
#driver.get("https://oldmanlearningsupport.blogspot.com")

breakpoint()


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

os.system('cls')        #clear the screen using https://www.naukri.com/code360/library/how-to-clear-a-screen-in-python
print(f'\n', '*'*60,'\n')
#fn.clear_d_screen()
#breakpoint()
# (1) pip install selenium <--success !!!
# (2) get webDRIVER from ChromeeDriver page:
# https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.185/win32/chromedriver-win32.zip

'''
From: About Vivaldi:
Vivaldi	7.5.3735.74 (Stable channel) (64-bit) 
Revision	74f05fd41186bb92666bc8b491d45ae013f41205
OS	Windows 10 Version 22H2 (Build 19045.6332)
JavaScript	V8 13.8.258.32
User Agent	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Command Line	"C:\\Users\\gideon\\AppData\\Local\\Vivaldi\\Application\\vivaldi.exe" --flag-switches-begin --flag-switches-end
Executable Path	C:\\Users\\gideon\\AppData\\Local\\Vivaldi\\Application\\vivaldi.exe
Profile Path	C:\\Users\\gideon\\AppData\\Local\\Vivaldi\\UserData\\Default
'''

print(f'Date: 9/17A/2025  --Status: Tutorial by Tech w Tim re  {v.yy_}Selenium{v.W_} step 1= install')
print(f' URL= https://realpython.com/videos/getting-started-lists/\n')
print(f'\t\tSee also {v.yy_}Geeks for Geeks{v.W_} re Lists at below ')
print(f' URL= https://www.geeksforgeeks.org/python/python-lists/\n')
print(f'\t\tAlso connect to {v.yy_}OLD MAN BACK PAGES{v.W_} USING THE LINK below ')
print(f' URL= https://oldmanlearningsupport.blogspot.com\n')
print(f'\t\tFurther see Metcalfe tutorial re {v.yy_}If Else in a List Comprehension{v.W_} USING THE LINK below ')
print(f'URL= https://www.youtube.com/watch?v=EL--NjvBw6o\n')

print('\n', '*'*40, '\n')
print(f'LEARNING TO WORK WITH LISTS')