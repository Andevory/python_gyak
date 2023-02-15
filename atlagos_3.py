# Átlagos - 3
import random

def névelő(szó):
    magánhangzók = 'aáeéiíoóöőuúüű'
    if szó[0].lower() in magánhangzók:
       return "Az"
    else:
        return "A"

def jelző():
    return random.choice(['piros', 'nagy', 'könnyed'])

print("Adj meg három főnevet!")
for i in range(3):
    fnev = input(f"{i + 1}. főnév: ")
    print(f"{névelő(fnev)} {fnev} {jelző()}.")
