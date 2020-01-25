import hashlib
from colorama import Style, Fore
from pyfiglet import figlet_format

title_name = "Sling Kit"
title = figlet_format(title_name,font="starwars") # other fonts "starwars","colossal"
print(Style.BRIGHT, Fore.RED, title)
print("These are some of the options.Check this out ..!")
print(Style.BRIGHT, Fore.GREEN + "[" + Fore.RED + "1.0" + Fore.GREEN + "]" + " String -> md5")
print(Style.BRIGHT, Fore.GREEN + "[" + Fore.RED + "2.1" + Fore.GREEN + "]" + " String -> URL" )
print(Style.BRIGHT, Fore.GREEN + "[" + Fore.RED + "2.2" + Fore.GREEN + "]" + " URL -> String" )
print(Style.BRIGHT, Fore.GREEN + "[" + Fore.RED + "3.1" + Fore.GREEN + "]" + " String -> base64" )
print(Style.BRIGHT, Fore.GREEN + "[" + Fore.RED + "3.2" + Fore.GREEN + "]" + " base64 -> String" )

