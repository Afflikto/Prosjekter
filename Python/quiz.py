import random

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

#print(random.choice(spm_geografi))


ant_spm = len(spm_geografi)
nytt_spm_index = random.randrange(0, ant_spm)
nytt_spm = spm_geografi[nytt_spm_index]
nytt_spm_fasit = svar_geografi[nytt_spm_index]
nytt_spm_brukersvar = input(nytt_spm + "\n>>")


if nytt_spm_fasit == nytt_spm_brukersvar.lower().strip():
    print("Riktig svar!")
else:
    print("Feil svar! Riktig svar var: " + nytt_spm_fasit.title())