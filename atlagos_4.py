# Átlagos - 4
#
# A program bekér a felhasználótól egy tetszőleges hosszúságú szöveget. Írjon benne
# függvényt, ami paraméterben megkapja ezt a szöveget és a végén visszaadja a szövegben
# található „e” karakterek számát, akár kis- akár nagybetűs formában.
# Ismételje meg addig a szöveg bekérését, valamint az „e” karakterek számának kiírását,
# amíg a felhasználó nem ad meg egy olyan szöveget, amiben nincsen „e” karakter.
# Munkáját atlagos_4.py néven mentse.

def NumOfE(szoveg):
    # return str(szoveg).count('e') + str(szoveg).count('E')
    db = 0
    for i in szoveg:
        if i == 'e' or i == 'E':
            db += 1
    return db

szoveg = "e"
while NumOfE(szoveg) != 0:
    szoveg = input("Kérem adja meg a vizsgált szöveget:\n")
    print(f"Az 'e' karakterek száma: {NumOfE(szoveg)}")
