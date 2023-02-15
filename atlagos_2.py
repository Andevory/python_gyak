# Átlagos - 2
#
# A feladatban elkészítendő program bekéri három film címét, illetve percben kifejezett
# hosszát. Egy-egy filmcím-filmhossz adatpár megadását követően a program a percben
# kifejezett időtartamot átszámolja órákra és pecekre – például a 61 percet 1 óra 1 percre. Az
# eredményt a film címével együtt kiírja.
# A program üzeneteinek megfogalmazásában kövesse az alábbi példát! Azokat a részeket,
# amiket a felhasználó gépel be, a mintában vastagított és döntött betűkkel emeltük ki.
# A program kiindulási alapja a filmalap.py fájlban található. Ennek felhasználásával írjon
# programot atlagos_2.py néven! Egészítse ki a megkapott függvényt úgy, hogy az alkalmas
# legyen percben megadott időtartamot órában és percben visszaadni! A program többi
# részében használja az így kiegészített függvényt!

def óraperc(ido): # Egésztse ki a függvénydefiníciót paraméterrel!
    # Írja meg a függvény többi részét!
    # EGÉSZ osztás eredménye
    óra = ido // 60
    perc = ido % 60
    return str(óra) + ' óra ' + str(perc) + ' perc'

for i in range(3):
    cim = input("Add meg egy film címét! ")
    ido = int(input("Hány perces a film? "))
    print(f"A(z) {cim} című film {óraperc(ido)} hosszú.")
