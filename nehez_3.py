class Tanulo:
    def __init__(self, nev, osztaly, ttargy, jegy):
        self.nev = nev
        self.osztaly = osztaly
        self.ttargy = ttargy
        self.jegy = jegy

osztaly = []
fbe = open("adatok.txt", "rt", encoding="utf8")
input = fbe.readlines()
for i in input:
    split = i.split(';')
    temp = Tanulo(split[0], split[1], split[2], int(split[3]))
    osztaly.append(temp)

#d, Mennyi tanuló vett részt a mérésen?
print(f"A mérésen {len(osztaly)} tanuló vett részt.")

#e, Számítsa ki mennyi lett a matematika tantárgy jegyeinek átlaga!
jegyek = []
for i in osztaly:
    if i.ttargy == "Matematika":
        jegyek.append(i.jegy)
print(f"A matematika tárgy átlaga: {sum(jegyek) / len(jegyek)}")

#f, Keresse ki azokat a tantárgyakat, melyekből a 11.B tanulói írtak.
print("A 10.B az alábbi tantárgyakból írt:")
targyak = []
for i in osztaly:
    if i.osztaly == "10.B" and i.ttargy not in targyak:
        targyak.append(i.ttargy)
for i in targyak:
    print("\t - ", i)

#g, Határozza meg, melyik tantárgyakból sikerült ötöst szerezniük a diákoknak.
# A kiíratásban szerepeljen az adott tantárgy és a tanuló neve is.

print("5-öst kaptak:")
for i in osztaly:
    if i.jegy == 5:
        print(f"\t{i.nev} - {i.ttargy}")
