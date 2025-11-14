#Shooting_game.py
import pygame
import sys
pygame.init()

######
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)
pink = (255,133,215)
orange = (240,155,89)
######



w = 480
h = 640

pad = pygame.display.set_mode((w,h)) #화면 생성
pygame.display.set_caption("Shooting Game") #제목 설정

#####배경화면 넣기#####
bg =pygame.image.load("background.jpg")
pad.blit(bg,(0,0))





pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
