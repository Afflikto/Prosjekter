import random
import requests

response = requests.get("https://webapi.no/api/v1/randomPersons/20")
data = response.json()

ant_forsok = 5
forsok = 0


fasit = data["data"][0]["firstname"].lower()
antall_bokstaver = len(fasit)


resultat = "*" * antall_bokstaver
print(resultat)


while forsok < ant_forsok:
    gjett = input("Gjett en bokstav >> ").lower()

    ny_resultat = ""
    riktig_gjett = False

    for i in range(antall_bokstaver):
        if fasit[i] == gjett:
            ny_resultat += gjett
            riktig_gjett = True
        else:
            ny_resultat += resultat[i]

    if riktig_gjett:
        resultat = ny_resultat
    else:
        forsok += 1

    print("Resultatet så langt: \n" + resultat)

    if resultat == fasit:
        print("Gratulerer, du vant!")
        break
else:
    print(f"Beklager, du tapte! Det riktige navnet var {fasit}.")
