import os
from functions import *
from imports import *

CHANCE_MUTATION_NEURONE = 0.19
NOMBRE_PIECE = 8
MEMBRES_PAR_POPULATION = 40

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
        choice = round(best[pieces-1])
        pieces -= round(best[pieces-1])
        if pieces <= 0:
            win = True
            textwinner = "The ia won the match !"
        stats = 4
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
    elif stats == 7:
        display(screen, btn_exit)
        showtext(screen, f"Last winner: {winner}", "assets/DIN_Bold.ttf", 70, (screen_x // 2, screen_y // 2 - 200), (255, 255, 255), "center")
        showtext(screen, f"Ia winrate: {winrate}%", "assets/DIN_Bold.ttf", 70, (screen_x // 2, screen_y // 2 - 100), (255, 255, 255), "center")
        showtext(screen, f"Indi: {indi}", "assets/DIN_Bold.ttf", 70, (screen_x // 2, screen_y // 2), (255, 255, 255), "center")
        showtext(screen, f"Gen: {gen}", "assets/DIN_Bold.ttf", 70, (screen_x // 2, screen_y // 2 + 100), (255, 255, 255), "center")
        showtext(screen, f"Best indi: {data['best']}", "assets/DIN_Bold.ttf", 30, (screen_x // 2, screen_y // 2 + 185), (255, 255, 255), "center")
        for i in range(pieces):
            screen.blit(liste_coins[i].image, liste_coins[i].pos)
        if auto:
            display(screen, btn_auto_y)
        else:
            display(screen, btn_auto_n)

        mooves = [1, 2, 3, 0, 1, 2, 3, 0]
        for i in range(len(mooves)):
            if mooves[i] == 0:
                mooves[i] = random.randint(1, 3)

        if auto is True:
            pieces -= mooves[pieces-1]
        else:
            display(screen, btn_p1)
            display(screen, btn_p2)
            display(screen, btn_p3)

        if auto or (not auto and clicked):
            if pieces <= 0:
                liste_switness.append(switness)
                winner = "Humain"
                if indi == MEMBRES_PAR_POPULATION - 1:
                    bestindi = []
                    bestswit = 0
                    for i in range(len(population[-1])):
                        if liste_switness[i] > bestswit:
                            bestswit = liste_switness[i]
                            bestindi = [population[-1][i]]
                        elif liste_switness[i] == bestswit:
                            bestindi.append(population[-1][i])
                    winrate = round((winia * 100) / (indi + 1))
                    gen += 1
                    winia = 0
                    indi = 0
                    liste_switness = []
                    makenewgen(population, bestindi, CHANCE_MUTATION_NEURONE, MEMBRES_PAR_POPULATION)
                    savepop(namesave, population, bestindi[random.randint(0, len(bestindi) - 1)], gen, data)
                else:
                    indi += 1
                pieces = NOMBRE_PIECE
                stats = 7
            else:
                stats = 8
    elif stats == 8:
        display(screen, btn_exit)
        showtext(screen, f"Last winner: {winner}", "assets/DIN_Bold.ttf", 70, (screen_x // 2, screen_y // 2 - 200), (255, 255, 255), "center")
        showtext(screen, f"Ia winrate: {winrate}%", "assets/DIN_Bold.ttf", 70, (screen_x // 2, screen_y // 2 - 100), (255, 255, 255), "center")
        showtext(screen, f"Indi: {indi}", "assets/DIN_Bold.ttf", 70, (screen_x // 2, screen_y // 2), (255, 255, 255), "center")
        showtext(screen, f"Gen: {gen}", "assets/DIN_Bold.ttf", 70, (screen_x // 2, screen_y // 2 + 100), (255, 255, 255), "center")
        showtext(screen, f"Best indi: {data['best']}", "assets/DIN_Bold.ttf", 30, (screen_x // 2, screen_y // 2 + 185), (255, 255, 255), "center")
        for i in range(pieces):
            screen.blit(liste_coins[i].image, liste_coins[i].pos)
        if auto:
            display(screen, btn_auto_y)
        else:
            display(screen, btn_auto_n)

        pieces -= round(population[-1][indi][pieces - 1])
        switness -= 1
        if pieces <= 0:
            switness += 100
            liste_switness.append(switness)
            winia += 1
            winner = "Ia"
            if indi == MEMBRES_PAR_POPULATION-1:
                bestindi = []
                bestswit = 0
                for i in range(len(population[-1])):
                    if liste_switness[i] > bestswit:
                        bestswit = liste_switness[i]
                        bestindi = [population[-1][i]]
                    elif liste_switness[i] == bestswit:
                        bestindi.append(population[-1][i])
                winrate = round((winia * 100) / (indi+1))
                gen += 1
                winia = 0
                indi = 0
                liste_switness = []
                makenewgen(population, bestindi, CHANCE_MUTATION_NEURONE, MEMBRES_PAR_POPULATION)
                savepop(namesave, population, bestindi[random.randint(0, len(bestindi) - 1)], gen, data)
            else:
                indi += 1
            pieces = NOMBRE_PIECE
        stats = 7
        if not auto:
            clicked = False
    # Manage user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and stats in (1, 6):
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
                            win = False
                            pieces = NOMBRE_PIECE
                            stats = 2
                    elif collide(btn_back["target"], event.pos):
                        stats = 0
                elif stats == 2:
                    if collide(btn_1["target"], event.pos):
                        pieces -= 1
                        if pieces > 0:
                            stats = 3
                        else:
                            win = True
                            textwinner = "You won the match !"
                            stats = 5
                    elif collide(btn_2["target"], event.pos):
                        pieces -= 2
                        if pieces > 0:
                            stats = 3
                        else:
                            win = True
                            textwinner = "You won the match !"
                            stats = 5
                    elif collide(btn_3["target"], event.pos):
                        pieces -= 3
                        if pieces > 0:
                            stats = 3
                        else:
                            win = True
                            textwinner = "You won the match !"
                            stats = 5
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
                        win = False
                    elif collide(btn_exitgame["target"], event.pos):
                        stats = 0
                elif stats == 6:
                    if collide(btn_lcreate["target"], event.pos):
                        if namesave == "" or os.path.isfile("json/" + namesave + '.json'):
                            error2 = True
                            error1 = False
                        else:
                            population = [createPop(MEMBRES_PAR_POPULATION, CHANCE_MUTATION_NEURONE, NOMBRE_PIECE)]
                            data = {"pop": [], "gen": 0, "best": []}
                            gen = 0
                            indi = 0
                            liste_switness = []
                            winia = 0
                            switness = NOMBRE_PIECE

                            auto = True
                            winrate = "/"
                            winner = "/"
                            stats = 7
                    elif collide(btn_lload["target"], event.pos):
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
                            indi = 0
                            liste_switness = []
                            winia = 0
                            switness = NOMBRE_PIECE

                            auto = True
                            winrate = "/"
                            winner = "/"
                            stats = 7
                    elif collide(btn_lback["target"], event.pos):
                        stats = 0
                elif stats in (7, 8):
                    if stats == 7:
                        if collide(btn_p1["target"], event.pos):
                            pieces -= 1
                            clicked = True
                        elif collide(btn_p2["target"], event.pos):
                            pieces -= 2
                            clicked = True
                        elif collide(btn_p3["target"], event.pos):
                            pieces -= 3
                            clicked = True
                    if collide(btn_exit["target"], event.pos):
                        namesave = ""
                        stats = 6
                    elif collide(btn_auto_y["target"], event.pos):
                        auto = not auto
                        if not auto:
                            clicked = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()