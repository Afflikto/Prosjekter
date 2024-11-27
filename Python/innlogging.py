brukere = ["per123", "jens234", "kej38"]
passord = ["asdqwe", "qweasd", "asd123"]

while True:
    bruker = input("Brukernavn: ")
    index = brukere.index(bruker)
    if bruker in brukere:
        passord_inn = input("Passord: ")
        if passord_inn == passord[index]:
            print("Velkommen til systemet")
            break
        else:
            print("Feil passord")
    else:
        print("Feil brukernavn")

