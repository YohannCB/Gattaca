
fichier = open("penicillium_camemberti.fna","r", encoding="utf-8")

contenu=""

for line in fichier:
    contenu+= line[:-1]


cible="GATTACA"
c=0
for i in range(len(contenu)):
    mot="".join(contenu[i:i+7])
    if mot==cible:
        c+=1
print(c) 

fichier = open("penicillium_camemberti.fna","r", encoding="utf-8")

contenu=""

for line in fichier:
    contenu+= line[:-1]

cible="GATTAC"

n=len(contenu)
m=len(cible)

cpt=0

for idx in range(n-m):
    if idx%1000000==0:
        print(idx, end="/r")
    hit=True
    j=0
    while hit and j<m:
        if contenu[idx+j]!=cible[j]:
            hit=False
        j+=1

    if hit:
        cpt+=1

print(cpt)


def calcule_distannce(cible):
    distance={}
    n=len(cible)
    for idx in range(n-1):
        charactàre=cible[idx]
        distance[charatère]=n-1-idx
    return distance