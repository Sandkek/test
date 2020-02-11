# уравнение
from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()
print(Back.CYAN)
print(Fore.BLACK)


print ("Программа для решения квадратного уравнения")
a = float (input("Введите переменную а:"))
b = float (input("Введите переменную б:"))
c = float (input("Введите переменную с:"))

if (b**2-4*a*c) < 0:
	print(Back.MAGENTA)
	print("Корней нет!")
	input()
	exit(0)

elif (b**2-4*a*c) == 0:
	koren= (-b+(b**2-4*a*c)**0.5)/(2*a)
	print(Back.MAGENTA)
	print("Корень:" + str(koren))
	input()
	exit(0)


print(Back.MAGENTA)
koren1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
print("Первый корень:" + str(koren1))

koren2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
print("Второй корень:" + str(koren2))

input()