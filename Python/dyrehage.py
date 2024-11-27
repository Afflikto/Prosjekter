dyrehage = ["løve", "bjørn"]
meny = """Legg til dyr til dyrehagen
Trykk på q for å avslutte"""

while True:
    print(meny)
    dyr = input("Legg til ett dyr >> ")
    if dyr.lower() == "q":
        break
    else:
        dyrehage.append(dyr)

print(dyrehage)
