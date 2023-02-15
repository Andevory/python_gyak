# Egyszerű feladat - 1

# Írjon programot egyszeru_1.py néven! A program kérjen be két számot a felhasználótól,
# majd írja ki, hogy melyik a nagyobb! A program üzeneteinek megfogalmazásában kövesse az
# alábbi példát!

# Adatbekérésnél figyelj! Milyen típusú adattal KELL dolgozni!
szam_1 = int(input("Adj meg egy számot! "))
szam_2 = int(input("Adj meg egy másik számot! "))

if szam_1 > szam_2:
    print(f"A nagyobb érték {szam_1}")
    # print("A nagyobb érték", szam_1)
    # print("A nagyobb érték", szam_1, sep=" ")
elif szam_1 < szam_2:
    print(f"A nagyobb érték {szam_2}")
else:
    print("A két szám egyenlő")
