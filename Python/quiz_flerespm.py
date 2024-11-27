import random

print("Du må svare riktig på tre svar på rad for å vinne!")

spm_geografi = [
    "Hva heter Norges lengste elv?",
    "Hva kalles den største byen i Troms?",
    "Hvor høyt er Norges høyeste fjell?",
    "Hvilken by har Norges største kirke?"
]

svar_geografi = [
    "glomma",
    "tromsø",
    "2469",
    "trondheim"
]

riktigsvar = 0
streak = 0
totalspm = 0

while streak < 3:
    ant_spm = len(spm_geografi)
    nytt_spm_index = random.randrange(0, ant_spm)
    nytt_spm = spm_geografi[nytt_spm_index]
    nytt_spm_fasit = svar_geografi[nytt_spm_index]
    nytt_spm_brukersvar = input(nytt_spm + "\n>>")

    if nytt_spm_fasit == nytt_spm_brukersvar.lower().strip():
        print("Riktig svar!")
        riktigsvar += 1
        streak += 1
        totalspm += 1
    else:
        print("Feil svar! Riktig svar var: " + nytt_spm_fasit.title())
        streak = 0
        totalspm += 1

riktigsvarprosent = riktigsvar * 100 / totalspm
print(f"Du fikk {riktigsvar} riktige svar og svarte riktig på {
      riktigsvarprosent}% av spørsmålene!")
