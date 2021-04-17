import random
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset = True)



print(f"{Fore.YELLOW}{Back.RED}{Style.BRIGHT} WELCOME TO OUR TEST PAGE ")
print("option are ;")
print("01 page 1 ")
print("02 page 2 ")
print("03 page 3 ")
print("04 page 4 ")
x = int(input("select the option "))
if  x== 1:
  print("option is ", x)
if  x== 2:
  print("option is ", x)
if  x== 3:
  print("option is ", x)
if  x== 4:
  print("option is ", x)

else:
  print("enter vaild option")
  