from turtle import *
from utilities import *
from random import choice
from my_network import Network
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
screen = pygame.display.set_mode((1000, 1000), pygame.RESIZABLE)
font = pygame.font.SysFont(None, 40)


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
                my_main()
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
    pygame.init()

    path = Turtle()
    writer = Turtle()

    aim = vector(5, 0)
    pacman = vector(-40, -80)

    ghosts = [
        [vector(-180, 160), vector(5, 0)],
        [vector(-180, -160), vector(0, 5)],
        [vector(100, 160), vector(0, -5)],
        [vector(100, -160), vector(-5, 0)],
    ]

    state = {'score': 0}

    tiles = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]

    def square(x, y):
        "Draw square using path at (x, y)."
        path.hideturtle()
        path.up()
        path.goto(x, y)
        path.down()
        path.begin_fill()

        for count in range(4):
            path.forward(20)
            path.left(90)

        path.end_fill()

    def offset(point):
        "Return offset of point in tiles."
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        index = int(x + y * 20)
        return index

    def valid(point):
        "Return True if point is valid in tiles."
        index = offset(point)

        if tiles[index] == 0:
            return False

        index = offset(point + 19)

        if tiles[index] == 0:
            return False

        return point.x % 20 == 0 or point.y % 20 == 0

    def world():
        r = random.randint(0, 62)
        if r == 0:
            mixer.music.load("IndustryBabyBackground1.mp3")
        elif r == 1:
            mixer.music.load("SevenNationBackground2.mp3")
        elif r == 2:
            mixer.music.load("SweetDreamsBackground3.mp3")
        elif r == 3:
            mixer.music.load("AvengersBackground4.mp3")
        elif r == 4:
            mixer.music.load("GodzillaBackground5.mp3")
        elif r == 5:
            mixer.music.load("SunflowerBackground6.mp3")
        elif r == 6:
            mixer.music.load("ComeAndGetYourLoveBackground7.mp3")
        elif r == 7:
            mixer.music.load("BackInBlackBackground8.mp3")
        elif r == 8:
            mixer.music.load("SmellsLikeTeenSpiritBackground9.mp3")
        elif r == 9:
            mixer.music.load("MandalorianBackground10.mp3")
        elif r == 10:
            mixer.music.load("WeAreTheChampionsBackground11.mp3")
        elif r == 11:
            mixer.music.load("AllStarBackground12.mp3")
        elif r == 12:
            mixer.music.load("BlueBackground13.mp3")
        elif r == 13:
            mixer.music.load("ChainBackground14.mp3")
        elif r == 14:
            mixer.music.load("NeverGonnaGiveYouUpBackground15.mp3")
        elif r == 15:
            mixer.music.load("RasputinBackground16.mp3")
        elif r == 16:
            mixer.music.load("RobberyBackground17.mp3")
        elif r == 17:
            mixer.music.load("HarderBetterFasterStrongerBackground18.mp3")
        elif r == 18:
            mixer.music.load("MegalovaniaBackground19.mp3")
        elif r == 19:
            mixer.music.load("GangstasParadiseBackground20.mp3")
        elif r == 20:
            mixer.music.load("CrabRaveBackground21.mp3")
        elif r == 21:
            mixer.music.load("Spider-ManBackground22.mp3")
        elif r == 22:
            mixer.music.load("DontStopMeNowBackground23.mp3")
        elif r == 23:
            mixer.music.load("BohemianRhapsodyBackground24.mp3")
        elif r == 24:
            mixer.music.load("SuperMarioBrosBackground25.mp3")
        elif r == 25:
            mixer.music.load("StarWarsImperialThemeBackground26.mp3")
        elif r == 26:
            mixer.music.load("InTheEndBackground27.mp3")
        elif r == 27:
            mixer.music.load("NumbBackground28.mp3")
        elif r == 28:
            mixer.music.load("StressedOutBackground29.mp3")
        elif r == 29:
            mixer.music.load("BuildOurMachineBackground30.mp3")
        elif r == 30:
            mixer.music.load("MinecraftSwedenBackground31.mp3")
        elif r == 31:
            mixer.music.load("TakeOnMeBackground32.mp3")
        elif r == 32:
            mixer.music.load("FadedBackground33.mp3")
        elif r == 33:
            mixer.music.load("BegginBackground34.mp3")
        elif r == 34:
            mixer.music.load("ThisIsAmericaBackground35.mp3")
        elif r == 35:
            mixer.music.load("BringMeToLifeBackground36.mp3")
        elif r == 36:
            mixer.music.load("RapGodBackground37.mp3")
        elif r == 37:
            mixer.music.load("XGonGiveItToYaBackground38.mp3")
        elif r == 38:
            mixer.music.load("MonteroBackground39.mp3")
        elif r == 39:
            mixer.music.load("WhereTheHoodAtBackground40.mp3")
        elif r == 40:
            mixer.music.load("ItWasntMeBackground41.mp3")
        elif r == 41:
            mixer.music.load("CelebrateGoodTimesBackground42.mp3")
        elif r == 42:
            mixer.music.load("StarBoyBackground43.mp3")
        elif r == 43:
            mixer.music.load("InDaClubBackground44.mp3")
        elif r == 44:
            mixer.music.load("AstronautInTheOceanBackground45.mp3")
        elif r == 45:
            mixer.music.load("GetLuckyBackground46.mp3")
        elif r == 46:
            mixer.music.load("CountingStarsBackground47.mp3")
        elif r == 47:
            mixer.music.load("DriversLicenseBackground48.mp3")
        elif r == 48:
            mixer.music.load("EyeOfTheTigerBackground49.mp3")
        elif r == 49:
            mixer.music.load("RansomBackground50.mp3")
        elif r == 50:
            mixer.music.load("EverybodyBackground51.mp3")
        elif r == 51:
            mixer.music.load("IWantItThatWayBackground52.mp3")
        elif r == 52:
            mixer.music.load("PrayForMeBackground53.mp3")
        elif r == 53:
            mixer.music.load("AllTheStarsBackground54.mp3")
        elif r == 54:
            mixer.music.load("MinecraftWetHandsBackground55.mp3")
        elif r == 55:
            mixer.music.load("GDFRBackground56.mp3")
        elif r == 56:
            mixer.music.load("ImmortalsBackground57.mp3")
        elif r == 57:
            mixer.music.load("CenturiesBackground58.mp3")
        elif r == 58:
            mixer.music.load("PacManFeverBackground59.mp3")
        elif r == 59:
            mixer.music.load("WakeMeUpBackground60.mp3")
        elif r == 60:
            mixer.music.load("TheNightsBackground61.mp3")
        elif r == 61:
            mixer.music.load("BelieverBackground62.mp3")
        elif r == 62:
            mixer.music.load("RadioactiveBackground63.mp3")
        mixer.music.play(-1)

        Screen().bgcolor('black')
        path.color('blue')

        for index in range(len(tiles)):
            tile = tiles[index]

            if tile > 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)

                if tile == 1:
                    path.up()
                    path.goto(x + 10, y + 10)
                    path.dot(2, 'white')

        update()

    def move():
        writer.clear()
        writer.write(state['score'])
        clear()

        if valid(pacman + aim):
            pacman.move(aim)

        index = offset(pacman)

        if tiles[index] == 1:
            tiles[index] = 2
            state['score'] += 1
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

        up()
        goto(pacman.x + 10, pacman.y + 10)
        dot(20, 'yellow')

        for point, course in ghosts:
            if valid(point + course):
                point.move(course)
            else:
                options = [
                    vector(5, 0),
                    vector(-5, 0),
                    vector(0, 5),
                    vector(0, -5),
                ]
                plan = choice(options)
                course.x = plan.x
                course.y = plan.y

            up()
            goto(point.x + 10, point.y + 10)
            dot(20, 'red')

        update()

        for point, course in ghosts:
            if abs(pacman - point) < 20:
                return

        Screen().ontimer(move, 70)

    def change(x, y):
        "Change pacman aim if valid."
        if valid(pacman + vector(x, y)):
            aim.x = x
            aim.y = y

    Screen().setup(420, 420, 370, 0), pygame.RESIZABLE
    Screen().tracer(0, 0)
    writer.hideturtle()
    writer.goto(160, 160)
    writer.color('white')
    writer.write(state['score'])
    Screen().listen()
    hideturtle()
    Screen().onkey(lambda: change(5, 0), 'Right')
    Screen().onkey(lambda: change(-5, 0), 'Left')
    Screen().onkey(lambda: change(0, 5), 'Up')
    Screen().onkey(lambda: change(0, -5), 'Down')

    world()
    move()
    done()


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
