
totalpris = 0
antallvarer = 0

while True:
    pris = float(input("Hva koster varen:"))

    if pris > 0:
        totalpris += pris
        antallvarer += 1
    else:
        break


print(f"Du handlet {antallvarer} varer for {totalpris}kr")
