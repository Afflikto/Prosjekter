navn = input("Skriv ned ditt fulle navn >>")
navn = navn.lower()
navn = navn.replace("æ", "ae")
navn = navn.replace("ø", "o")
navn = navn.replace("å", "a")
navn = navn.title()
navn = navn.strip()


alder = int(input("Skriv alderen din >>"))

if alder < 18:
    print("Du er under 18 år, og kan ikke delta")
else:
    epost = input("Skriv inn E-post addressen din >>")
    if "@" not in epost:
        print("Ugjyldig epost")
    else:
        
        print(f"Hei, {navn}! Din registrering med e-posten {epost} er fullført!")