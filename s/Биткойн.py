import requests
url = 'https://blockchain.info/ticker'

x = requests.get(url)
x = x.json()
valutsss = []
for p1 in x:
    valutsss.append(p1)
print('список всех валют: ')
print(valutsss)
dengi = input('введите валюту: ')
kall = input('введите количество валюты: ')

x = requests.get(f'https://blockchain.info/tobtc?currency={dengi}&value={kall}')

print(x.text,"- Такое количество биткойнов вы получите в этой валюте -",dengi)
