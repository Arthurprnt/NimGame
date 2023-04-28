import os
from functions import *

CHANCE_MUTATION_NEURONE = 0.19
MEMBRES_PAR_POPULATION = 120
NOMBRE_PIECE = 8
PLAY_BEST = True

if input("Do you wan't to use an existing save (y/n) ? ").lower() == 'y':
    save = str(input("Save name: ")).replace(".json", "")
    while not os.path.isfile("json/" + save + '.json'):
        print('This file does not exist.')
        save = str(input("Save name: ")).replace(".json", "")

    file = open("json/" + save + '.json')
    data = json.load(file)

    if data['pop'] != []:
        MEMBRES_PAR_POPULATION = len(data['pop'][0])
        NOMBRE_PIECE = len(data['pop'][0][0])
        gen = data["gen"]
        population = data["pop"]
        best = data["best"]

    file.close()
else:
    save = "unnamedpop"
    population = [createPop(MEMBRES_PAR_POPULATION, CHANCE_MUTATION_NEURONE, NOMBRE_PIECE)]
    data = {"pop":[], "gen":0}
    gen = 0
    best = []

indi = 0
generationmade = 0
showgen = 9


for i in range(5000):

    liste_switness = []
    winia = 0

    for i in range(MEMBRES_PAR_POPULATION):

        pieces = NOMBRE_PIECE
        remain = True
        switness = NOMBRE_PIECE

        while remain:
            
            if PLAY_BEST == True:
                showPieces(pieces)
                
                request = NOMBRE_PIECE+1
                while pieces - request < 0:
                    request = int(input("Combien de pieces voulez vous enlever ? "))
                    if pieces - request < 0:
                        print("Il n'y a pas assez de pièces")
            else:
                listemoovs = [1, 2, 3, 0, 1, 2, 3, 0]
                for i in range(len(listemoovs)):
                    if listemoovs[i] == 0:
                        listemoovs[i] = random.randint(1, 3)
                request = listemoovs[pieces-1]
            
            pieces -= request
            if pieces <= 0:
                gagnant = "Humain"
                remain = False

            if pieces != 0:
                
                if best != [] and PLAY_BEST == True:
                    showPieces(pieces)
                    print("L'ia a enlevé", round(best[pieces-1]), "pièces")
                    pieces -= round(best[pieces-1])
                else:
                    pieces -= round(population[-1][indi][pieces-1])

                switness -= 1

                if pieces <= 0:
                    gagnant = "Ia"
                    remain = False
                    switness += 100
                    winia += 1

        liste_switness.append(switness)
        
        if PLAY_BEST == True:
            print("Gagnant:", gagnant)
            print("")
            print("")
        
        
        indi += 1

    bestindi = []
    bestswit = 0
    for i in range(len(population[-1])):
        if liste_switness[i] > bestswit:
            bestswit = liste_switness[i]
            bestindi = [population[-1][i]]
        elif liste_switness[i] == bestswit:
            bestindi.append(population[-1][i])
    gen += 1
    indi = 0
    
    winrate = (winia*100)/MEMBRES_PAR_POPULATION
    
    showgen += 1
    if showgen >= 100:
        print("Génération: " + str(gen) + " | Winrate: " + str(round(winrate, 1)) + "%")
        showgen = 0

    makenewgen(population, bestindi, CHANCE_MUTATION_NEURONE, MEMBRES_PAR_POPULATION)
    
    generationmade += 1
    if generationmade >= 1000:
        savepop(save, population, bestindi[random.randint(0, len(bestindi)-1)], gen, data)
        generationmade = 0
    
print("Génération: " + str(gen) + " | Winrate: " + str(round(winrate, 1)) + "%")
savepop(save, population, bestindi[random.randint(0, len(bestindi)-1)], gen, data)
#fichier.close()

"""
running = True
debug = False
stats = 0
screen = pygame.display.set_mode()
screen_x, screen_y = screen.get_size()
pygame.display.set_caption('NimGame')
clock = pygame.time.Clock()

background = pygameimage(pygame.image.load('assets/background.png'), (screen_x // 2 - 2560 // 2, screen_y // 2 - 1440 // 2))

while running:

    screen.blit(background.image, background.pos)

    # Manage user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
"""