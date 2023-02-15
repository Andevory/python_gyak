#Egyszerű - 2

# Írjon programot egyszeru_2.py néven! A program kérjen be két szót a felhasználótól, majd
# írja ki, hogy melyik a hosszabb! A program üzeneteinek megfogalmazásában kövesse az
# alábbi példát!

szoveg_1 = input("Adj meg egy szót! ")
szoveg_2 = input("Adj meg egy másik szót!")

# len = Length, azaz a szöveg vagy lista hossza
if len(szoveg_1) < len(szoveg_2):
    print(f"A hosszabb szó: {szoveg_2}")
elif len(szoveg_2) < len(szoveg_1):
    print(f"A hosszabb szó: {szoveg_1}")
else:
    print("A két szó egyforma hosszú.")