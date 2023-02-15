# Egyszerű - 4

# Írjon programot egyszeru_4.py néven, amely azt vizsgálja, hogy egy felhasználó helyesen
# adja-e meg a jelszavát! A program addig kérdezi újra a felhasználónév-jelszó párost, amíg a
# felhasználó mindkettőt hibátlanul meg nem adja. A program egyetlen felhasználó (bori99)
# jelszavát (Szivecske<3) ismeri, csak ezt a párost fogadja el helyesként. Mind a sikertelen,
# mind a sikeres bejelentkezési kísérletekről üzenetet ír a képernyőre.
# A program üzeneteinek megfogalmazásában kövesse az alábbi példát!

felh = input("Adja meg a felhasználó nevét! ")
jelsz = input("Adja meg a jelszavát! ")

while felh != "bori99" and jelsz != "Szivecske<3":
    print("Belépés megtagadva.")
    felh = input("Adja meg a felhasználó nevét! ")
    jelsz = input("Adja meg a jelszavát! ")
print("Belépés engedélyezve.")