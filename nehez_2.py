class Állatfaj:
    def __init__(self, fajnév, tömeg):
        self.fajnév = fajnév
        self.tömeg = tömeg

allatok = []
for i in range(3):
    nev = input("Add meg egy állatfaj nevét! ")
    tomeg = int(input("Hány kilogramm a tömege egy példánynak? "))
    allat = Állatfaj(nev, tomeg)
    allatok.append(allat)

for i in allatok:
    print(f"A(z) {i.fajnév} tömege {i.tömeg} kg.")

max = 0
for i in range(len(allatok)):
    if allatok[i].tömeg > allatok[max].tömeg:
        max = i
fki = open("legnehezebb.txt", "wt", encoding="utf8")
fki.write(allatok[max].fajnév)
fki.close()