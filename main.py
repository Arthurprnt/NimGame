import os, pygame
from functions import *
from btrpygame import *
from imports import *

"""

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


for i in range(1000):

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
        print("Génération: " + str(gen) + " | Winrate: " + str(round(winrate, 1)) + "% | Indi gagnant: " + str(len(bestindi)))
        showgen = 0

    makenewgen(population, bestindi, CHANCE_MUTATION_NEURONE, MEMBRES_PAR_POPULATION)
    
    generationmade += 1
    if generationmade >= 1000:
        savepop(save, population, bestindi[random.randint(0, len(bestindi)-1)], gen, data)
        generationmade = 0
    
print("Génération: " + str(gen) + " | Winrate: " + str(round(winrate, 1)) + "% | Indi gagnant: " + str(len(bestindi)))
savepop(save, population, bestindi[random.randint(0, len(bestindi)-1)], gen, data)
#fichier.close()

"""

"""
STATS:
0 = MENU
1-5 = PLAY AGAINST BEST IA
"""

CHANCE_MUTATION_NEURONE = 0.19
PLAY_BEST = False

pieces = 8

pygame.init()

while running:

    screen.blit(background.image, background.pos)

    if stats == 0:
        screen.blit(logo.image, logo.pos)
        display(screen, btn_play)
        display(screen, btn_learn)
        display(screen, btn_exit)
    elif stats == 1:
        screen.blit(logo.image, logo.pos)
        display(screen, btn_load)
        display(screen, btn_back)
        if namesave != "":
            showtext(screen, "Save name: " + namesave, "assets/DIN_Bold.ttf", 70, (screen_x // 2, screen_y // 2 - 150), (255, 255, 255), "center")
        else:
            showtext(screen, "Save name: *write it*", "assets/DIN_Bold.ttf", 70, (screen_x // 2, screen_y // 2 - 150), (255, 255, 255), "center")
        if error1:
            showtext(screen, "This file does not exist", "assets/DIN_Bold.ttf", 30, (screen_x // 2, screen_y // 2 - 90), (255, 100, 90), "center")
        if error2:
            showtext(screen, "You must give the save a name. Be sure this file does not exist.", "assets/DIN_Bold.ttf", 30, (screen_x // 2, screen_y // 2 - 90), (255, 100, 90), "center")
    elif stats == 2:
        showtext(screen, "How many coins do you want to take ?", "assets/DIN_Bold.ttf", 50, (screen_x // 2, screen_y // 2), (255, 255, 255), "center")
        display(screen, btn_1)
        display(screen, btn_2)
        display(screen, btn_3)
        for i in range(pieces):
            screen.blit(liste_coins[i].image, liste_coins[i].pos)
    elif stats == 3:
        stats = 4
        choice = round(best[pieces - 1])
        pieces -= round(best[pieces - 1])
        if pieces <= 0:
            win = True
            textwinner = "The ia won the match !"
    elif stats == 4:
        for i in range(pieces):
            screen.blit(liste_coins[i].image, liste_coins[i].pos)
        showtext(screen, f"The ia took {choice} coins.", "assets/DIN_Bold.ttf", 90, (screen_x // 2, screen_y // 2 - 150), (255, 255, 255), "center")
        display(screen, btn_next)
    elif stats == 5:
        showtext(screen, textwinner, "assets/DIN_Bold.ttf", 90, (screen_x // 2, screen_y // 2 - 150), (255, 255, 255), "center")
        display(screen, btn_replay)
        display(screen, btn_exitgame)
    elif stats == 6:
        screen.blit(logo.image, logo.pos)
        display(screen, btn_lcreate)
        display(screen, btn_lload)
        display(screen, btn_lback)
        if namesave != "":
            showtext(screen, "Save name: " + namesave, "assets/DIN_Bold.ttf", 70, (screen_x // 2, screen_y // 2 - 150), (255, 255, 255), "center")
        else:
            showtext(screen, "Save name: *write it*", "assets/DIN_Bold.ttf", 70, (screen_x // 2, screen_y // 2 - 150), (255, 255, 255), "center")
        if error1:
            showtext(screen, "This file does not exist", "assets/DIN_Bold.ttf", 30, (screen_x // 2, screen_y // 2 - 90), (255, 100, 90), "center")
        if error2:
            showtext(screen, "You must give the save a name. Be sure this file does not exist.", "assets/DIN_Bold.ttf", 30, (screen_x // 2, screen_y // 2 - 90), (255, 100, 90), "center")
    # Manage user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_BACKSPACE and stats in (1, 6):
                namesave = namesave[:-1]
                error = False
            elif event.unicode in accepted_carac and stats in (1, 6):
                namesave += event.unicode
                error1 = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if stats == 0:
                    if collide(btn_play["target"], event.pos):
                        namesave = ""
                        error1 = False
                        error2 = False
                        stats = 1
                        win = False
                    elif collide(btn_learn["target"], event.pos):
                        namesave = ""
                        error1 = False
                        error2 = False
                        win = False
                        stats = 6
                    elif collide(btn_exit["target"], event.pos):
                        running = False
                elif stats == 1:
                    if collide(btn_load["target"], event.pos):
                        if not os.path.isfile("json/" + namesave + '.json'):
                            error1 = True
                            error2 = False
                        else:
                            file = open("json/" + namesave + '.json')
                            data = json.load(file)

                            MEMBRES_PAR_POPULATION = len(data['pop'][0])
                            NOMBRE_PIECE = len(data['pop'][0][0])
                            gen = data["gen"]
                            population = data["pop"]
                            best = data["best"]

                            stats = 2
                    elif collide(btn_back["target"], event.pos):
                        stats = 0
                elif stats == 2:
                    if collide(btn_1["target"], event.pos):
                        pieces -= 1
                        stats = 3
                    elif collide(btn_2["target"], event.pos):
                        pieces -= 2
                        stats = 3
                    elif collide(btn_3["target"], event.pos):
                        pieces -= 3
                        stats = 3
                    if pieces <= 0:
                        win = True
                        textwinner = "You won the match !"
                elif stats == 4:
                    if collide(btn_next["target"], event.pos):
                        if not win:
                            stats = 2
                        else:
                            stats = 5
                elif stats == 5:
                    if collide(btn_replay["target"], event.pos):
                        stats = 2
                        pieces = 8
                    elif collide(btn_exitgame["target"], event.pos):
                        stats = 0
                elif stats == 6:
                    if collide(btn_lcreate["target"], event.pos):
                        if namesave == "" or os.path.isfile("json/" + namesave + '.json'):
                            error2 = True
                            error1 = False
                        else:
                            stats = 7
                    elif collide(btn_lload["target"], event.pos):
                        if not os.path.isfile("json/" + namesave + '.json'):
                            error1 = True
                            error2 = False
                        else:
                            stats = 7
                    elif collide(btn_lback["target"], event.pos):
                        stats = 0

    pygame.display.flip()
    clock.tick(60)

pygame.quit()