import time
deltakere = []

meny = """Velkommen til dansekurs! Hva skal du gjøre?
1. Legge til en deltaker
2. Slette en deltaker
3. Vis oversikt over deltakere
4. Avslutt"""

while True:
    print(meny)
    valg = int(input("Skriv inn valg: "))
    if valg == 1:
        navn = input("Skriv inn navn på deltaker: ")
        deltakere.append(navn)
        print(f"Deltaker {navn} er nå lagt til")
        time.sleep(1)
    elif valg == 2:
        navn = input("Skriv inn navn på deltaker du vil slette:")
        if navn in deltakere:
            deltakere.remove(navn)
            print(f"Deltaker {navn} er nå slettet")
            time.sleep(1)
        else:
            print(f"Deltaker {navn} finnes ikke")
            time.sleep(1)
    elif valg == 3:
        print("Her er listen:")
        print(deltakere)
        time.sleep(1)
    elif valg == 4:
        print("Takk for at du deltok i dansekurs!")
        break
    else:
        print("Ugyldig valg, Prøv igjen.")


