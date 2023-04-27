import json, random

def savepop(nom, popu, best, gene, data):
    data["pop"] = popu
    data["gen"] = gene
    data["best"] = best

    json_object = json.dumps(data, indent=4)

    with open("json/" + nom + ".json", "w") as outfile:
        outfile.write(json_object)


def mutation(listepropre, chancemut):
    liste = listepropre[:]
    for i in range(len(liste) - 2):
        rng = random.random()
        if rng < chancemut:
            liste[i] = random.randint(1, 3)
    liste[0] = 1
    if liste[1] == 3:
        liste[1] = 2
    return liste


def createPop(nbmembers, chancemut, nbcoins):
    indi = [random.randint(1, 3) for _ in range(nbcoins)]
    indi[0] = 1
    if indi[1] > 2:
        if random.randint(1, 2) == 1:
            indi[1] = 1
        else:
            indi[1] = 2
    gen = [indi]
    for i in range(nbmembers - 1):
        gen.append(mutation(indi, chancemut))
    return gen

def moyenneListe(liste1, liste2):
    newliste = []
    for i in range(len(liste1)):
        newliste.append((liste1[i]+liste2[i])/2)
    return newliste

def showPieces(pieces):
    txt = ""
    for i in range(pieces):
        txt = txt + "o "
    print(txt)


def makenewgen(pop, indi, chancemut, nbmembre):
    pop.append([])
    for i in range(nbmembre):
        if i not in indi:
            pop[-1].append(mutation(moyenneListe(indi[random.randint(0, len(indi)-1)], pop[-2][i]), chancemut))
        else:
            pop[-1].append(indi[indi.index(nbmembre[i])])
    if len(pop) > 15:
        pop.pop(0)