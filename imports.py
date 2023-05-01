import pygame
from btrpygame import *

running = True
debug = False
stats = 0
screen = pygame.display.set_mode((1920, 1080))
screen_x, screen_y = screen.get_size()
pygame.display.set_caption('NimGame')
pygame.display.set_icon(pygame.image.load('assets/icon.png'))
clock = pygame.time.Clock()

background = pygameimage(pygame.image.load('assets/background.png'), (screen_x // 2 - 2560 // 2, screen_y // 2 - 1440 // 2))
logo = pygameimage(pygame.transform.scale(pygame.image.load('assets/logo.png'), (1500, 322)), (screen_x // 2 - 1500 // 2, screen_y // 15))
btn_play = createbtn("assets/play.png", (465, 105), (screen_x // 2 - 465 // 2, screen_y // 2))
btn_learn = createbtn("assets/learn_ia.png", (465, 105), (screen_x // 2 - 465 // 2, screen_y // 2 + 120))
btn_exit = createbtn("assets/exit.png", (465, 105), (screen_x // 2 - 465 // 2, screen_y // 2 + 240))
coin1 = pygameimage(pygame.transform.scale(pygame.image.load('assets/coin.png'), (150, 150)), (screen_x // 2 - 150 // 2 - 686, screen_y // 10))
coin2 = pygameimage(pygame.transform.scale(pygame.image.load('assets/coin.png'), (150, 150)), (screen_x // 2 - 150 // 2 - 489, screen_y // 10))
coin3 = pygameimage(pygame.transform.scale(pygame.image.load('assets/coin.png'), (150, 150)), (screen_x // 2 - 150 // 2 - 292, screen_y // 10))
coin4 = pygameimage(pygame.transform.scale(pygame.image.load('assets/coin.png'), (150, 150)), (screen_x // 2 - 150 // 2 - 95, screen_y // 10))
coin5 = pygameimage(pygame.transform.scale(pygame.image.load('assets/coin.png'), (150, 150)), (screen_x // 2 - 150 // 2 + 95, screen_y // 10))
coin6 = pygameimage(pygame.transform.scale(pygame.image.load('assets/coin.png'), (150, 150)), (screen_x // 2 - 150 // 2 + 292, screen_y // 10))
coin7 = pygameimage(pygame.transform.scale(pygame.image.load('assets/coin.png'), (150, 150)), (screen_x // 2 - 150 // 2 + 489, screen_y // 10))
coin8 = pygameimage(pygame.transform.scale(pygame.image.load('assets/coin.png'), (150, 150)), (screen_x // 2 - 150 // 2 + 686, screen_y // 10))
liste_coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8]
btn_1 = createbtn("assets/1.png", (200, 200), (screen_x // 2 - 200 // 2 - 300, screen_y // 1.7))
btn_2 = createbtn("assets/2.png", (200, 200), (screen_x // 2 - 200 // 2, screen_y // 1.7))
btn_3 = createbtn("assets/3.png", (200, 200), (screen_x // 2 - 200 // 2 + 300, screen_y // 1.7))