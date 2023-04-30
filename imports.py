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