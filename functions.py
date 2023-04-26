import json, random

def savepop(nom, popu, gene, data):
    data["pop"] = popu
    data["gen"] = gene

    json_object = json.dumps(data, indent=4)

    with open(nom + ".json", "w") as outfile:
        outfile.write(json_object)


def mutation(listepropre, chancemut):
    liste = listepropre[:]
    for i in range(len(liste) - 2):
        rng = random.random()
        if rng < chancemut:
            if random.randint(1, 2) == 1 and liste[i] <= 2:
                liste[i] += 1
            elif liste[i] >= 2:
                liste[i] -= 1
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


def showPieces(pieces):
    txt = ""
    for i in range(pieces):
        txt = txt + "o "
    print(txt)


def makenewgen(pop, indi, generation):
    pop.append([])
    for i in pop[generation - 1]:
        if i != indi:
            newindi = []
            for y in range(len(i)):
                if random.randint(1, 2):
                    newindi.append(i[y])
                else:
                    newindi.append(indi[y])
            newindi[0] = 1
            if newindi[1] > 2:
                if random.randint(1, 2) == 1:
                    newindi[1] = 1
                else:
                    newindi[1] = 2
            pop[generation].append(mutation(newindi[:]))
        else:
            pop[generation].append(mutation(i[:]))