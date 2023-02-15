# Egyszerű - 5

# Írjon programot egyszeru_5.py néven! Kérje be a felhasználótól, hogy Celsius vagy Kelvin
# hőmérsékletet ad meg. Mind a két választás esetén kérje be az átváltandó számot, majd
# használja az alábbi képleteket hozzá:
# Ha a felhasználó olyan választ ad, ami nincs felsorolva, akkor írja ki, hogy „Nincs ilyen
# opció!”

mertek = input("Kérem adja meg, melyik a bemeneti adat típusa (C/K): ")

if mertek == "C":
    c = float(input("Kérem a Celsiusban megadott értéket: "))
    f = c * 9/5 + 32
    print(f"A hőmérséklet Fahrenheitben: {f}")
elif mertek == "K":
    k = float(input("Kérem a Kelvinben megadott értéket: "))
    f = (k - 273.15) * 9/5 + 32
    print(f"A hőmérséklet Fahrenheitben: {f}")
else:
    print("Nincs ilyen opció!")