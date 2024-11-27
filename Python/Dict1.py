eng_no =  {
    "bird":"fugl",
    "cat":"katt",
    "jerk":"dust",
    "car":"bil"
}

jens = {
    "etternavn":"englund",
    "antall venner":5,
    "vennenavn":["kari", "arne","bernt", "kjell", "goobli"],
    "er kjekk": True,
    "gift": False
}

print(eng_no["bird"])
print(eng_no["car"])
eng_no.update({"jerk": "tulling"})
print(eng_no)

print(" ".join(jens.keys()))

for verdi in jens.values():
    print(verdi)