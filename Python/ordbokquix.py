
spørsmål_og_svar = {
    "Hva heter hovedstaden til Horden?": "orgrimmar",
    "Hva heter hjemplaneten til orkene?": "draenor",
    "Hva heter hjembyen til blod alvene?": "silvermoon"
}


totalpoeng = 0


for spørsmål, riktig_svar in spørsmål_og_svar.items():

    print(spørsmål)

    brukersvar = input("Skriv inn ditt svar: ").lower()

    if brukersvar == riktig_svar:
        print("Riktig svar!")
        totalpoeng += 1
    else:
        print(f"Feil svar. Riktig svar er {riktig_svar}.")

print(f"Du fikk {totalpoeng} av {len(spørsmål_og_svar)} riktige.")
