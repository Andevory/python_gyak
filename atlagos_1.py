# Átlagos - 1

# A program vizsgázók nevét és pontszámát kéri be. Eldönti és kiírja, hogy a vizsgázó sikeresen
# vizsgázott-e. A vizsga sikeres, ha legalább 48 pontot ért el a vizsgázó.
# Írjon programot atlagos_1.py néven!
# Kérje be a vizsgázók nevét és az elért pontszámokat! Írja meg azt a függvényt, ami eldönti,
# hogy a vizsga sikeres-e! A függvény paramétere a vizsgázó által elért pontszám, a visszatérési
# értéke logikai érték: igaz, ha a vizsga sikeres, hamis, ha sikertelen. Ezt a függvényt használja
# fel a programjában!
# A program kérdezgesse addig újabb és újabb vizsgázó nevét és pontszámát, amíg a vizsgázó
# nevének megadásakor üres bemenetet nem kap! Ilyen akkor történik, ha a felhasználó
# egyszerűen Entert nyom, anélkül, hogy bármit is begépelne.
# A program üzeneteinek megfogalmazásában kövesse az alábbi példát!

def Sikeres(pontszam):
    return pontszam >= 48
    # if pontszam >= 48:
    #     return True
    # else:
    #     return False

# nev = input("Add meg a vizsgázó nevét! ")
# if nev != "":
#     pontszam = int(input("Add meg a pontszámát! "))
# while nev != "":
#     if Sikeres(pontszam):
#         print(f"{nev} vizsgája sikeres.")
#     else:
#         print(f"{nev} vizsgája sikertelen.")
#     nev = input("Add meg a vizsgázó nevét! ")
#     if nev != "":
#         pontszam = int(input("Add meg a pontszámát! "))

nev = "Cica"
while nev != "":
    nev = input("Add meg a vizsgázó nevét! ")
    if nev != "":
        pontszam = int(input("Add meg a pontszámát! "))
        if Sikeres(pontszam):
            print(f"{nev} vizsgája sikeres.")
        else:
            print(f"{nev} vizsgája sikertelen.")