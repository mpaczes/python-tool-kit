# co trzeba zrobic jezeli chcemy zaimportowac modul z innego katalogu
import sys
sys.path.append('C:\devel_python')
# w windowsie trzeba utworzyc zmienna srodowiskowa (env var) 'PYTHONPATH' o wartosci jak wyzej

# from my_module import *
from my_module import test, find_index
# import my_module
# import my_module as mm

# przykladowe moduly standardowych bibliotek
import random, math, datetime, calendar, os

courses = ['History', 'Math', 'Physics', 'CompSci']

# index = mm.find_index(courses, 'Math')
index = find_index(courses, 'Math')
print(index)

print(test)

print(sys.path) # lista katalogow na mojej maszynie gdzie Python szuka modulow kiedy uruchamiamy import

# ['C:\\devel_python\\moduly', 
# 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip', 
# 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python311\\Lib', 
# 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python311\\DLLs', 
# 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python311', 
# 'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages']

# czyli Python szuka plikow do zaimportowania w kolejnosci :
#   biezacy katalog z ktorego uruchamiamy skrypt
#   Python path environment variable (PYTHONPATH)
#   standard directory libraries
#   site-packages directory for third party packages

