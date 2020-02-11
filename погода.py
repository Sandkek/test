# погода
import pyowm

from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()

owm = pyowm.OWM('1fc7c882811d1b4b7a449a66ac253eb6', language ="ru" )

print(Fore.BLACK)
print(Back.GREEN)

spot = input("Введите ваш город:")

observation = owm.weather_at_place(spot)
w = observation.get_weather()
temperture = w.get_temperature('celsius')["temp"] 
print(Back.YELLOW)


print("В городе " + spot + " сейчас " + w.get_detailed_status() + ",")
print("Температура около " + str(round(temperture)) + "°C")

if temperture < 10:
	print("На улице холодно! Одевайся теплее :)")
if temperture > 20:
	print("На улице жара! Иди в шортах B)")	
	exit(0)
if temperture > 10:
	print("На улице тепло, иди в джинсах =)")
input()