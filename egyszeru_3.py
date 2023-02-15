#Egyszerű - 3

# Egy bolt pontban reggel nyolc órakor nyit, és pontban délután tizenhat órakor zár be – azaz
# 8:00-kor már nyitva van és 16:00-kor már nincs nyitva.
# Írjon programot egyszeru_3.py néven! A program kérjen be egy egész órát jelző számot a
# felhasználótól, majd írja ki, hogy a megadott időpontban nyitva van-e a bolt! Amennyiben
# igen, akkor azt is írja ki, hogy mennyi idő van még zárásig, azaz hány egész óra áll
# rendelkezésre odaérni a boltba! A program üzeneteinek megfogalmazásában kövesse az
# alábbi példát!

ora = int(input("Hány óra van most? "))

if ora > 7 and ora < 16:
    print("A bolt nyitva van.")
    print(f"Ennyi órád van odaérni: {16 - ora}")
else:
    print("A bolt zárva van.")