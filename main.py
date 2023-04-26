import os
from functions import *
  
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

population = [createPop(MEMBRES_PAR_POPULATION, CHANCE_MUTATION_NEURONE, NOMBRE_PIECE)]

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
    savepop(save, population, gen, data)

    print(population)
