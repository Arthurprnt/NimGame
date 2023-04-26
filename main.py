import json, random, os
  
CHANCE_MUTATION_NEURONE = 0.39
MEMBRES_PAR_POPULATION = 10
NOMBRE_PIECE = 8

save = "unnamedpop"
data = {"pop":[], "gen":0}

if input("Do you wan't to use an existing save (y/n) ? ").lower() == 'y':
    save = str(input("Save name: ")).replace(".json", "")
    while not os.path.isfile(save + '.json'):
        print('This file does not exist.')
        save = str(input("Save name: ")).replace(".json", "")

    file = open(save + '.json')
    data = json.load(file)

    if data['pop'] != []:
        MEMBRES_PAR_POPULATION = len(data['pop'][0])
        NOMBRE_PIECE = len(data['pop'][0][0])

    file.close()

def savepop(popu, gene):
    data["pop"] = popu
    data["gen"] = gene

    json_object = json.dumps(data, indent=4)

    with open(save + ".json", "w") as outfile:
        outfile.write(json_object)

def mutation(listepropre):
    liste = listepropre[:]
    for i in range(len(liste)-2):
        rng = random.random()
        if rng < CHANCE_MUTATION_NEURONE:
            if random.randint(1, 2) == 1 and liste[i] <= 2:
                liste[i] += 1
            elif liste[i] >= 2:
                liste[i] -= 1
    return liste
    
def createPop():
    indi = [random.randint(1, 3) for _ in range(NOMBRE_PIECE)]
    indi[0] = 1
    if indi[1] > 2:
        if random.randint(1, 2) == 1:
            indi[1] = 1
        else:
            indi[1] = 2
    gen = [indi]
    for i in range(MEMBRES_PAR_POPULATION-1):
        gen.append(mutation(indi))
    return gen

def showPieces(pieces):
    txt = ""
    for i in range(pieces):
        txt = txt + "o "
    print(txt)

def makenewgen(pop, indi, generation):
    pop.append([])
    for i in pop[gen-1]:
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


population = [createPop()]

print(population)


gen = 0
indi = 0

for i in range(5):

    liste_switness = []

    for i in range(MEMBRES_PAR_POPULATION):

        pieces = NOMBRE_PIECE
        remain = True
        switness = 0

        while remain:

            showPieces(pieces)

            request = NOMBRE_PIECE+1
            while pieces - request < 0:
                request = int(input("Combien de pieces voulez vous enlever ? "))
                if pieces - request < 0:
                    print("Il n'y a pas assez de pièces")

            pieces -= request
            if pieces == 0:
                gagnant = "Humain"
                remain = False

            if pieces != 0:
                showPieces(pieces)

                print("L'ia a enlevé", population[gen][indi][pieces-1], "pièces")

                pieces -= population[gen][indi][pieces-1]

                switness += 1

                if pieces == 0:
                    gagnant = "Ia"
                    remain = False
                    switness += 100

        liste_switness.append(switness)

        print("Gagnant:", gagnant)
        print("")
        print("")
        indi += 1

    bestindi = population[gen][liste_switness.index(max(liste_switness))]
    gen += 1
    indi = 0

    makenewgen(population, bestindi, gen)
    savepop(population, gen)

    print(population)