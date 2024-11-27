import time
import random

# På Level 1 må du reagere raskere enn 1 sekund for å 
# komme videre til level 2
levels = {
    "Level 1":1,
    "Level 2":0.8,
    "Level 3":0.5,
    "Level 4":0.35,
    "Level 5":0.25,
    "Level 6":0.15,
    "Final level":0.10
}

spill_info = """
Reaksjonstid - Teh GAME

Trykk ENTER for å starte en runde.
Trykk deretter ENTER igjen så fort du kan, etter du ser
*_* på skjermen.
Du får da vite reaksjonstiden din i sekunder.
"""

print(spill_info)

# Spillet starter på Level 1 og går videre
for level, maxtid in levels.items():
    print(f"\n{level} - Maksimal tillatt tid: {maxtid} sekunder")

    # Start runden
    input("Trykk ENTER for å starte ny runde.")
    print(f"{level} starter snart...")
    
    # Random sleep fra 1-3 sekunder før *_* vises
    tid = random.random()*2 + 1
    time.sleep(tid)
    
    # Start tidtakeren
    tid_start = time.time_ns()
    input("*_* Trykk ENTER så raskt du kan!")
    tid_slutt = time.time_ns()

    # Beregn reaksjonstiden i sekunder
    tid_ns = tid_slutt - tid_start
    tid_s = tid_ns / 1_000_000_000  # Omregning til sekunder
    print(f"Reaksjonstid: {tid_s:.4f} sekunder")

    # Sjekk om spilleren klarte reaksjonstiden for dette nivået
    if tid_s > maxtid:
        print(f"Du tapte! Reaksjonstiden din var for treg for {level}.")
        break
else:
    # Spilleren vant hvis de klarer alle nivåer
    print("Gratulerer! Du klarte alle nivåene og vant spillet!")
