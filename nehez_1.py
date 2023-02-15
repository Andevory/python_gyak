class HíresNő:

    def __init__(self, név, foglalkozás, nemzetiseg):
        self.név = név
        self.foglalkozás = foglalkozás
        self.nemzetiseg = nemzetiseg

    def Elotag(self):
        if self.nemzetiseg == "n":
            return "Frau"
        else:
            return "Ms."

nok = []
for i in range(3):
    nev = input("Add meg egy híres nő nevét! ")
    fogl = input("Add meg a foglalkozását! ")
    nemz = input("Add meg a nemzetiségét (a/n)! ")
    No = HíresNő(nev, fogl, nemz)
    nok.append(No)

for i in nok:
    print(f"{i.Elotag()} {i.név} egy híres {i.foglalkozás}")
