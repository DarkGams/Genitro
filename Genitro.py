-*- coding: utf-8 -*-

import random
import time
from colorama import *

init()

print(Fore.BLUE + 
	"""            ::::::::       ::::::::::       ::::    :::       :::::::::::   :::::::::::       :::::::::       :::::::: 
          :+:    :+:      :+:              :+:+:   :+:           :+:           :+:           :+:    :+:     :+:    :+: 
         +:+             +:+              :+:+:+  +:+           +:+           +:+           +:+    +:+     +:+    +:+  
       :#:             +#++:++#         +#+ +:+ +#+           +#+           +#+           +#++:++#:      +#+    +:+   
      +#+   +#+#      +#+              +#+  +#+#+#           +#+           +#+           +#+    +#+     +#+    +#+    
     #+#    #+#      #+#              #+#   #+#+#           #+#           #+#           #+#    #+#     #+#    #+#     
     ########       ##########       ###    ####       ###########       ###           ###    ###      ########  """)

print("=======================================================================================================================")

time.sleep(3)
print("\n")

print(Fore.GREEN + "Bienvenue sur l'outil Genitro de Gam's\n")

time.sleep(1)
print("Il s'agit d'un générateur de codes discord nitro \n")

time.sleep(1)
print("Ce programme génère des codes nitro en testant diverses combinaisons de caractères\n")

time.sleep(1)
print("Un fichier nitro.txt apparaitra sur votre bureau , il servira à stocker les codes générés\n")

time.sleep(1)
print("Bon courage !")

time.sleep(10)

  
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

while True:
	nitro = ''

	for i in range(10):
		nitro = f"{nitro}{random.choice(chars)}"

	print(f"https://discord.gift/{nitro}")

	with open("nitro.txt", "a+") as file:
		file.write(f"https://discord.gift/{nitro}\n")
		file.close()
