# Калькулятор v1

from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()

print(Fore.BLACK)
print( Back.MAGENTA)

what = input("Что делаем? (+, -, /, *, %, корень):" )
print( Back.CYAN)


if what == "корень":
	d = float( input("Из какого числа вычеслить корень?:"))
	c = d**0.5
	print ("Результат:" + str(c))
	input()
	exit(0)


if what == "%":
	proz = input("Что дальше?(+, -):" )

a = float( input("Введите первое число:"))
b = float( input("Введите второе число (для процетов - процент):"))

print( Back.GREEN)

if proz == "+" :
	c = a * (1+b*0.01)
	print("Результат: " + str(c))

elif proz == "-" :
	c = a * (1-b*0.01)
	print("Результат: " + str(c))

elif what == "+":
	c = a + b
	print("Результат: " + str(c))

elif what == "-":
	c = a - b
	print("Результат: " + str(c))

elif what == "/":
	c =a / b
	print("Результат: " + str(c))

elif what == "*":
	c = a * b
	print("Результат: " + str (c))

else:
	print("Выбранна неверная команда!")

input()
