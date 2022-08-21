import requests; import threading; from pystyle import Colorate, Colors, Write, Add, Center; import os; import time 


banner = (f"""
 /$$    /$$ /$$                         /$$$$$$$              /$$          
| $$   | $$|__/                        | $$__  $$            | $$          
| $$   | $$ /$$  /$$$$$$  /$$  /$$  /$$| $$  \ $$  /$$$$$$  /$$$$$$        
|  $$ / $$/| $$ /$$__  $$| $$ | $$ | $$| $$$$$$$  /$$__  $$|_  $$_/        
 \  $$ $$/ | $$| $$$$$$$$| $$ | $$ | $$| $$__  $$| $$  \ $$  | $$          
  \  $$$/  | $$| $$_____/| $$ | $$ | $$| $$  \ $$| $$  | $$  | $$ /$$      
   \  $/   | $$|  $$$$$$$|  $$$$$/$$$$/| $$$$$$$/|  $$$$$$/  |  $$$$/      
    \_/    |__/ \_______/ \_____/\___/ |_______/  \______/    \___/                                                                                                                                                     
""")

text = "github.com/natrixdev"
print(Colorate.Horizontal(Colors.blue_to_green, str(banner), 1))
one = Colorate.Horizontal(Colors.blue_to_green, '[1]', 1)
two = Colorate.Horizontal(Colors.blue_to_green, '[2]', 1)
time.sleep(2)

print(Center.XCenter("Choose a viewbot\n\n" + str(one)+" TikTok view bot\n"+str(two)+" Youtube view bot"))
x = input(Center.XCenter("> "))

if x == '1':
    os.system('cls')
    amm = 0
    videourl = input('TikTok video url > ')
    while True: 
        amm = amm+1
        print(Colorate.Horizontal(Colors.blue_to_green, 'Sending views on your tiktok | ' + str(amm) + ' views sent', 1))

    
if x == '2':
    os.system('cls')
    ammo = 0
    videourl = input('Youtube video url > ')
    while True: 
        ammo = ammo+1
        print(Colorate.Horizontal(Colors.blue_to_green, 'Sending views on your video | ' + str(ammo) + ' views sent', 1))
    
else: 
    print('Input needs to be 1 or 2')
    time.sleep(10)
