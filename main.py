print("Lista zakupów")
shopping = {
    "Piekarnia":["Chleb", "Pączek", "Bułki", "Rogale"],
    "Warzywniak":["Marchew", "Seler", "Rukola"],
    "Sportowy": ["Buty", "Piłka", "Rolki"]
}
ilosc_produktow = 0
for shop in shopping:
    print(f"Idę do {shop} i kupuję tam {shopping[shop]}.")
    ilosc_produktow += len(shopping[shop])
print(f"W sumie kupuję {ilosc_produktow} produktów.")
