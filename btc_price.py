import requests
from time import sleep
from colorama import Fore
logo = """    
  ___  ___   _____   _   _       ___       ___  ___   _____   _____  
    /   |/   | /  _  \ | | | |     /   |     /   |/   | | ____| |  _  \ 
   / /|   /| | | | | | | |_| |    / /| |    / /|   /| | | |__   | | | | 
  / / |__/ | | | | | | |  _  |   / / | |   / / |__/ | | |  __|  | | | | 
 / /       | | | |_| | | | | |  / /  | |  / /       | | | |___  | |_| | 
/_/        |_| \_____/ |_| |_| /_/   |_| /_/        |_| |_____| |_____/  
"""
logo2 = """ 
 _____       ___   _____   _____   __    __ 
/  ___/     /   | |  _  \ |  _  \  \ \  / / 
| |___     / /| | | |_| | | |_| |   \ \/ /  
\___  \   / / | | |  _  { |  _  /    \  /   
 ___| |  / /  | | | |_| | | | \ \    / /    
/_____/ /_/   |_| |_____/ |_|  \_\  /_/     
"""
print (f"{Fore.RED} {logo}")
print (f"{Fore.YELLOW} {logo2}")
print (f'\n{Fore.BLUE}                          By @M_50_S Telegram  ')
token = input(f'{Fore.CYAN}Enter your Telegram Token =>> ')
id = input('Enter your Telegram id =>> ')
def get_btc_api():
    req = requests.get('https://api.coindesk.com/v1/bpi/currentprice/CNY.json').json()
    btc_prices = req['bpi']['USD']['rate_float']
    return btc_prices
while True:
	get_btc_api()
	btcoin = get_btc_api()
	req1 = requests.get(f'https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text= Btc Brice ==> {btcoin}$')
	if 'ok":true' in req1.text :
		print(f'{Fore.GREEN}\nDone Send ....')
		sleep(60)
	elif '"ok":false' in req1.text :
		print (f'{Fore.RED}Error Telegram Id or Token ')
		break