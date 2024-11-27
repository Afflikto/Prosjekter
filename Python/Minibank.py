import time

meny = """Meny
Trykk I for å gjøre et innskudd.
Trykk U for å gjøre et uttak.
Trykk O for å vise saldo.
Trykk P for å vise de siste 5 transaksjonene.
Trykk Q for å avslutte
"""

saldo = 12000
historie = []

while True:
    print(meny)
    valg = input(">>> ").upper()

    if valg == "I":
        innskudd = float(input("Skriv inn beløp: "))
        saldo += innskudd
        transaksjon = f"Innskudd på {innskudd} kr. Saldo er nå {saldo} kr."
        print(transaksjon)
        historie.append(transaksjon)
        if len(historie) > 5:
            historie.pop(0)  # Fjern den eldste transaksjonen hvis det er mer enn 5
        time.sleep(1)

    elif valg == "U":
        uttak = float(input("Skriv inn beløp: "))
        if uttak > saldo:
            print("Du har ikke nok penger til dette uttaket.")
        else:
            saldo -= uttak
            transaksjon = f"Uttak på {uttak} kr. Saldo er nå {saldo} kr."
            print(transaksjon)
            historie.append(transaksjon)
            if len(historie) > 5:
                historie.pop(0)  # Fjern den eldste transaksjonen hvis det er mer enn 5
        time.sleep(1)

    elif valg == "O":
        print(f"Saldo er {saldo} kr.")
        time.sleep(1)

    elif valg == "P":
        print("Siste 5 transaksjoner:")
        if not historie:
            print("Ingen transaksjoner er registrert.")
        else:
            for transaksjon in historie:
                print(transaksjon)
        time.sleep(1)

    elif valg == "Q":
        print("Takk for at du brukte bankautomaten!")
        break

    else:
        print("Ugyldig valg. Vennligst prøv igjen.")
        time.sleep(1)
