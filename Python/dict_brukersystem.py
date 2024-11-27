import time

bruker = {
    "brukernavn": "bob",
    "passord": "bobobob"
}
antall_forsøk = 0
max_forsøk = 3
ventetid = 5  # 5 sekunder ventetid

while antall_forsøk < max_forsøk:
    riktig_bruker_passord = True  # Initialiser som True for hvert forsøk

    for key in bruker.keys():
        user = input(f"Oppgi {key} >> ")
        if user != bruker[key]:
            print(f"Feil {key}")
            riktig_bruker_passord = False
            break  # Stopp løkken hvis brukernavn eller passord er feil

    if riktig_bruker_passord:
        print("Velkommen til systemet!")
        break  # Avslutt løkken hvis innlogging er korrekt
    else:
        antall_forsøk += 1
        if antall_forsøk < max_forsøk:
            print(f"Feil innlogging. Du må vente {
                  ventetid} sekunder før neste forsøk.")
            time.sleep(ventetid)  # Vent i 5 sekunder
            print(f"Du har {max_forsøk - antall_forsøk} forsøk igjen.")
        else:
            print("Maks antall forsøk nådd. Tilgang nektet.")
