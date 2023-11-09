import pygame
from pygame import mixer
import random
import sys
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
gold1 = (255, 215, 0)
blue = (0, 0, 255)
aqua = (0, 255, 255)
chartreuse1 = (127, 255, 0)  # (green)

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Main Menu')
screen = pygame.display.set_mode((700, 700), pygame.RESIZABLE)
font = pygame.font.SysFont("comicsans", 40)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False
background = pygame.image.load('Bar.jpg')


def game():
    while True:
        screen.blit(background, (0, 0))
        Game = pygame.Rect(20, 20, 85, 30)
        pygame.draw.rect(screen, black, Game)
        draw_text('GAME', font, aqua, screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)
        button_4 = pygame.Rect(50, 400, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                play()
        if button_2.collidepoint((mx, my)):
            if click:
                controls()
        if button_3.collidepoint((mx, my)):
            if click:
                options()
        if button_4.collidepoint((mx, my)):
            if click:
                quit()
        pygame.draw.rect(screen, red, button_1)
        pygame.draw.rect(screen, red, button_2)
        pygame.draw.rect(screen, red, button_3)
        pygame.draw.rect(screen, red, button_4)
        draw_text('PLAY', font, white, screen, 65, 100)
        draw_text('Controls', font, white, screen, 65, 200)
        draw_text('Options', font, white, screen, 65, 300)
        draw_text('QUIT', font, white, screen, 65, 400)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def play():
    running = True
    while running:
        screen.blit(background, (0, 0))

        Play = pygame.Rect(20, 20, 70, 30)
        pygame.draw.rect(screen, black, Play)
        draw_text('PLAY', font, red, screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def controls():
    running = True
    while running:
        screen.blit(background, (0, 0))

        Play = pygame.Rect(20, 20, 120, 30)
        pygame.draw.rect(screen, black, Play)
        draw_text('Controls', font, gold1, screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    while running:
        screen.blit(background, (0, 0))

        Play = pygame.Rect(20, 20, 110, 30)
        pygame.draw.rect(screen, black, Play)
        draw_text('Options', font, chartreuse1, screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def quit():
    pygame.quit()
    sys.exit()


game()
