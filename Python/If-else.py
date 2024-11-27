import random

kast1 = random.randint(1, 6)
kast2 = random.randint(1, 6)
differanse = kast1 - kast2

if kast1 == kast2:
    print("like")
elif differanse > 4:
    print("Stor forskjell")
else:
    print("Ikke noe spessielt")
print(kast1, kast2)