import random as rd

print("\nBonjou, byenvini sou platfòm jeneratè Epsedo Sosyal la\n")
siyati = input("Antre siyati w: ").title()
non = input("Antre non w: ").title()

try:
    data = open("database.txt", "r")
    data.close()
except FileNotFoundError:
    data = open("database.txt", "w")
    data.close()

kantite = 0
data = open("database.txt", "r")
kantite = len(data.read().split(",")) - 1
data.close()


print(f"\nBonjou {non.title()} {siyati.title()}, nou rekoni nan sèvis nou an")
if kantite > 0:
    print(f"Nou deja jenere epsedo pou {kantite} moun deja")

lis_non = non.split() + siyati.split()
epsedo_1, epsedo_2, epsedo_3 = "", "", ""


for name in lis_non:
    epsedo_1 += name[0].upper()

epsedo_1 += str(len("".join(lis_non)))
epsedo_2 = ("".join(lis_non)).capitalize()
lis_len_lis_non = []

for name in lis_non:
    lis_len_lis_non.append(len(name))

endis = lis_len_lis_non.index(min(lis_len_lis_non))
epsedo_3_ = lis_non[endis]
epsedo_3 = epsedo_3_[::-1].capitalize() + str(rd.randrange(100,1000))

lis_epsedo = [non, siyati, epsedo_1, epsedo_2, epsedo_3]

lis_epsedo_fav = []
for pseudo in lis_epsedo: lis_epsedo_fav.append(pseudo) if len(pseudo) < 7 else print("", end="")

data = open("database.txt", "a")
chwa_epsedo = rd.choice(lis_epsedo_fav)
data.write(chwa_epsedo+",")
data.close()

print(f"\nEpsedo ki pi favorab pou w itilize sou rezo sosyal yo se: {chwa_epsedo}\n")
print(f"Mèsi {non.title()} paske paske ou te chwazi nou.\nBabay \U0001f44b")