import json, random
  
CHANCE_MUTATION_NEURONE = 0.39
MEMBRES_PAR_POPULATION = 10
NOMBRE_PIECE = 8

# Opening JSON file
file = open('pop.json')
data = json.load(file)
  
print(data["pop"])

file.close()

def savepop(popu):
    data["pop"] = popu

    json_object = json.dumps(data, indent=4)

    with open("pop.json", "w") as outfile:
        outfile.write(json_object)

def mutation(listepropre):
    liste = listepropre[:]
    for i in range(len(liste)-2):
        rng = random.random()
        if rng < CHANCE_MUTATION_NEURONE:
            if random.randint(1, 2) == 1 and liste[i] < 3:
                liste[i] += 1
            elif liste[i] > 1:
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

    population.append([])
    for i in population[gen-1]:
        if i != bestindi:
            newindi = []
            for y in range(len(i)):
                print(i[y])
                newindi.append(round((i[y]+bestindi[y])/2))
            newindi[0] = 1
            if newindi[1] > 2:
                if random.randint(1, 2) == 1:
                    newindi[1] = 1
                else:
                    newindi[1] = 2
            population[gen].append(newindi[:])
        else:
            population[gen].append(i[:])

    print(population)